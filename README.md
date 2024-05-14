# Little Rascal Recipes Blog

![AmIResponsive Image](./README_Images/site_images/amiresponsive.webp)

## Live website

Link to live website: [Little Rascal Recipes](https://little-rascal-recipes-7007a778b4a8.herokuapp.com/)

## Purpose of the project

This is my project 4 for Code Institute as part of their Full stack development diploma. The project is a full-stack website built using the Django framework.

Little Rascal Recipes is a blog where users can look for a delicious and nutritious meal or snack to prepare for their children aged 12 months and over.

This website initially provides the user with a homepage enticing them to ‘Explore popular Recipes’. Once clicked the page drops down showcasing popular recipes for their child, this is where the user will be prompted to sign up. Once a user signs up and logs in they will have access to a share page where they can view shared and share their own cookbooks for kids, and have the opportunity to access and partake in the comments section on each recipe. 

## Table of contents

- [1. User Expeience](#user-experience-ux)
- [2. Agile Methodology](#agile-methodology)
- [3. The Scope](#the-scope)
- [4. Design](#design)
- [5. Features](#features)
- [6. Django Admin](#django-admin)
- [7. Technologies Used](#technologies-used)
- [8. Testing](#testing)
- [9. Deployment](#deployment)
- [10. Credits](#credits)
- [11. Acknowledgements](#acknowledgements)


## User Experience (UX)

### User Stories

* As a website user, I can:

<br>

1. Navigate around the site and easily view the content.

2. View a few selected recipes and choose accordingly.

3. Click on the post to read the recipe details.

4. See the About page which provides information on the blog creator.

5. Register for an account to access the services offered to members.

<br>

* As a logged in website user, I can:

<br>

1. Comment on recipes and give my opinion.

2. Delete any of my previous comments.

3. Log out from the website.

<br>

* As a website superuser, I can:

<br>

1. Create and publish a new recipe.

2. Create draft recipe posts that can be reviewed and finalised/ published later.

3. Create a new user.

4. Delete user.

5. Approve, reject or delete user's comments.

### MoSCoW

![MoSCoW screenshot](./README_Images/site_images/MoSCoW.webp)

This project used the "MoSCoW" method to classify its features and requirements according to their importance towards a minimum viable product (MVP). "MoSCoW" stands for "Must have, Should have, Could have and Won't have," with each classification aiding in the prioritisation of features. This method makes sure that essential components are tackled in priority order.



## Agile Methodology

* All functionality and development of this project were managed using GitHub Projects. This can be found here [Github Projects](https://github.com/users/DeveloperDunne/projects/4)

## The Scope

### Main Site Goals

* To provide users with a good experience when using the website.
* To provide users with a visually pleasing website that is intuitive to use and easy to navigate.
* To provide a website with a clear purpose.
* To provide role-based permissions that allow users to interact with the website.
* The ability to find relevant information on the business and its services.
* The ability to update and delete comments if desired.
* The ability to interact with content by commenting.

### Target audience

This blog is for users who are interested in healthy and delicious food for their children.

## Design

### Wireframes
Balsamiq was used to design the blog's look.

### Colour Theme
![Colour Theme](./README_Images/design_images/theme.webp)

The colour theme above was used throughout the project to ensure consistency and appeal to the user.

### Fonts
Fonts used were 'Lato', 'Raleway' and 'Alice'. All were sourced from [Google Fonts](https://fonts.google.com/).

## Features

### Navigation Bar

A responsive navigation bar is situated at the top of the page. When on a mobile the bar condenses into a burger icon which will enable a dropdown menu, however on a desktop all pages are displayed along the bar. What is shown in the navigation bar depends on whether the user is logged in or not.

#### Not logged in:
![Navigation Bar - Not Logged in](./README_Images/site_images/navbar-notlogged.webp)

When not logged in you will be able to see the following pages: Home, About, Contact, Register and Sign In.

#### Logged in:
![Navigation Bar - Logged in](./README_Images/site_images/navbar-logged.webp)

When logged in the Register and Sign-in page disappears and instead you will see a Share page and Logout option.

#### Logged in message:
![Logged in message](./README_Images/site_images/logged-in.webp)

When you log in a message will appear at the top of the page to confirm that you have logged in successfully.

### Home Page
![Home Page](./README_Images/site_images/home-page.webp)

Upon arrival to the website, you will be directed straight to the home page. Here you will be shown a welcome message and an enticing 'Explore our recipes' option, drawing you into what is to come.

#### Home Page - Popular Recipes
![Popular recipes](./README_Images/site_images/popular-recipes.webp)

If you click on the 'Explore' option you will be directed down the page to see some of the blog's recipe posts. The user can click on a post to view the ingredients and methods on how to make the meal. If there are more than can fit on one page you can click next to view more.

### Recipe Details
![Recipe Details](./README_Images/site_images/recipe.webp)

If the user likes the sound of one of the recipes they can click on the post title. Once clicked they will be directed to a page displaying the ingredients and the method on how to prepare the meal.

#### Recipe Details - Comments Logged in:
![Comments - Logged in](./README_Images/site_images/comment-logged.webp)

If the user has signed up and logged in they will be able to interact and to comment on the recipe themselves.

#### Recipe - Comments logged out:
![Comments - logged out](./README_Images/site_images/comment-not-logged.webp)
If the user has not signed up then they will be asked to log in if they wish to comment. The user can see the comments and how many of them even if they are not logged in.

### About Page
![About](./README_Images/site_images/about-page.webp)

Here the user can read about the purpose of the blog and the creator.

### Contact Page
![Contact](./README_Images/site_images/contact.webp)

The contact page consists of a form that the user can fill out and submit if they have any questions.

### Sign Up Page
![Sign Up](./README_Images/site_images/signup.webp)

This page is a form where the user can sign up to reap the benefits of being a logged in user.

### Sign In Page
![Sign in](./README_Images/site_images/signin.webp)

This page is where the user can sign in so that they can make comments and have access to the share page.

### Sign Out Page
![Sign Out](./README_Images/site_images/signout.webp)

This is the sign out page where users can log out. They will be asked to confirm before the sign out is complete.

### Sign Out Confirmation
![Sign out confirmation](./README_Images/site_images/sigout-confirmed.webp)

Once signed out the user will be redirected to the home page, they will be shown a message which states that they have logged out.

### Share Page

#### Share Page - Share Cookbook
![Share Cookbooks](./README_Images/site_images/share-form.webp)

The share page was designed for logged in users to share their favourite children's cookbooks. Once the form is filled out it will be sent for approval to the superuser.

#### Share Page - View Shared Cookbooks
![Shared Books](./README_Images/site_images/share-shared.webp)

Below the form, the logged in users will be able to view the approved shared books.

### Footer
![Footer](./README_Images/site_images/footer.webp)

The footer provides information on where to follow the creator on social links. Each link will open in a new tab.

### Future Features

Features I would have liked to implement but did not get time to would be a favourites function and maybe a like and dislike button on the comments.

I would also liked to have styled the pages a bit more, however I just ran out of time.

## Django Admin

### Admin Home Page
![Admin home page](./README_Images/admin_images/admin-page.webp)

This is the homepage of the Django Admin panel. Here the superuser can access posts, create, edit, update and delete for each of the below pages showing full CRUD  functionality.


### Admin Recipes
![Admin Recipes](./README_Images/admin_images/admin-recipes.webp)



### Admin Contact
![Admin Contact](./README_Images/admin_images/admin-contact.webp)

### Admin Comments
![Admin Comments](./README_Images/admin_images/admin-comments.webp)

### Admin Share
![Admin Share](./README_Images/admin_images/admin-share.webp)

## Technologies Used

### Languages Used

* HTML 5
* CSS 3
* JavaScript
* Django
* Python

### Frameworks & Libraries Used

* Bootstrap: This was used to style the website, and add responsiveness and interactivity.

* Git: Was used for version control to commit to Git and push to GitHub.

* GitHub: Is is used to store the project's code after being pushed from Git

* Heroku: Was used to deploy the live project.

* VSCode: This was used to create and edit the website.

* Fontawesome: To add icons to the website.

* Google Fonts: To add the fonts that could be used for the project.

* Coolors: To build the colour palette of the project.

* Balsamiq: To build the wireframes for the project.

### Databases

* PostgreSQL from Code Institute was used as the PostgreSQL database for this project.


### Django packages Installed

* Gunicorn: As the server for Heroku.

* Cloudinary: This was used to host the static files and media.

* Dj_database_url: To parse the database URL from the environment variables in Heroku.

* Psycopg2-binary: As an adaptor for Python and PostgreSQL databases.

* Summernote: As a text editor for the admin panel.

* Allauth: For authentication, registration, and account management.

* Crispy Forms: To style the forms.


## Testing

Detailed testing documentation can be found here[ TESTING.MD](./TESTING.md)

## Deployment

All code for this project was written using the IDE Visual Studio code (VS Code). Github was used for version control and the application was deployed via Heroku.

 ### Heroku Deployment

* This site was deployed by completing the following steps:

1. Log in to Heroku or create an account.

2. On the main page click Create New App.

3. Select your region.

4. Click on the Create App button.

5. The next page is the project’s Deploy Tab, click the Settings Tab.

6. Next, scroll down to the Build pack section click ‘Add Build pack’ select Python and click Save Changes.

7. Add Node.JS after adding Python. 
(Please be aware: Python must be above Node.JS in that order).

8. Go to the Deploy tab.

9. Select Github as your deployment method.

10. Connect to GitHub.

11. Search your repository name and connect.

12. Click either Enable Automatic Deploys for automatic deployment when you push updates to GitHub or manual to do this manually.

### Cloning:

1.  Go to the repository on GitHub.

2.  Click on the Code button and copy the https URL under Clone.

3.  Open a terminal.

4. Go to the folder you want to store the cloned repository.

5. In the terminal type git clone and paste the URL of the cloned repository after it then press Enter.

6. The site will then be cloned to that directory.

### Fork this repository:

- Go to the GitHub repository.
- Click on the Fork button in the upper right-hand corner.

## Credits

### Code
The CI walkthrough (Django Blog) was leaned on and relied upon heavily in this project due to time restraints and there are still some remnants of legacy code within. As I was really pushed for time to complete the project I used the CI code and initial styling as a base. 

I did however change the design to make it my own, created and implemented my own app (Share). This app was created so that users once signed up and logged in could share cookbooks that they liked and view other shared cookbooks. This custom app has front-end CRUD functionality.

### Recipes
All recipes were taken from the BBC Goodfood website and can be found here [BBC Good  Food](https://www.bbcgoodfood.com/recipes/collection/toddler-recipes).

### Images
The recipe images were taken directly from where the recipes were sourced [BBC Good  Food](https://www.bbcgoodfood.com/recipes/collection/toddler-recipes).

The hero image was taken from [Unsplash](www.unsplash.com).

## Acknowledgements
Thank you to my mentor, the Slack community and tutors for all their help throughout this project. Also thank you to my friends and family for help with testing the project.