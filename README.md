# Damien Meere - BT Ireland
### Full Stack Frameworks with Django Milestone Project - Code Institute

## Introduction

This project website will highlight my capability to employ the various tools illustrated throughout the entirety of the Code Institute programme. The purpose of this project is to
build a full-stack django-based site, with the requisite business logic to support all aspects of an online store. This django-enabled site allows an admin to create, store and 
manipulate product records, which are then presented to the site visitors/customers. Customers can create their own profiles, view and sort all products depending on their requirements,
sign up for mailing lists, view the available inventory on products and leave reviews for products they have purchased. 

All functionality relating to both site admins and customers is laid out within the [UX + User Stories](#UX+User-Stories) section below. 

This project is built upon the Django framework and follows the model-template-view architecture pattern. Sqlite was utilised during development as the database for local testing.
Sqlite is a relational database management system (RDBMS) embedded within the application itself. Within the [deployed site](https://dmeere-thecomicstore.herokuapp.com/), Postgres is 
employed as the Database to house all data. Postgres is an open source object-relational database management system. The data structures and associated applications models are 
detailed in the [Database](#Database) section.

Utilising Django and the DBMS highlighted above, site admins, can access a customised Django-supported Admin Dashboard where they can Create, Read, Update and Delete records within the 
various application models (Products, Users, Orders, Product Reviews etc.), as illustrated in the following image:

![Django Dashboard](documentation/SiteImages/Admin_Dashboard.jpg)

Throughout the development of the project, [Git](https://git-scm.com/) & [Github](https://github.com/) were employed to support version control. The [Github Repository](https://github.com/damien-meere/full_stack_milestone) 
for the project is linked directly to the [Heroku-deployed site](https://dmeere-thecomicstore.herokuapp.com/).


## Table of Contents

- [Demo](#Demo)
- [UX + User Stories](#UX+User-Stories)
- [Technologies](#Technologies-Used)
- [Database](#Database)
- [Current Features](#Current-Features)
- [Future Features](#Future-Features)
- [Testing](#Testing)
- [Testing - Unresolved Bugs](#Testing-Unresolved_Bugs)
- [Deployment](#Deployment)
- [Internal Deployment](#Internal-Deployment)


## Demo
A live demo of the project can be found deployed to Heroku [Here](https://dmeere-thecomicstore.herokuapp.com/)


## UX+User-Stories

Describe User Stories from Excel

In particular highlight the Mailing list, Review and Inventory functions

[Back to top](#Introduction)

## Site Design

Page breakdowns across the site.

Defensive Design

[Back to top](#Introduction)
    
## Technologies Used

#### Languages, Frameworks, Editors, Tools & Version Control:

1. [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
2. [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
3. [Javascript](https://www.w3schools.com/jsref/)
4. [Python](https://www.python.org/)
5. [Bootstrap](https://getbootstrap.com/) - Responsive site functionality
5. [Django Web Framework](https://www.djangoproject.com/) - Architectural engine
6. [FontAwesome](https://fontawesome.com/) - Icons utilised throughout the site
7. [Git](https://git-scm.com/) - Support of Version Control
8. [Github](https://github.com/) - Host the repository of all previous versions of the build
9. [Gitpod](https://www.gitpod.io/) - Open-source prebuilt, collaborative development environments within your browser
10. [Heroku](https://www.heroku.com/) - Cloud platform as a service enabling deployment 
11. [Stripe](https://stripe.com/ie) - Online payment processing platform
12. [Postgres](https://www.postgresql.org/) - open source object-relational database system
13. [SQLite](www.sqlite.org) - light-weight relational database management system (RDBMS)


[Back to top](#Introduction)

## Database

During the early development and later local testing of the application, [SQLite](www.sqlite.org) was utilised as the database management system embedded within the 
application itself. This faciliated the early deployment of the User Registration and Authentication system through the django platform. Within the [deployed site](https://dmeere-thecomicstore.herokuapp.com/) 
on Heroku, [Postgres](https://www.postgresql.org/) was employed as the Database to house all data. Postgres is an open source object-relational database management system and is 
installed as an add-on within the Heroku application.

The structure of the database is as follows:

![Database Structure](documentation/database_structure_v3.jpg)

### User & UserProfile Models
Django’s authentication system provides the base structures for authorising, authenticating and accounts user interactions with the platform. The authentication system, bundled as 
a Django contrib module in django.contrib.auth, handles user accounts, groups, permissions and cookie-based user sessions. This default implementation includes the **User model** out of 
the box. User objects are the core of the authentication system. They represent the people interacting with the site and are used to facilitate things like access restrictions, user 
registration etc. Within Django’s authentication framework, these user objects represent all users on the site - both Customer and Admin. 'Superusers' or admin 'staff' users 
are just standard user objects with special attributes. The Primary Key for a user is an assigned User ID.

The primary attributes of the default user are:
*   username
*   password
*   email
*   first_name
*   last_name
*   staff status (added to differentiate access privilages)

![User Admin](documentation/SiteImages/Admin_Users.jpg)

The **UserProfile** model is directly associated with a specific User object, and is used to maintaining default delivery information for that individual. This model maintains a One-to-One 
relationship with it's associated User Object. On deletion of the referenced User object, the related UserProfile object is also deleted. The following fields provide all the information
required to fulfil any orders that the user might make through the site. This is bound directly to the Order model as a Foreign Key. 

*   default_phone_number
*   default_street_address1
*   default_street_address2
*   default_town_or_city
*   default_county
*   default_postcode
*   default_country

![User Profile Admin](documentation/SiteImages/Admin_User_Profile.jpg)

### Subscriber List

The **Subscriber List** Model facilitates the curation of all site users wishing to be part of the site's mailing list. The model maintains only the email address of users, as visitors
to the site can either sign up anonymously (i.e. without a profile) via the home page, or by ticking the subscribe button within the Profile page (once logged in). Logged in users can also
choose to unsubscribe from the list, by un-ticking this button. This process is described in greater detail in the [Current Features](#Current-Features) section.

*   subscriber_id
*   email

![Subscriber List Admin](documentation/SiteImages/Admin_subscribe_List.jpg)

### Product

The **Product** Model contains all details relating to the products being sold on the site. This model links to both the Order Line Item and the Product Review models as a Foreign Key.
The Product model itself contains the Category field as a Foreign Key, which facilitaes the differentation of various products types from the main page search functionality. The other
field within this model describe the product itself and it's status. For example, the SKU (Stock Keeping Unit) is product code that you can use to search and identify stock on hand 
from lists, invoices, or order forms. It's typically used to facilitate inventory management. The Name, Description, Price and Image field allow customers to view information about 
product before purchase. The has_sizes field is utilised to discern if a product is an item of clothing, and whether the customer should be able to pick the requisite size (S, M, L, XL etc.).
The Ratings field is tied directly to the **Product_Review** model. The value in this field is calculated by getting the average of all review scores submitted by confirmed purchasers
of the specific product. The Reviewing process will be discussed in more detail in the [Current Features](#Current-Features) section. Finally, the Stock_level Field is dtermined by 
site admin. When the admin sets this value, the users are presented with a notification on the product detail page to highlight current stock levels. When the stock level drops to a 
critical level, the customer is provided with a warning to promote the purchase. When the stock is exhausted (0 remaining), the ADD TO BAG button on the product detail page is removed.
This prevents users from adding a prodcut to their shopping bag, when we no long have the product in stock.

*   category
*   sku
*   name
*   description
*   has_sizes
*   price
*   rating
*   stock_level
*   image_url
*   image

**Product Admin**
![Product Admin](documentation/SiteImages/Admin_Product.jpg)

**Product Detail Admin**
![Product Detail Admin](documentation/SiteImages/Admin_Product_Detail.jpg)

### Product Review

The **Product Review** Model is utilised to harness feedback from confirmed product purchasers. Only those users that have completed an order (accessible via their profile) can 
submit a review for a product. Even then, they can only provide a review for a prodcut that are associated with their Order. The process or creating and viewing product reviews 
will be details in the [Current Features](#Current-Features) section. The various fields within the model support this function. The review_id field is utilised to uniquely identify
each review record within the datebase. The user field identifies the user that submits the review. This detail is used to populate the review section within the Product Detail
page. The Product field is a foreign key and associates the review with a specific product. On deletion of the product in question, all associated product reviews are deleted. The 
review (Text input) and Timestamp (gathered at the time of submission - `datetime.now()`) are used to provide additional information on the Product detail page. The prodcut detail 
page will tabulate the various reviews associated with the specific Product. Finally, the ratings field is just an integer value between 0-5. The user can select their input within a dropdown menu with submitting their review. The actual rating assigned to the Product
object itself is actually the average of all submitted review scores. On successful submission of a review, the ratings score is averaged across all reviews for that product. The 
result is saved to the original Product Object rating field, as detailed above. 

*   review_id
*   user
*   product
*   rating
*   review
*   timestamp

**Product Review Admin**
![Product Review Admin](documentation/SiteImages/Admin_Product_Review.jpg)

**Product Review Detail Admin**
![Product Review Detail Admin](documentation/SiteImages/Admin_Product_Review_Detail.jpg)

### Category

The **Category** Model is utilised to provide additional context to the Products (Foreign key within Product Model). The categories are used to differentiate and group products within
the store's inventory. The model is limited to two field that provide a name, and a "Friendly" version of that name

*   name
*   friendly_name

**Category Admin**
![Category Admin](documentation/SiteImages/Admin_Category.jpg)

### Order

### Order Line Item



## Current-Features

Admin Portal - Django based
Products pages + Navigation + toasts
Product Review + Rating
Shopping Bag + stripe
SKU Generator
Inventory function
Mailing List

[Back to top](#Introduction)

## Future-Features

Stock Keeping System (utilising the SKU)

## Testing
Validation against the User stories highlighted in previous sections was key. 
    
Therefore the following tests were conducted to ensure that the originally stated users stories were catered to:

All CSS, HTML and Javascript files were passed through code validators. The [CSS Validator](https://jigsaw.w3.org/css-validator/) & [HTML Validator](https://validator.w3.org)
checked the markup validity of Web documents against the w3c standards. the [JSHint](https://jshint.com/) utility was used to check for errors and potential problems in the
JavaScript code.

This site was tested across multiple browsers (Chrome, Safari, Firefox), and on multiple devices (Samsung Galaxy S9/S10, Samsung Galaxy Tab, Apple iPad, iPhone 6/7/8)
to ensure compatibility and responsiveness. As detailed in previous sections, depending on the screen size, elements will move and change size to ensure usability in unaffected by 
the changes.

[Back to top](#Introduction)

## Testing-Unresolved_Bugs



## Deployment
A live iteration of this project can be found deployed to [Heroku](https://dmeere-thecomicstore.herokuapp.com/)

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/damien-meere/Data-Centric-Development-Milestone-Project.git` 
into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.

>NOTE:
>Ensure that when testing with the Stripe-supported payment system, utilise the [Stripe Testing](https://stripe.com/docs/testing#cards) details. 
>Throughout the development of this project the followig details were utilised - Card number: 4242424242424242 (16-digit Card number), CVV & Date: Any digit combinations you wish.

You can also Clone this Repository to GitHub Desktop, by navigating to the [main page](https://github.com/damien-meere/full_stack_milestone) of the 
repository on GitHub, under the repository name, click Clone or download. Click Open in Desktop to clone the repository and open it in GitHub Desktop. Click Choose... and, 
using Windows Explorer, navigate to a local path where you want to clone the repository. For more information you can 
review the [GitHub site](https://help.github.com/en/articles/cloning-a-repository#cloning-a-repository-to-github-desktop).

To deploy the project to Heroku you will need to do the following:
1.  Create a new app on [Heroku](https://www.heroku.com/)
2.  Linked the app to its Github repository shown above
3.  Verify that the project has an up to date Procfile and requirements.txt
4.  Ensure you have Heroku set up as a remote repo (`git remote -v`)
5.  Push the project to the Heroku remote (`git push heroku master`)
6.  Set the requisite environmental variables/confirg vars on heroku:
    *   AWS_ACCESS_KEY_ID (S3 Application)
    *   AWS_SECRET_ACCESS_KEY (S3 Application)
    *   DATABASE_URL (Provisioned Postgres Database)
    *   SECRET_KEY
    *   STRIPE_PUBLIC_KEY
    *   STRIPE_SECRET_KEY
    *   STRIPE_WH_SECRET
8.  Restart all dynos.
9.  Open the app on Heroku and check to ensure that it's working correctly.

[Back to top](#Introduction)