# Damien Meere - BT Ireland
### Full Stack Frameworks with Django Milestone Project - Code Institute

This project website will highlight my capability to employ the various tools illustrated throughout the entirety of the Code Institute programme. The purpose of this project is to

build a full-stack django-based site, with the requisite business logic to control a centrally-owned dataset.


 On creation of a new course, the trainer specifies the maximum number of subscribers a course can take. In defining this value, only that number 
of trainees will be permitted to enrol on the course. All elements of the courses are editable except for the maximum subscriber value. On the trainer view, the 
trainer can quickly view what the uptake levels are for each course with a progress bar. The site also enables trainees to view course information, and view the uptake 
level. And once they have chosen a course, upon submission of their name and email, they will be given feedback as to whether their request has been successful of if 
there are no remaining spaces on a course.



## Table of Contents

- [Demo](#Demo)
- [Database](#Database)
- [UX + User Stories](#UX+User-Stories)
- [Technologies](#Technologies)
- [Site Notes](#Site-Notes)
- [Current Features](#Current-Features)
- [Future Features](#Future-Features)
- [Testing](#Testing)
- [Testing - Unresolved Bugs](#Testing-Unresolved_Bugs)
- [Deployment](#Deployment)
- [Internal Deployment](#Internal-Deployment)


    
## Demo
A live demo of the project can be found deployed to Heroku [Here](LINK TO BE PROVIDED)

    
## Database
![Database Structure](IMAGE TO BE PROVIDED)

Describe Categories
Describe Updated Products structure - Inventory
Describe SubscriberList Structure and Reasoning
Describe ProductReview Structure and Reasoning

## UX+User-Stories

Describe User Stories from Excel

In particular highlight the Mailing list, Review and Inventory functions
    
## Technologies
This project utilises the following technologies:
1. [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
2. [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
3. [Javascript](https://www.w3schools.com/jsref/)
4. [Python](https://www.python.org/)
5. [Django Web Framework](https://www.djangoproject.com/)
6. [FontAwesome](https://fontawesome.com/)
7. [Git](https://git-scm.com/)
8. [Heroku](https://www.heroku.com/)
9. [Stripe](https://stripe.com/ie)

## Current-Features

Admin Portal - Django based
Products pages + Navigation + toasts
Product Review + Rating
Shopping Bag + stripe
SKU Generator
Inventory function
Mailing List

## Future-Features


## Testing
Validation against the User stories highlighted in previous sections was key. 
    
Therefore the following tests were conducted to ensure that the originally stated users stories were catered to:

All CSS, HTML and Javascript files were passed through code validators. The [CSS Validator](https://jigsaw.w3.org/css-validator/) & [HTML Validator](https://validator.w3.org)
checked the markup validity of Web documents against the w3c standards. the [JSHint](https://jshint.com/) utility was used to check for errors and potential problems in the
JavaScript code.

This site was tested across multiple browsers (Chrome, Safari, Firefox), and on multiple devices (Samsung Galaxy S9/S10, Samsung Galaxy Tab, Apple iPad, iPhone 6/7/8)
to ensure compatibility and responsiveness. As detailed in previous sections, depending on the screen size, elements will move and change size to ensure usability in unaffected by 
the changes.

## Testing-Unresolved_Bugs



## Deployment
A live iteration of this project can be found deployed to [Heroku](https://dmeere-thecomicstore.herokuapp.com/)

To run locally, you can clone this repository directly into the editor of your choice by pasting `git clone https://github.com/damien-meere/Data-Centric-Development-Milestone-Project.git` 
into your terminal. To cut ties with this GitHub repository, type `git remote rm origin` into the terminal.

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
6.  Set the environmental variables/confirg vars on heroku to- IP: 0.0.0.0, PORT: 5000 
7.  Set the MONGO_URI environmental variable in the Heroku config vars 
8.  Restart all dynos.
9.  Open the app on Heroku and check to ensure that it's working correctly.
