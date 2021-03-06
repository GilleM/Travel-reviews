import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# part of the code of user registration taken from the Code Institute

@app.route("/")

@app.route("/get_destination")
def get_destination():
    """
        Render home page with available destinations from db
    """
    destinations = mongo.db.destinations.find()
    return render_template("destinations.html", destinations=destinations)


@app.route("/search", methods=["GET", "POST"])
def search():
    """
        Search destinations by the city and country name
    """
    query = request.form.get("query")
    destinations = mongo.db.destinations.find({"$text": {"$search": query}})
    return render_template("destinations.html", destinations=destinations)


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
        Sign up function
    """
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("sign_up"))

        sign_up = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(sign_up)

        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
  
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """
        Log In function
    """
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """
        render user profile from db
    """
    destinations = mongo.db.destinations.find()

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username, destinations=destinations)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """
        Log Out function
    """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add_destination", methods=["GET", "POST"])
def add_destination():
    """
        add destination collection function. user can add destination to db.
        user needs to log in first.
    """
    if request.method == "POST":
        place = {
            "city": request.form.get("city"),
            "country": request.form.get("country"),
            "travel_description": request.form.get("travel_description"),
            "best_memory": request.form.get("best_memory"),
            "advice": request.form.get("advice"),
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
            "destination_image_url": request.form.get("destination_image_url"),
            "extra_url": request.form.get("extra_url"),

        }
        mongo.db.destinations.insert_one(place)
        flash("New Place Successfully Added!")
        return redirect(url_for("get_destination"))

    return render_template("add_destination.html")


@app.route("/edit_destination/<place_id>", methods=["GET", "POST"])
def edit_destination(place_id):
    """
        edit destination in the destination collection section
    """
    if request.method == "POST":
        submit = {
            "city": request.form.get("city"),
            "country": request.form.get("country"),
            "travel_description": request.form.get("travel_description"),
            "best_memory": request.form.get("best_memory"),
            "advice": request.form.get("advice"),
            "due_date": request.form.get("due_date"),
            "created_by": session["user"],
            "destination_image_url": request.form.get("destination_image_url"),
            "extra_url": request.form.get("extra_url"),

        }
        mongo.db.destinations.update({"_id": ObjectId(place_id)}, submit)
        flash("Destination Successfully Updated!")
    place = mongo.db.destinations.find_one({"_id": ObjectId(place_id)})
    return render_template("edit_destination.html", place=place)


@app.route("/delete_destination/<place_id>")
def delete_destination(place_id):
    """
        delete function
    """
    mongo.db.destinations.remove({"_id": ObjectId(place_id)})
    flash("Destination Successfully Deleted")
    return redirect(url_for("get_destination"))


@app.route('/terms_and_conditions')
def terms_and_conditions():
    """
        Render term and condition section
    """
    return render_template("terms_and_conditions.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT"))
            )