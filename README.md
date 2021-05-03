# TRAVEL REVIEW PROJECT

**Code Institute - Milestone Project for Data Centric Development**

![pic](wireframes/proba.jpg)

Welcome to my third Code Institute milestone project that you can check out by clicking on [here](https://travel-reviews-project.herokuapp.com/)

[GitHub repository](https://github.com/GilleM/Travel-reviews)

<br/>

## Table of Contents - update them when you finish the sections!!!
***

1. [UX](#ux)<br/>
2. [Features](#features)<br/>
    - 2.1. [Our travels](#our-travels)<br/>
    - 2.2. [My reviews](#my-reviews)<br/>
    - 2.3. [Add destination](#add-destination)<br/>
3. [Technologies Used](#technologies-used)<br/>
4. [Database architecture](#database-architecture)<br/>
5. [Testing](#testing)<br/>
    - 5.1. [Making a shared destination library](#making-a-shared-destination-library)<br/>
        - 5.1.1. [Create a user account](#create-a-user-account)<br/>
        - 5.1.2. [User personal destination library](#user-personal-book-library)<br/>
        - 5.1.3. [Our travels home page](#our-travels-home-page)<br/>
        - 5.1.4. [Search in the destinations](#search-in-the-destinations)<br/>
    - 5.2. [The website validation](#the-website-validation)<br/>
6. [Deployment](#deployment)<br/>
    - 6.1. [GitHub](#gitHub)<br/>
    - 6.2. [Heroku](#heroku)<br/>
7. [Content](#content)<br/>
8. [Media](#media)<br/>
9. [Acknowledgements](#acknowledgements)<br/>
10. [Disclaimer](#disclaimer)<br/>

<br/>

## Project Description
***
**Travel Review Project** is one of the milestone projects I did at the Code Institute Full Stack Developer course. The main requirements were to make a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. We needed to respect CRUD functionality and to design a database structure that would suit well for required domain.

I decided to design Travel review site. The site requires registration. Once registered, you can leave your own review, tell the reasons behind your travels and give travel advice to others. Even more, you can search for a specific destination and read other people's added destination(s). After leaving yours, you can edit or delete it. 
The choice of this subject was pretty easy; lots of people like to travel and are willing to listen to other people's experience. 


## UX

***

In this paragraph I'm about to provide insight into my UX process, 
focusing on who this website is for, what it is that they want to achieve 
and how my project is the best way to help them achieve these things.


### Project Goals

- to create a website that is fully responsive on mobiles, tablets, laptops and desktops,
- to make a page with interface design, providing a logical structure which is easy to follow,
- to make a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records,
- to respect CRUD functionality so users can create, read, edit and delete the contents they wrote,
- to include "Search field" so users can get familiar with the destinations they would like to go,
- to write interactive JavaScript code so it can help with more intuitive UX (e.g. navbar on mobile devices)
- generally, to make an interesting and usefull backend web page that can help travellers to leave their experience and read the others' in order to get more information

### The business goals of this website is:

- the page could possibly be part of some tourist agency's website that could draw peoples' attention on travelling and participating with the travel's community 

### User Stories

- as travel lover, I'd like to read other people's experience and leave mine,
- as a new user, I'd like the page to have easy to follow and understandable, not to complex UX
<br/>
<br/>

##  Five Planes Method
***
## 1. Strategy

The main goal of the website is to help tourists with the information about particular place. They can read other users' experience and leave theirs. All should be done in a friendly and interesting way so that even if a user is not travelling anywhere, they can read others experience if nothing then for fun.
My personal goal, on the other hand, was to well understand the back-end logic, MongoDB, Flask as well as Python rules, so I could create the first blog.


## 2. Scope
My goal in design was to make everything as structured and intuitive as possible. Register, log in, add/edit/delete your destination, read other users' destination, search for destination, log out. 
I introduced social links that lead to random pages, as well as the link for the Terms and Conditions. 


## 3. Structure


 _Our Travels_ page:
*   **navbar** is on the top, coloured in black. It is the same for the whole pages. In the middle of it is the logo I created for Travel review purpose and on the right are categories: _Our Travels_, _My Profile_, _Add destination_ and _Log Out_. When not registered, _Log Out_ is not there, but _Log In_ and _Sign Up_ appear.

* The **central part** is composed of the search field that is centered above the flexbox section of Materialize's Card Reveal. Those cards have image and name of the destination and it reveals more information of the travel once button is clicked. They are nicely distributed and easy to use.
Below each image there is the link icon if the link is provided. Otherwise it is not visible. Next to it is abovementioned button that reveals the information about the destinations (the categories are listed in the central part of the _Add destination_ category).

* **Footer** includes social links, a link for _Terms and Conditions_ with the text: Website created by Matea Leka © 2021.



 _My Profile_ page:
*   **navbar** - as in _Our Travels_ page.

* The **central part** has the user profile name. Below we can see the Materialize cards done only by the logged in User and also distributed in flex. This time they can be Edited and Deleted.

* **Footer** - as in _Our Travels_ page.


 _Add destination_ page:
*   **navbar** - as in _Our Travels_ page.

* The **central part** - Below the form container there's centered "Add destination" header. <br/>
The form below is composed of the following fields:
    - City
    - Country
    - Travel description
    - Best memory
    - Advice to others
    - Date of travel/stay
    - Destination cover link
    - Extra link, if any
Left to each field there's an icon.
Below the form is a _Submit_ button. 

* **Footer** - as in _Our Travels_ page.

_Log In_ and _Sign Up_ pages:
*   **navbar** - as in _Our Travels_ page.

* The **central part** - The header is centered on the top of the form. The form in both consists of providing the Username and the Password as well as _Submit_ button below the form.
On the _Sign Up_ page there is checkbox provided that the new user needs to agree on terms and conditions provided. They open on new tab once clicked on. The _Log In_ page has additional link under the form that leads to Register form if the user doesn't have an account.

* **Footer** - as in _Our Travels_ page.


## 4. Skeleton       
### Wireframe
I used Balsamiq to develope the wireframes for mobile, tablet and laptop/desktop size. 

You can check them by clicking on one of the following links:

FIX THE LINKS!!!, ADD WIREFRAMES

+ [Our Travels Page](https://gillem.github.io/Travel.reviews/wireframes/wireframe_our_travels.html)

+ [My Profile](https://gillem.github.io/Memory-game/assets/wireframes/wireframe_game_page.html)

+ [Add destination](https://gillem.github.io/Memory-game/assets/wireframes/wireframe_game_page.html)

+ [Log In](https://gillem.github.io/Memory-game/assets/wireframes/wireframe_game_page.html)

+ [Sign Up](https://gillem.github.io/Memory-game/assets/wireframes/wireframe_game_page.html)

## 5. Surface

I wanted to have all the pages vivid and well organized, paying extra attention to responsiveness and margins. I tried to keep the same consistent colors, so black, dark purple and white with a bit of light green and occasional teal buttons (more about colours in Colours section). I kept the right contrast between background and text which makes it easy readable.









## Deployment

### GitHub

This part explain how to, clone this repository from GitHub, or work the project  from a local copy and finally deploy it to Heroku, for this purpose you need to have  Python (verson 3.0) installed, Github, MongoDB and Heroku account.

It is possible to deploy this project in GitHub as your development environment with following these steps:

##### Cloning of the Repository

* In your IDE CLI type:

```
git clone https://github.com/GilleM/Travel-reviews.git
```
##### Installing the Requirements

* Install all requirements modules with following CL:

```
pip3 install -r requirements.txt
```
##### Creating Collections in MongoDB

* Login to your MongoDB account
* Create a cluster
* Create a database with following collections:
    * destinations
    * users

##### Setting up the environmental variables:

* Create a .gitignore file in the root directory
* Write `env.py` and `__pycache__/` into the .gitignore file
* create `env.py` file
* In the `env.py` file write following code with YOURPASSWORD, YOURCLUSTERNAME, YOURDABASENAME and YOURSECRETKEY

##### Running the app

* In the last line of `app.py` change `debug=False` to `debug=True`

* It is possible to run the application with following CL:

```
python3 app.py
```
### Heroku

You have to follow these steps to host this project to Heroku:

##### Setup the Heroku

* Create a Heroku account
* Create a new app and select your region

##### Prepare Local workspace for Heroku

* Make a requirements.txt file using follwing CL:

```
pip3 freeze --local > requirements.txt
```
(This is required for the Heroku to know which files need to be installed for the app)

* Make a Procfile in the CL:
```
echo web: python app.py > Procfile
```
(This is required for the Heroku to know at the entry point get the app up and running)

##### Push the files to Heroku

* In the CLI type:
```
heroku login -i 
```
(and fill in your username and password)

* Commit all the files to Herkou, in CLI type:

```
git push heroku master 
```
##### Setup the configuration variable in Heroku

* Go to your Heroku account and in the app setting
* Set the keys and values as follow:

| Key | Value |
 --- | ---
IP | 0.0.0.0
PORT | 5000
MONGO_URI | `mongodb+srv://root:YOURPASSWORD@YOURCLUSTERNAME.j4ah4.mongodb.net/YOURDATABASENAME?retryWrites=true&w=majority`
SECRET_KEY | `YOURSECRETKEY`
MONGO_DBNAME | `YOURDATABASENAME`

##### Run the App in Heroku

* Click Open app in the right corner of your Heroku account
* Click on the live link available in the address bar
