# Dhanvi-Fashion - E-Commerce Web App.

### Code Institute - Final Milestone Project (4) - Full Stack Frameworks With Django.

The live website can be found [here]()

![image]())

This is my fourth and final milestone project for Code institute’s full-stack web developer diploma. This project is a **Django web application** made with the use of **HTML**, **CSS**, **JavaScript**, and **Python** and utilizing a relational database.
**Stripe** is also used for payment systems.
This project is plugged into a **PostgreSQL** database, with **SQlite3** used in the development and was deployed using **Heroku**. **AWS S3 bucket** is used to store static and media files. The **Bootstrap** framework and grid system were used for styling across the site.
***

## **Table of Content**

* [Overview](#overview)

* [User Experience](#user-experience)

   * [User Goals](#user-goals)
   * [User Stories](#user-stories)

* [Planes of Development](#planes-of-development)
    * [Strategy](#strategy)
    * [Scope](#scope)
    * [Structure](#structure)
    * [Skeleton](#skeleton)
        * [Wireframe](#wireframe)
        * [Sitemap](#sitemap)
    * [Surface](#surface)
        * [Color](#color)
        * [Core](#core)
        * [Buttons](#buttons)
        * [Typography](#typography)
        * [Images](#images)

* [Database model](#database-model)

* [Features](#features)
    * [Features Used](#features-used)
    * [Features to be implementd in Future](#features-to-be-implemented-in-future)

* [Technologies used](#technologies-used)
    * [Languages Used](#languages-used)
    * [Libraries, Frameworks and Editors](#libraries-frameworks-and-editors)
    * [Extensions and Kits](#extensions-and-kits) 
    * [Databases](#databases)
    * [Tools](#tools)

* [Bugs](#bugs)
    * [Project barriers and solutions](#project-barriers-and-solutions)
    * [Known Issues](#known-issues)

* [Testing](#testing)

* [Deployment](#deployment)
    * [Local Deployment](#local-deployment)
    * [Deployment to Heroku](#deployment-to-heroku)

* [Credits](#credits)
    * [Code](#code)
    * [Media](#media)
    * [Acknowledgments](#acknowledgments)
***

## **Overview**

- Dhanvi Fashion is an online e-commerce store, which offers a collection of Clothes, Bags, Jewellery and Beauty Accessories. 
- Users can create their account, saving their details for faster checkout for future purchases, but are not limited to that,and can make a purchase as a guest if wanted.
- The registered user can edit their details and access their shopping history.
- Blogs are presented for good reads and site owners can be contacted easily.

[Go Back to Top](#table-of-content)
***

## **User Experience**

### **User Goals**

1.	In the current pandemic situation, Users may want to do purchasing from the safe environment from their home.
2.	User-friendly website, where users doesn’t have to be very technically educated to do the purchasing.
3. User can easily purchase their items.

### **User Stories**

 | User Story ID   | As a/an     | I want to be able to  |  So that I can  |
| ------------- |:----------:| :------:|  :-----:  |
|    |       |    **Viewing and Navigation**         |    |
| 1 | Shopper    | View a list of Products |  Select some to Purchase  |
| 2 | Shopper    | View the details of specific products | Identify the larger image, price, detailed description and rating of the product. |
| 3 | Shopper    | View the total of item in my shopping bag | Avoid spending too much time |
| 4 | Shopper    | Easily identify deals, special offers and clearance items | Take advantage to special saving on product I'd have like to purchase |
| 5 | Site User  | View the blog about the site | Learn more about the Dhanvi Fashion |
| 6 | Site User  | Add comments on the blog | Express my view about the blog post |
|     |     |  **Registration and User accounts**         |      |
| 7 | Site User  | Easily register for an account | Have a personal account to come back and view my profile |
| 8 | Site User  | Easily Login or Logout | Access my personal account information |
| 9 | Site User  | Easily recover my password in case I forget it | Recover access to my account |
| 10 | Site User | Receive a confirmation email after registering an account | Know that my account registration was successful |
| 11 | Site User | Have a personalised user profile | View my order history, see my order confirmation and save my payment information |
|     |      |   **Sorting and Searching**         |      |
| 12 | Shopper   | Select which category of product to show | Easily find a product within the category that I am interested |
| 13 | Shopper   | Sort products by different parameters | Easily find the products with the best rating or lowest price |
| 14 | Shopper   | Search for the product by name or description | Easily find the specific product that I am looking to buy |
| 15 | Shopper   | Easily see what I have searched for and the number of results | Identify misspelling in my search string and quickly overview the search result |
|      |      |    **Purchasing and Checkout**         |      |
| 16 | Shopper   | Easily select the number of product when adding it | Ensure I do not accidently select the wrong product or quantity |
| 17 | Shopper   | Easily view all items in my shopping bag | Identifying the total cost and overview the items to be ordered |
| 18 | Shopper   | Change the quantity of a product in my shopping bag | Easily make changes to my shopping bag |
| 19 | Shopper   | Easily enter my payment information | Checkout easily and quickly |
| 20 | Shopper   | Personal and payment information is safe and secure | Feel confident when providing the information needed to make a purchase |
| 21 | Shopper   | View an order confirmation after checkout | Verify that I haven't made any mistakes |
| 22 | Shopper   | Receive a confirmation email after registering an account | Keep the confirmation of what I've purchased for my records |
|       |      |   **Admin and Store Management**         |       |
| 23 | Owner     | Add a product to the website | Add new items to my store |
| 24 | Owner     | Edit / Update a product | Change the product prices, descriptions, images and other product crietria |
| 25 | Owner     | Delete a product | Remove items that are no longer for the sale |
| 26 | Owner     | Add, Update and Delete blog posts | Write and maintain a blog about product related topics |

[Go back to Top](#table-of-content)
  ***

## **Planes of Development**
### **Strategy**

The aim of making this site is to make a website that focus mainly on Fashion products. 
There are plenty of sites right now but very few focus on fashion clothes and  beauty accessories. We are going through a pandemic and lockdown situation worldwide. We are bound to stay inside our home and left with very few activities, in that online shopping is a good hobby to pursue.

 ### **Scope**

 1. I want to make a website that is accessible to everyone. People can search and browse all the products without being registered so that there will be no hesitation in going through the site. Anyone can do the purchasing by adding his/her details and doing a valid payment. 
 
 2. The detail of every product opens on a new page with a product rating with it, so it is easier to decide which product to buy. 
 
 3. Products can be sorted in various ways like the price- low to high or high to low, category, ratings, etc. users can make their profile so that when they return, they will have their details already filled.

 4. Users can go through the blog page and write a comment if they want. And they can contact the site owner with the contact form provided.

### **Structure**

- This website will be a multi-page site, where pages are connected through Navigation Bar or Python. 
- The navigation bar will have links for the Home page, my account(login, register), bag, and Blog. The navigation links will change and show the logout and My profile Once the user is logged in. 
- It will show a product management link for the admin. The navigation bar will be collapsible for Mobile view. 
- There will be a footer, which will show the contact details of the admin. It will be sticky and always remain at the end of the page. 2 forms will be there, one for Login and the other for Registration. 
- One contact form will also be there for the users to contact the admin. There will be pages for products, product details, shopping bag, checkout, checkout success, blog, blog details, Users will have my profile page after they register with the site. Admin will do the product management, he/she can add edit, and delete any product. Admin will post the blog which can be commented on by any user.
- SQLite3 is used in the development and the PostgreSQL database is used in production mode. All the static and media files will be stored in the AWS s3 bucket it will be deployed by using Heroku.

### **Skeleton**
#### **Wireframe**

The wireframes for this project can be seen here.
<details>
<summary>Wireframe</summary>
<br>

1. [Home Page]()

2. [Products Page]()

3. [Product Details Page]()

4. [Category Page]()

5. [My Profile Page]()

6. [Login Page]()

7. [Register Page]()

8. [Bag Page]()

9. [Checkout Page]()

10. [Contact page]()

11. [Blog Page]()

12. [Blog Details Page]()

13. [Product Management Page]()

</details>

#### **Sitemap**
A Sitemap is prepared for this site to understand the navigation of the pages.

The Sitemap can be seen here. [Sitemap]()

