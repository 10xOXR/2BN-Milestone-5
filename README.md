[![Build Status](https://travis-ci.org/10xOXR/2BN-Milestone-5.svg?branch=master)](https://travis-ci.org/10xOXR/2BN-Milestone-5)

#   [The Unicorn Attractor - Issue Tracker](https://django-2bn-unicorn.herokuapp.com/)

Welcome to the issue tracker for the world's leading dating app - The Unicorn Attractor!

With The Unicorn Attractor, you'll meet new people that share in your Unicorn love. Think of us as your most dependable wingman - wherever you go, we’ll be there, offering all the possibilities of riding off into the sunset!

---
 
## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
        - [**Framework**](#framework)
        - [**Color Scheme**](#color-scheme)
        - [**Typography**](#typography)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-left-to-implement)

3. [**Technologies Used**](#technologies-used)

4. [**Testing**](#testing)
    - [**Automated Testing**](#automated-testing)
    - [**Manual Testing**](#manual-testing)
    - [**Validators**](#validators)
    - [**Compatibility**](#compatibility)

5. [**Deployment**](#deployment)
    - [**Local Deployment**](#local-deployment)
    - [**Remote Deployment**](#remote-deployment)

6. [**Credits**](#credits)
    - [**Content**](#content)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

This is actually the final project in my Full-Stack Software Development course with [Code Institute](https://codeinstitute.net/full-stack-software-development-diploma/), in the **Full-Stack Frameworks** module.

The brief provided requires the creation of, *"a web application that allows users to submit tickets to an online issue tracker called the Unicorn Attractor, where bugs can be submitted for free, but feature requests require a nominal fee"*. 

### User Stories

As a user, I want to be able to _____________:

- Create an account
- Log into the site
- Log out of the site
- Have a profile page
- Fully edit my profile details and upload a picture
- Change my password
- Delete my account
- See all of my submitted bug tickets and feature requests
- View all bug and feature request tickets
- Unlock achievements for my participation in the site
- View full details of any bug/feature
- Comment on a bug ticket for free
- Upvote a bug to indicate that I am also experiencing the issue
- Comment on a feature request for free
- Upvote a feature request for a fee to indicate that I wish this developed as a priority
- Create a bug ticket/feature request
- Be charged securely for feature requests
- See the current progress of bugs and features
- View charts/graphs showing how many bugs or features are tended to, as well as the highest-voted bugs and features
- View information on the App being offered


### Design

The design of the site is based on standard Materialize elements, with their colouring altered to be bright and colorful. Bug Reports and Feature Requests are displayed as cards, showing a brief summary of the ticket along with information on how many views and favourites that each has.

#### Framework

Frameworks used in the project are:

 - [Materialize 1.0.0](https://materializecss.com/)
    - Using the Materialize framework allowed for the development of a clean and modern user interface with minimal need to override or alter the default settings in most cases.
- [Django 1.11.22](http://flask.pocoo.org/)
    - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- [jQuery 3.4.1](https://code.jquery.com/jquery/)
    - Although mostly unbound from jQuery in version 1.0.0, Materialize still requires some jQuery in order to properly initialize its elements (such as dropdowns, carousels, etc.).

#### Color Scheme

Given the mythical nature of unicorns, and their representation in popular culture, the site features a bright color scheme with heavy emphasis on pinks and purples. A balance has been struck so that the site doesn't appear garish or off-putting to users.

#### Typography

The primary fonts used on the site are those provided by the Materialize framework. The Google font [Baloo Tamma](https://fonts.google.com/specimen/Baloo+Tamma) has been used for titles and main headings.

### Wireframes

[Balsamiq Wireframes](https://balsamiq.com/) was used to create all of the wireframes during the design phase of this site.

These can be found using [this link](https://github.com/10xOXR/2BN-Milestone-5/tree/master/wireframes).

##### back to [top](#table-of-contents)

---

## Features

All required feature as detailed in the brief have been implemented, as well as several additional features that offer greater overall user experience.
 
### Existing Features

**Status-dependant Navbar**

The options that a user will see displayed in the navbar are dependant on whether or not they are logged in.
- Users that are not logged in will see:
    - The Unicorn Attractor
    - Tickets
    - Statistics
    - Register
    - Log In
- Users that are signed into the site will see:
    - The Unicorn Attractor
    - Tickets
    - Statistics
    - Profile
    - Log Out

Admins will also see an additional link to the Django Admin panel.

**Create Account**

Users are able to create their own user account. The code checks against existing users in the database to ensure that the selected username is unique, and that both the username and password meet the minimum/maximum length requirements.

**User Profile Page**

Upon registering or logging into the site, users are directed to their own profile page. Here they can choose to edit their profile information, as well as upload a profile picture or leave the default image in place.

**Logout**

Users that have logged into the site may end their session at any time by clicking the 'Logout' button on the navbar. Django ends their session and redirects the user to the homepage.

**Pagination**

Only four tickets are displayed on the Tickets page so as not to overload the user with information. Pagination has been implemented to let users move through all the results that available.

**Ticket Filtering**

Users are able to filter the displayed tickets based on their status and/or type by using the dropdown menus at the top of the Tickets page.

**Create a Bug Report**

Users that have registered and logged in are able to create a Bug Report. They are only required to enter a title for the bug and a description of the issue that they are experiencing.

**Create a Feature Request**

Users may also create Feature Requests in a similar manner to creating a Bug Report. However, users are required to pay €100 via a credit/debit card before they may proceed to submit the ticket. The Stripe API allows this payment transaction to be processed securely.

**View Detailed ticket information**

When a user clicks any of the cards displaying ticket information they are directed to a page where they can view full details of the ticket. This includes:

- Who raised the ticket and their picture
- Current Status
- When the ticket was raised and last updated
- Full details of the issue

**Edit a Ticket**

Tickets may only be edited by either the user that created the ticket initially, or by an Admin. Editing a ticket is as simple as updating the information pre-populated into the relevant fields on the Edit Ticket page.

**Delete Ticket**

Tickets may only be deleted by either the user that created the ticket initially, or by an Admin. Clicking the delete button will trigger a modal asking the user to confirm the action and reminding them that this cannot be undone.

**Upvote/Downvote Tickets**

Any logged-in user may upvote a Bug Report for free by clicking the Upvote button on the Ticket Detail page. For Feature Requests, a modal will appear advising that there is a €5 fee for upvoting a Feature Request and allows the user to enter card details via the Stripe API to complete the process. Only once payment has been successful will the upvote be registered.

**Change Ticket Status**

Admins are able to change the current status of a ticket via dropdown below the other function buttons on the Ticket Detail page. This functionality is available only to Admin users.

**Comment on a Ticket**

All logged-in users are able to freely comment on any ticket that is not currently in 'Completed' status. At this point, users are informed that comments are closed. Comments show the author, timestamp, and a small image of their avatar.

**View Ticket Stats**

Al users are able to view a statistics page that displays interactive charts, rendered by Charts.js, detailing the status of all Bugs/Features, as well as the number of Bugs/Features that have been updated each day, that week, and that month.

### Features Left to Implement

**Delete Account**

Users should be able to delete their account at any time, however time constraints meant that this feature couldn't be implemented at this time.

**User Badges**

When users reached certain milestones in their participation with the site (such as their first comment, first Feature Request, etc.) they were to have badges appear in their user profiles representing each one. Again, time constraints make this an item that will need to be left until a future release.

##### back to [top](#table-of-contents)

---

## Technologies Used

- [Microsoft Visual Studio Code](https://code.visualstudio.com/) - Open source IDE from Microsoft that was used to code this project.
- [GitHub](https://github.com/) - Remote repository for all project code with git version control.
- [TinyPNG](https://tinypng.com/) - Compresses images used on the site to keep file sizes to a minimum.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - The fundamental code structure for all webpages.
- [Sass CSS](https://sass-lang.com/) - CSS extension language used to build the CSS for this project and the recommended method to alter the default CSS of the Materialize framework.
- [jQuery 3.4.1](https://code.jquery.com/jquery/) - Javascript framework used to implement custom code and initialize Materialize functions.
- [Materialize 1.0.0](https://materializecss.com/) - Primary visual framework for this project, based on Google's Material Design.
- [Stripe](https://stripe.com/docs/api?lang=python) - The Stripe API allows individuals and businesses to make and receive payments over the Internet.
- [Chart.js](https://www.chartjs.org/) - Simple, clean and engaging HTML5 based JavaScript charts. Chart.js is an easy way to include animated, interactive graphs on your website for free.

### Back-End Technologies

- **Heroku**
    - [Heroku](https://www.heroku.com) - Hosts the deployed version of this project.
- **Python**    
    - [Python 3.7.3](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language and is the language used for all backend functions of this project.
    - [Django 1.11.22](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Amazon Web Services**
    - [Amazon S3](https://aws.amazon.com/s3/) - Amazon Simple Storage Service is a service offered by Amazon Web Services that provides object storage through a web service interface. Amazon S3 uses the same scalable storage infrastructure that Amazon.com uses to run its global e-commerce network.

##### back to [top](#table-of-contents)

---

## Testing

TBD

### Automated Testing

TBD
### Manual Testing

TBD

### Validators

**HTML**

Passing the HTML from all templates and base into the [W3C Markup Validator](https://validator.w3.org/) generates numerous errors, but these are expected as the validator is unable to understand the Django templating that builds most aspects of the page. For the HTML that does not involve this templating, no errors have been found.

**CSS**

The CSS for the project has been generated by the Sass CSS extension language. Passing the generated CSS through the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) shows that there are no errors. A number of warnings are flagged, but these relate to MS-Grid vendor prefixes and can be safely ignored.

**Javascript**

All Javascript was passes throught the [Esprima Syntax Validator](http://esprima.org/demo/validate.html) and was found to be syntactically valid.

**Python**

All Python code was passed through the [PEP8 Online](http://pep8online.com/) validator and is fully PEP8 compliant.

### Compatibility

The project was tested to ensure full usability across the following browsers and their mobile equivalents (where applicable):

- Chrome *v.74*
- Edge *v.18*
- Firefox *v.67*
- Safari *v.12*
- Opera *v.56*
- Internet Explorer *v.11*

##### back to [top](#table-of-contents)

---

## Deployment

TBD

### Local Deployment

TBD

### Remote Deployment

TBD

##### back to [top](#table-of-contents)

---

## Credits

### Content

TBD

### Media

TBD

### Code

TBD 

### Acknowledgements

- My mentor, [Mark Railton](https://github.com/railto), for all of his input on this project.
- [Tim Nelson](https://github.com/TravelTimN), for the immeasurable patience and help that he always provides, and for being the sounding board for my ideas and solutions to issues. HDL.

##### back to [top](#table-of-contents)