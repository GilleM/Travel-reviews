# Travel Reviews

**Code Institute - Third Milestone Project for  Data Centric Development**

![pic](wireframes/mockup-readme.png)

Welcome to my third Code Institute milestone project that you can check out by clicking on [here](https://travel-reviews-project.herokuapp.com/)

[GitHub repository](https://github.com/GilleM/Travel-reviews)

<br/>

## Table of Contents - update them when you finish the sections!!!
***

1. [Project Description](#project-description)
2. [UX](#ux)<br/>
    - 2.1. [Project Goals](#project-goals)<br/>
    - 2.2. [User Stories](#user-stories)<br/>
3. [Features](#features)<br/>
    - 3.1. [Five Planes Method](#five-planes-method)<br/>
        - 3.1.1. [Strategy](#strategy)<br/>
        - 3.1.2. [Scope](#scope)<br/>
        - 3.1.3. [Structure](#structure)<br/>
            - 3.1.3.1. [Our Travels](#our-travels)<br/>
            - 3.1.3.2. [My Profile](#my-profile)<br/>
            - 3.1.3.3. [Add destination](#add_destination)<br/>
            - 3.1.3.4. [Log In and Sign Up](#log-in-and-sign-up)<br/>
        - 3.1.4. [Skeleton](#skeleton)<br/>
            - 3.1.4.1. [Wireframes](#wireframes)<br/>
        - 3.1.5. [Surface](#surface)<br/>
            - 3.1.5.1. [Colour Scheme](#colour-scheme)<br/>
            - 3.1.5.2. [Typography](#typography)<br/>
    - 3.2. [Consistent features across all pages](#consistent-features-across-all-pages)<br/>
    - 3.3. [Features left to implement](#features-left-to-implement)<br/>
3. [Technologies Used](#technologies-used)<br/>
4. [Database architecture](#database-architecture)<br/>
5. [Testing](#testing)<br/>
    - 5.1. [Making a shared destination reviews](#making-a-shared-destination-reviews)<br/>
        - 5.1.1. [Create a user account](#create-a-user-account)<br/>
        - 5.1.2. [User personal destination reviews](#user-personal-destination-reviews)<br/>
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
**Travel Review Project** is one of the milestone projects I did at the Code Institute Full Stack Developer course. The main requirements were to make a MongoDB-backed Flask project for a web application that allows users to store and manipulate data records about a particular domain. We needed to respect CRUD functionality and to design a database structure that would suit well for the required domain.

I decided to design a Travel review site. The site requires registration. Once registered, you can leave your own review, tell the purpose of your travels and give travel advice to others. Additionally, you can search for a specific destination and read other people's added destinations. After leaving yours, you can edit or delete it. The choice of this subject was pretty easy: lots of people like to travel and are want to read about other people's experiences.


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
- to include a "Search field" so users can get familiar with the destinations they would like to go to,
- to write interactive JavaScript code so it can help with more intuitive UX (e.g. navbar on mobile devices)
- generally, to make an interesting and usefull backend web page that can help travellers to describe their experience and read others' in order to get more information

### The business goal of this website is:

- to be part of a tourist agency's website that could draw peoples' attention to travelling and participating with the travel's community

### User Stories

- as a travel lover, I'd like to read other people's experience and leave mine,
- as a new user, I'd like the page to have easy to follow, understandable, uncomplicated UX <br/> <br/>

## Features
***

This project consists of five main sections:

- Our Travels
- My Profile
- My reviews
- Log In 
- Sign Up


##  Five Planes Method

### Strategy

The main goal of the website is to help tourists with information about a particular place. They can read other users' experience and leave theirs. All should be done in a friendly and interesting way so that even if a user is not travelling anywhere, they can read others’ experience if for nothing other than for fun. My personal goal, on the other hand, was to understand back-end logic, MongoDB, Flask as well as Python rules, so I could create the first blog. <br/><br/>


### Scope
My goal in design was to make everything as structured and intuitive as possible. Register, log in, add/edit/delete your destination, read other users' destination, search for destination, log out. 
I introduced social links that lead to random pages, as well as the link for the Terms and Conditions. <br/><br/>


### Structure

#### Our Travels

* The **navbar** is on the top, coloured in black. It is the same for all the pages. In the middle of it is the logo I created for the purpose of travel review and on the right are categories: _Our Travels_, _My Profile_, _Add destination_ and _Log Out_. When not registered, _Log Out_ is not there. Instead, _Log In_ and _Sign Up_ appear.

* The **central part** is composed of the search field that is centred above the flexbox section of Materialize's Card Reveal. Those cards have the image and name of the destination and it reveals more information of the travel once the button is clicked. They are nicely distributed and easy to use. Below each image there is the link icon if the link is provided. Otherwise it is not visible. Next to it is the button mentioned above that reveals the information about the destinations (the categories are listed in the central part of the _Add destination_ category).


* **Footer** includes social links, a link for _Terms and Conditions_ with the text: _Website created by Matea Leka © 2021._ <br/><br/>


#### My Profile

* The **navbar** - as in _Our Travels_ page.

* The **central part** has the user profile name. Below we can see the Materialize cards done only by the logged in User and also distributed in flex. This time they can be Edited and Deleted.

* **Footer** - as in _Our Travels_ page. <br/><br/>

#### Add destination

* The **navbar** - as in _Our Travels_ page.

* The **central part** - Above the form container is centered the "Add destination" header. <br/> Left to each field listed below there's an icon.
Below the form is a _Submit_ button. <br/>
The form below is composed of the following fields:
    - City
    - Country
    - Travel description
    - Best memory
    - Advice to others
    - Date of travel/stay
    - Destination cover link
    - Extra link, if any 
<br/>

* **Footer** - as in _Our Travels_ page. <br/><br/>

#### Log In and Sign Up

* The **navbar** - as in _Our Travels_ page.

* The **central part** -  In the _Sign Up_ section the user needs to provide the username and password and agree to the terms and conditions of the webpage. In the _Log In_ page the user should provide a valid username and password and it has the additional link under the form that leads to a Register form if the user doesn't have an account. After log in, there is a profile page showing short info about the username. The header of both pages is centred at the top of the form. The form in both consists of providing the Username and the Password as well as _Submit_ button below the form.

* **Footer** - as in _Our Travels_ page. <br/><br/>


### Skeleton       
#### Wireframes
I used Balsamiq to develope the wireframes for mobile, tablet and laptop/desktop size. 

You can check them by clicking on one of the following links:

+ [Our Travels Page](https://github.com/GilleM/Travel-reviews/blob/master/wireframes/wireframe_our_travels.pdf)

+ [My Profile](https://github.com/GilleM/Travel-reviews/blob/master/wireframes/wireframe_my_profile.pdf)

+ [Add destination](https://github.com/GilleM/Travel-reviews/blob/master/wireframes/wireframe_add_destination.pdf)

+ [Log In](https://github.com/GilleM/Travel-reviews/blob/master/wireframes/wireframe_log_in.pdf)

+ [Sign Up](https://github.com/GilleM/Travel-reviews/blob/master/wireframes/wireframe_sign_up.pdf) <br/><br/>

### Surface

I wanted to have all the pages vivid and well organised, paying extra attention to responsiveness and margins. I tried to keep the same consistent colours, so black, dark purple and white with a bit of light green and occasional teal buttons (more about colours in the Colours section). I kept the right contrast between background and text which makes it easy readable. <br/><br/>

#### Colour Scheme


The patterns used for this project are taken from [Hero Patterns](https://www.heropatterns.com/) page. 


+ color: #110916;
+ pattern: Topography

![pic](wireframes/bg_photo_1.JPG)


+ color:  #134606;
+ pattern: Topography

![pic](wireframes/bg_photo_2.JPG)

+ color: #110916e8;
+ pattern: Topography

![pic](wireframes/bg_photo_3.JPG)


#### Typography

font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;


### Consistent features across all pages

* The navbar always contains the logo image and the links (that change depending if you're logged in or not)
* The footer with social links and Terms and Conditions <br/><br/>


### Features left to implement

* Introduce the comment section for destinations not necessarily added by the same user. <br/><br/>


## Technologies Used
***

The following technologies have been used in this project:

* [Python 3.8.2](https://www.python.org/download/releases/3.0/) 
    * Python is supposed to be the main hero of this project.
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
    * web framework written in Python.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * is used as templating language for Python and its depending framework Flask
* [MongoDB](https://www.mongodb.com/)
    * It is a document-oriented database program.
* [Heroku](https://heroku.com/)
    * It is a cloud platform to run this python project.
* [HTML](https://www.w3.org/TR/html52/) 
    * used to structure and presenting the content.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html)
    * used for styling.
* [JQuery](https://jquery.com/)
    * this project used JavaScript in the form of JQuery to simplify DOM manipulation.
* [Materialize 1.0.0](https://materializecss.com/)
    * CSS framework used for structuring and presenting the content.
* [FontAwesome](https://fontawesome.com/)
    * used to create icons. <br/><br/>


## Database architecture
***

This project has two main collections in the database: destinations and users. The database structure in MongoDB has been set as follow:

![pic](wireframes/database_representation.JPG) <br/><br/>


## Testing
***

### Making a shared destination reviews

In this app user can create reviews of their favorite destinations that they had visited and share it with others. They can edit and delete their reviews and read others people reviews. Like this, by reading about other people's experiences, users can get more information about the destinations they would like to go to.

This was achieved with the following sections: <br/><br/>

#### Create a user account


By clicking _Sign Up_, the user can create an account by providing a valid/unique username and password and agree to the standard term and conditions provided with the webpage.

![pic](testing/sign_in_user.png)
![pic](testing/sign_in_terms_and_conditions.png)

Once signed out, the user is directed to their profile page where the user profile can be seen on the page.

 ![pic](testing/registration_successful.JPG)

Once sing out, you should log in with the correct Username and Password.
 ![pic](testing/log_in_incorrect.JPG) <br/><br/>



#### User personal destination reviews

In this section, the user can write travel reviews and add them to their collections. 
The user needs to provide a valid city, country, travel description, best memory, advice to others, URL image of the destination and another URL if they have any.
Beneath the form, there's a button "Submit".

 ![pic](testing/submit_destination.png)


After submission, a flash message appears with the saying “New Place Successfully Added”.
 ![pic](testing/new_place_successfully_added.JPG)

<br/>
The new destination appears both: <br/>

- in _Our travels_ page, without possibility to edit/delete destination

- in _My Profile_ page with the possibility to edit the destination or to simply remove it from the database.

 ![pic](testing/added_destination_to_the_profile.png)

 In both example we can see the visible link icon if the extra link was provided at the time of adding (or editing) destination. Otherwise is hidden.
 
 By clicking on the _"Travel description"_ button, a card reveals with all the information that users provided for the pecific destination.
  ![pic](testing/added_revealed_destination.png)

The username of the user who added the destination is added at the end of the card.
![pic](testing/created_by.JPG)

After deleting the destination, we can see it disappears from our profile and the flash message informs us that the destination was deleted.

![pic](testing/destination_deleted_from_my_profile.JPG)
![pic](testing/destination_successfully_deleted.JPG) <br/><br/>


#### Our Travels home page

_Our Travels_ home page is the central page of the project. All the destinations created by users will appear on this page. There's no possibility to edit or delete anyone's destination and you can edit/delete yours just from _My Profile_ page. 

At the top of the page, just below navbar, we can see the search section.
 ![pic](testing/search_section.JPG)

Below it, there's a flexbox of cards among which you can see the **Cork, Ireland** destination from the previous example added to the main page.
 ![pic](testing/added_destination_list.png) <br/><br/>


#### Search in the destinations

You can search destinations by the city name or country.
Below you can see the the example of all the destinations with the country name "France".

 ![pic](testing/search_by_country.png) <br/><br/>



### The website validation

I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) and [W3C Markup Validation Service](https://validator.w3.org/) to check the validity of the website code. All the pages, as well as the CSS page, passed validation tests.
I checked the validation of each page by clicking on the right button and choosing _"View page source"_. I copied the code directly into the validation service page. 

 ![pic](wireframes/validation_passed.JPG) <br/><br/>
 ![pic](wireframes/validation_css_passed.JPG) <br/><br/>


## Deployment
***

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

## Content 

I made Terms and Conditions template using  [LawDepot page](https://www.lawdepot.com/contracts/website-terms-and-conditions/?loc=IE&pid=googleppc-118180551342-514404739913_sl-ggkey_terms%20and%20conditions&gclid=Cj0KCQjws-OEBhCkARIsAPhOkIY_gkn2J6fITunWiaqiBjtvVWIPjkE1hSI2SzsDM8Vp41ZYxrSor6QaAmK9EALw_wcB&webuser_data_id=125207795) which content I changed a bit.



## Media

I made the logo image by using [Canva page](https://www.canva.com/) - a graphic design platform, used to create social media graphics, presentations, posters, documents and other visual content.

The site requires from users to copy the url link of the destinations they visited. I don't own any copyrights. The URLs of these images can be various and taken anywhere.


## Acknowledgements
I acknowledge my mentor Gerard McBride for the guidance on this project.

## Disclaimer
Please contact me if you have any issue regarding copyright content. This project is only for educational purposes. <br/>
email: matea.leka@gmail.com