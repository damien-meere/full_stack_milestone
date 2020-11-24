# Damien Meere - BT Ireland
### Full Stack Frameworks with Django Milestone Project - Code Institute

<p align="center">
    <img height="200" src="https://github.com/damien-meere/full_stack_milestone/blob/master/static/img/Comic-Store-Logo.png" alt="Comic Store Logo">
</p>

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
- [Site Design](#Site-Design)
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

The goal of project was to build a full-stack site with the business logic to support the sale of products to customers/site visitors. In this case,
the site supports a comic book store's online presence. The main actors involved in the site are **customers** (both logged in and anonymous), and the 
**site admin**. The various interations with the site can be broken out into 5 key domains:
*   Product View & Navigation
*   Registration and Individual User Account Functionality
*   Sort & Search of Products
*   Purchasing & Checkout
*   Admin & Product Management

The checklist used to track the user stories can be accessed here - ![Checklist - Excel](documentation/user_stories_models_v2.xlsx)

### Product View & Navigation
####    View products
All site users need to be able to identify items for purchase on the site with minimal effort. They need to be able to easily navigate to a central
respoitory and view all available products, and view high level information relating to each product (Name, Image, Price, Rating). This requirement is
fulfulled within the Main Product Page which presents a view of the Product catalogue. The design of this main product page will be presented and 
discussed in the upcoming section - [Site Design](#Site-Design).
####    View individual product details
All site users need to be able to focus in and delve into more specific details relating to a particular product - price, product description, 
applicable sizes for clothing, Product Images, Inventory Availability, Ratings and Product Reviews. All of this information is in place to attract the 
customer and promote the purchase of the product. This functionality Again, the design of the product detail page will be disucssed within the Site Design Section.
####    View categories of products
It's hugely important that site users are able to filter the list of avilable products. In many cases with these types of sites, there can be a 
substantial list of products available. Therefore, users need to be able to narrow the search parameters and limit their view of available products to
the general area of interest. In this case, this user story is fulfulled throught the assingment of categories to the individual products. This is detailed in the [Database](#Database), where the 
Product is presented in detail. The Categories, and their associated menu times enable the site users to select the type of product they wish to view. The following are the categories that site 
users can filter their product view on:
*   All products 
    *   Arranged by Price, 
    *   Arranged byRatings,
    *   Arranged by Category,
*   Books
    *   Comics
    *   Graphic Novels
    *   Magazines
*   Games
    *   Board Games
    *   Card Games
*   Apparel
    *   Hats
    *   Shirts
*   Special Offers
    *   New arrrivals
    *   Deals
    *   Clearence

![Category Menu](documentation/SiteImages/Categories_Menu.jpg)

####    Identify any clearence items or available discounts
As with all online stores, the primary goal is to drive business, and push customers to complete purchases. With that in mind, it's very important that customers can easily identify and take advantage
of offers/deals, and gain access to any price reductions across the site. In order to fulful this user story, the Special offers menu option was added, as detailed above. The Categories that fall under
this seciton heading are as follows:
*   New arrrivals
*   Deals
*   Clearence

By filtering the product list on on these categories, users can quickly identify priced reduced items. As such, it increases the chances of customers adding these items to their shopping bag.

####    View total for all queued items for purchase
Customers need to be able to keep track of the total cost of all items they're added to their shopping bag during a session. With each item that's added,
customers must be able to see at all times what charges they can expect, including any delivery charges. This user story is fulfilled though the use
of the shopping bag placeholder in the navbar (top right of page). At all times, this figure is updated based on the input of the user.

![Shopping Bag Total](documentation/SiteImages/Shopping_Bag_Total.jpg)

####    View Inventory Status of a product
It's important that when purchasing a product, Customers can be assured that their order can be fulfilled. With that in mind, when customers view the
details for a specific product, when they go to add the product to their shopping bag, they are presented with a view of the inventory level for that
specific product. As shown below, the inventory levels are reflected, so as to promote the completion of purchases.

![Inventory Level - In stock](documentation/SiteImages/Inventory_Level3.jpg)

![Inventory Level - Low stock](documentation/SiteImages/Inventory_Level1.jpg)

![Inventory Level - Out of stock](documentation/SiteImages/Inventory_Level2.jpg)


### Registration and Individual User Account Functionality
####    Register for an account
In order for customers to build a relationship with the site, they need to be able to create an account on the site. Having an individual user account
enables the user to save their details, so that when accessing the site in future, their details are already saved. This makes it easier for the user
to complete purchases, and so drives additional business. 

As detailed in the upcoming [Database](#Database) section, Django’s out-of-the-box authentication system provides the base structures for authorising, authenticating and accounting for all
user interactions with the platform. The authentication system is bundled within the Django contrib module in django.contrib.auth. This handles the creation of user accounts, 
facilitation of permissions and cookie-based user sessions.

####    Login/Logout
Site users need to be able to login and logout as they need to (e.g. shared devices). Again, building on the Django Authentication system, once a user account has been created, 
the users can very easily logout via the 'My Account' button on the navigation bar. So at any point on the site, the user can log out. 

####    Recover password if necessary
Site Users should be able to reset/recover their password should they need to. Again, the benefit of building this site on a robust platform like 
Django, is that the out-of-the-box authentication handles this functionality. Should the user require it, the authentication system will enable the user
to supply their email address and have they'll receive an e-mail allowing them to reset it.

####    Email confirmation with registration
It's important that the site have accurate email address information for all users. As we saw in the previous section, when resetting an account password,
when completing an Order and receiving the Order confirmation, the user email address is required to faciliate any communications with the user. Therefore,
when creating a new account, in order to finalise the account creation, the user is required to supply an email address. The user receives an email with
a link to verify their account and confirm their new account on the site. Until their email is verified, they cannot access their account. 

####    Up to date personalised account
One of the reasons for needing a profile is to maintain user information, so that users can view a history of their purchases, view order confirmations,
manage their delivery information. This user story is faciliated within the User's own profile page which enables the user to supply/update their 
delivery information, and view all previous orders.

####    Mailing List
It's important that stores cultivate a relationship with their customers. One good way of doing this is the creation of a mailing list, that enables
the store to circulate details of upcoming product releases, Price reductions, Ongoing Deals, Upcoming events etc. Within this site, this user story
is facilitated through two mechanisms. Anonymous users (with no Profile), can sign up to be a part of the mailing list via the mailing list button on
the home page. Customers with a registered account can elect to join the mailing list via their profile page, where they cna check the checkbox to join.



### Sort & Search of Products
####    Sort products into an appropriate order
As highlighted in previous user stories, central to any eCommerce site is the capability to effectively sort product lists so as to easily identify requisite products based on chosen 
criteria. To facilitate this capability, within the navbar, the site users have the option of sorting all products according to Price, Rating or Category. 

####    Sort products into categories
Site users need to be able to quickly locate the products they require. the longer it takes a user to find what they want, the more likely it is that they will take their business elsewhere. Therefore
to facilitate easier filtering of products, users can limit their view of products within the specific categories as detailed in the [View Category](#View-categories-of-products) user story. They can
simply select the requisite category from the navbar.

####    Search for products by name or description
Customers may have more specific criteria that they are searching for. So rather then just relying on broad categorys to try and isolate the requisite product, customers can specifically input their
own search parameters to either identify a single product, or zone in on a number of products that match the users inputted search criteria. This user story is faciliated via the search field within
the sites nav bar. When the user inputs their parameters, the Name and Description field of each product is queried. If any products match that criteria, they are presented to the user.

####    Easily view search results
Search parameters entered by a user can return a broad range of results, depending on the criteria entered. Therefore depending on the results, users must still be presented with a suitbale view to 
peruse through the resultant list of products. This user story is fulfilled within the site as when the user inputs a search parameter, the results are presented to the user in the exact same format
as when products are sorted or filtered from the navbar menu.



### Purchasing & Checkout
####    Select size (where applicable) and quantity of product for purchasing
Within the site certain items, typically clothing, require input from the user to select the requisite sixe (Small, medium, Large, Extra-Large etc.) Where appropriate, customers preference  with regards
the item size needs to be harnessed. Within the Product management menu (available to superusers), and the Django admin portal, Site Admins can create/edit products. When they do, the admin has the 
option to determine whether the product "Has Sizes". If the Admin user responds with a Yes, when a customer accesses the specific Product detail page, they are presented with an option to select the 
required size as illustrated below.

![Size Selector](documentation/SiteImages/size_selector.jpg)

####    View all items that I've selected to add to shopping bag
Once a customer has selected (Added to their Bag) all products they wish to purchase, they need to be able to review this product list before proceeding to the payment. Therefore to fulfil this 
user story, the customer can view a list of all products currently in their shopping bag by selevting the shopping cart icon in the top right of the site. Below this icon is the current total cost
of all items in the bag. Once the users selects this button they are presented with a list of all items they've added.

####    Adjust quantities of items in shopping bag
Once a user has gotten to the point of adding products to their shopping bag, it needs to be as easy as possible to proceed with a purchase. To ensure that customers can proceed to the payment phase 
without issue, they need to be able to edit the contents of their bag, right up until we begin processing their payment. To facilite this user story, within the shoping bag, custerms have the opportunity
to edit the contents of the bag. Either deleting items, or adjusting the quantity field of the item before proceeding. When they update their order quantities, the Grand Total value is updated to 
reflect the new order details, before the user proceeds to the payment.

####    Enter payment details
As with any eCommerce site, the customers need to be able to complete the purchase of their chosen items. And again, the process of gathering the payment information and completing the transation 
needs to be as hassle free as possible to ensure customers have no reason to leave. Once the customer has reviews their shopping bag and selected the 'Secure Checkout' button, they are brought to 
the Checkout page. It's here that this user story is fulfilled. If the user has a profile, their delivery information may already be populated. However, at the botton of the screen, the user can 
input their credit card details, as illustrated below. This card processing functionality is supported by [Stripe](https://stripe.com/ie), an online payment processing platform.

![Payment Details](documentation/SiteImages/payment_details.jpg)

####    View order confirmations
Once a customer entered their card details and elected to proceed with a purchase, they need to be given all details related to the Order to ensure there are no discrepancies. Therefore, to fulfill
this user story, on completion of an Order payment, the customer is presented with a complete breakdown of the processed Order. This Order confirmation contains details of the products included in 
the order, the Delivery address, and the breakdown of the associated charges as illustrated below:

![Order Confirmation](documentation/SiteImages/Order_Confirmation.jpg)

####    Receive Email confirmation after completing purchase
It's important that customers are able to maintain records of their purchases off the site. To fulfil this user story, when an order is successfully processed, an email copy of the order confirmation
is also emailed to the customer.


####    Provide Review and Rating of products purchased
Within eCommerce sites, user feedback is essential to building confidence in your service. Customer feedback in the form of reviews and product ratings are essential components in building this confidence.
To fulfil this user story, if a user has completed an order, they have an opportunity to review the products from that order. Within the customers profile page, all orders associated with that user account
are presented. The customer can select the order number to view specific information about each other. Within the Order details, the customer can elect to leave a review as illustrated below. The Product
Review page allows the user to provide a review for only the products that were within the Order. They can select a rating (between 0 - 5), and a text input.

![Prodcut Review](documentation/SiteImages/product_review.jpg)

This information is appended to the specific product's detail page, and is used to inform the other customers and promote purchases. More information on this feature is contained within the [Current Features](#Current-Features) section.



### Admin & Product Management
####    Add products
Add new products to site

####    Edit/update existing products
Change details of existing products

####    Delete products
Remove products no longer for sale on the site

####    Update inventory number for item
Add warning when stock drops below a certain level, only applow users to purchase items in stock

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
registration etc. 

Within Django’s authentication framework, these user objects represent all users on the site - both Customer and Admin. 'Superusers' or admin 'staff' users 
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
page. 

The Product field is a foreign key and associates the review with a specific product. On deletion of the product in question, all associated product reviews are deleted. The 
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

The **Order** Model is one of the key models supporting the checkout application, and as such, the purchasing capability within the site. The Order Model is used to harness the various
pieces of information required do fulfil a customers order (Delivery Information), harnessed from the User Profile (for logged in users).

The Order model links directly to the UserProfile model (Foreign Key) and as such binds an order to a specific user profile. Order Model contains all the  The Order Model also details
the various costs associated with an order (i.e. Delivery Cost, Order Total, Grand Total). These values are dependant on the associated Order Line Items (Detailed Below). The Stipe 
Payment ID contains the identifier that can be matched against Stripe records to ensure payment has been received before processing the customers order and arranging for the delivery
of the products within the Order.

*   order_number
*   user_profile = models.ForeignKey(UserProfile)
*   full_name
*   email
*   phone_number
*   country
*   postcode
*   town_or_city
*   street_address1
*   street_address2
*   county
*   date
*   delivery_cost
*   order_total
*   grand_total
*   original_bag
*   stripe_pid

**Order Admin**
![Order Admin](documentation/SiteImages/Admin_Order.jpg)

**Order Detail Admin**
![Order Detail Admin](documentation/SiteImages/Admin_Order_Detail.jpg)

### Order Line Item

The **Order Line Item** Model prodvides the specific prodcut context for the Order Model. The Order Line Item is bound to the Order Model and the Product Model. Both Order and Product
are Foreign Keys within the Order Line Item. When the user creates an order, the contents of their 'Shopping Bag' are iteratted over to create an individual Order Line Item instance,
which details the requisite order number, the requisite product ID, the details of prodcut size where applicable (in the case of clothing) the quantity, and finally the total for that 
particular line item, based on the aforementioned information. Within the Admin interface, the Order Line Items are visible within the output of the specific associated Order, as illustrated
below.

*   order = models.ForeignKey(Order
*   product = models.ForeignKey(Product
*   product_size
*   quantity
*   lineitem_total

**Order Line Item Admin**
![Order Line Item Admin](documentation/SiteImages/Admin_Order_Line_Item_Detail.jpg)

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
Price Reduction notifications
Complete Order on items with no stock - Added to back order or Opt out of purchase

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

###### <i>Disclaimer: This project (Milestone 4) was created for educational purposes as part of the Code Institute's Full Stack Software Development Course.</i>

<p align="center">
    <img height="150" src="https://github.com/damien-meere/full_stack_milestone/blob/master/static/img/Comic-Store-Logo.png" alt="Comic Store Logo">
</p>