# Dhanvi-Fashion - E-Commerce Web App.

### Code Institute - Final Milestone Project (4) - Full Stack Frameworks With Django.

The live website can be found [here](https://dhanvi-fashion-ms4.herokuapp.com/)

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

### **Surface**
#### **Color**

The colors used for this project are kept very minimum so that the strong tonal varitaions provides a good contrast. The main color used for the project is Mustard yellow(#E1AD01), which goes very well with these theme and it is a good contrast with the other two colors Black(#000000) and White(#ffffff).

The colors used are:

![image]()

Mustard Yellow color is used for delivery Banner and hovers over across page. The Text color used are mainly black and changes to mustard yellow when hovered over.
The placeholder text for the form have the color Cadet Blue(#AAB7C4) and the rating text of the product description is Bootstrap text-muted class Slate Gray(#6C757d).

#### **Core**

The Core of the project is kept, Black and White. The navbar is White, which has text written in black that changes to mustard yellow when hovered over. 
The Footer is Black with texts of white color. The social media links and Contact link changes to mustard yellow color when hovered over.
The pages of the project are kept white to make a good contrast with the products images.

#### **Buttons**

The Buttons are kept black with text white, which changes to mustard yellow when hovered over.
The edit and delete links have given a consistent color with the intuitive suggestions about their functions.
The edit is kept Dodger Blue(#007BFF) and Delete link is Amaranth(#DC3545)
The back to top button is Mustard yellow(#E1AD01)

*  ![#000000](https://via.placeholder.com/15/00000/000000?text=+) `#000000` (Black)
*  ![#007BFF](https://via.placeholder.com/15/007bff/000000?text=+) `#007bff` (Dodger Blue)
*  ![#DC3545](https://via.placeholder.com/15/dc3545/000000?text=+) `#DC3645`(Amaranth)
*  ![#E1AD01](https://via.placeholder.com/15/e1ad01/000000?text=+) `#E1AD01`(Mustard Yellow)

#### **Typography**

[Montserrat](https://fonts.google.com/specimen/Montserrat?query=mon)

Google font **Montserrat** with a fallback of **sans serif** is selected for the entire project.

#### **Images**

Images used are taken from [Unsplash](https://unsplash.com/) and [Google](https://www.google.com). 

[Go back to Top](#table-of-content)
***

## **Database Model**

SQLite3 database is used during the development of the project. For deployment of the project PostgreSQL databse is used. 
Using Django Allauth and it's default django.contrib.auth.models, provided me with the the User model used in the profile app.

The structure of the Product and Checkout apps are guided by the Code Institute's walkthrough project, **Boutique Ado**.

### **Profile App**
**User Profile Model**

| Name   | Database Key     | Field Type  |  Validation  |
| ------------- |:----------:| :------:|  :-----:  |
| User | user    | OneToOneField 'User' |  on_delete=models.CASCADE  |
| Phone Number | default_phone_number    | models.CharField | max_length=20, null=True, blank=True   |
| Street Address 1 | default_street_address1    | models.CharField |  max_length=80, null=True, blank=True  |
| Street Address 2 | default_street_address2    | models.CharField |  max_length=80, null=True, blank=True  |
| Town or City |  default_town_or_city    | models.CharField |  max_length=40, null=True, blank=True  |
| County | default_county    | models.CharField |  max_length=80, null=True, blank=True  |
| Postcode | default_postcode    | models.CharField |  max_length=20, null=True, blank=True  |
| Country |  default_country   | models.CharField |  blank_label='Country', null=True, blank=True  |

### **Product App**
**Category Model**

| Name   | Database Key     | Field Type  |  Validation  |
| ------------- |:----------:| :------:|  :-----:  |
| Name | name    | moels.CharField |  max_length=254  |
| Friendly Name | friendly_name    | models.CharField | max_length=254, null=True, blank=True   |

**Product Model**

| Name   | Database Key     | Field Type  |  Validation  |
| ------------- |:----------:| :------:|  :-----:  |
|  Category | category    | models.ForeignKey |  'Category', null=True, blank=True, on_delete=models.SET_NULL  |
| Sku | sku    | models.CharField | max_length=254, null=True, blank=True   |
| Name |  name    | models.CharField |  max_length=254  |
| Description |  description    | models.TextField |    |
| Price | price    | models.DecimalField |  max_digits=6, decimal_places=2  |
| Rating | rating    | models.DecimalField | max_digits=6, decimal_places=2, null=True, blank=True  |
| Image URL | image_url    | models.URLField |  max_length=1024, null=True, blank=True  |
| Image | image   | models.ImageField | null=True, blank=True  |

### **Checkout App**
**Order Model**

| Name   | Database Key     | Field Type  |  Validation  |
| ------------- |:----------:| :------:|  :-----:  |
| Order Number | order_number    | models.CharField |  max_length=32, null=False, editable=False  |
| User Profile | user_profile    | models.ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'   |
| Full Name | full_name   | models.CharField |  max_length=50, null=False, blank=False  |
| Email | email   | models.EmailField |  max_length=254, null=False, blank=False  |
| Phone Number |  phone_number    | models.CharField |  max_length=20, null=False, blank=False  |
| Country | country    | CountryField | blank_label='Country *', null=False, blank=False  |
| Postcode | postcode    | models.CharField |  max_length=20, null=True, blank=True  |
| Town or City |  town_or_city   | models.CharField |  max_length=40, null=False, blank=False  |
| Street Address 1 | street_address1    | models.CharField |  max_length=80, null=False, blank=False  |
| Street Address 2 | street_address2    | models.CharField |  max_length=80, null=True, blank=True  |
| County | county    | models.CharField |  max_length=80, null=True, blank=True  |
| Date | date    | models.DateTimeField |  auto_now_add=True  |
| Delivery Cost |  delivery_cost   | models.DecimalField |  max_digits=6, decimal_places=2, null=False, default=0  |
| Order Total |  order_total   | models.DecimalField |  max_digits=10, decimal_places=2, null=False, default=0  |
| Grand Total |  grand_total   | models.DecimalField |  max_digits=10, decimal_places=2, null=False, default=0  |
| Original Bag |  original_bag   | models.TextField |  null=False, blank=False, default=''  |
| Stripe Payment Intent ID |  stripe_pid   | models.CharField |  max_length=254, null=False, blank=False, default=''  |


**Order Line Item Model**

| Name   | Database Key     | Field Type  |  Validation  |
| ------------- |:----------:| :------:|  :-----:  |
| Order  | order    | models.ForeignKey |  Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'  |
| Product |product    | models.ForeignKey | Product, null=False, blank=False, on_delete=models.CASCADE   |
| Quantity | quantity   | models.IntegerField |  null=False, blank=False, default=0  |
| Line Item Total | lineitem_total   | models.DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False  |

### **Blog App**
**BlogPost Model**

| Name   | Database Key     | Field Type  |  Validation  |
| ------------- |:----------:| :------:|  :-----:  |
| Title | title    | models.CharField |  max_length=254, unique=True  |
| Date Created | created_on   | models.DateTimeField | auto_now_add=True   |
| Date Updated | updated_on    | models.DateTimeField |  auto_now=true  |
| Slug | slug    | models.SlugField |  max_length=254, unique=True  |
| Author |  author    | models.ForeignKey |  User, on_delete=models.CASCADE, related_name='blog_posts'  |
| Body | body    | models.TextField |   |
| Image | image    | models.ImageField |  default='', blank=true  |
| Image URL |  image_url   | models.URLField |  max_length=1024, default='', blank=True  |
| Status |  status   | models.IntegerField |  choices=STATUS, default=0  |


**Comment Model**

| Name   | Database Key     | Field Type  |  Validation  |
| ------------- |:----------:| :------:|  :-----:  |
| Post | post    | models.ForeignKey |  BlogPost, on_delete=models.CASCADE, related_names='comments'  |
| Name | name   | models.CharField |  max_length=80  |
| Email | email    | models.EmailField |    |
| Body | body    | models.TextField |    |
| Date Created |  created_on    | models.DateTimeField |  auto_now_add=True  |
| Active | active    | models.BooleanField |  default=False  |

[Go back to Top](#table-of-content)
***

## **Features**

### **Features Used**
**Navigation Bar:**

All pages of the project have a fixed top navigation bar which has a Site logo, *Search*, and 3 icons, One is for *Blog* second is for *my Account* and another is *bag* icon.
The search box can be used to search by keywords of the product name or description. The My account icon is a dropdown list, which shows login and register links for first-time users. If the user has registered and logged in then it will show a link to *my profile* and *logout* page. If the user is a superuser/admin then links to *Product management* and *Blog Management* are also visible. The bag icon takes us to the *shopping Bag* page after clicking on it and it also displays the total amount of the products already in the bag. This section is fully responsive and in the mobile view the search box is replaced by only the icon of the search and the search box appears after clicking on it. 
The navigation bar consists of one **Main Nav** also, which is a list of all the categories of the products used in the project. These lists have links based on the price and rating of the product also. This section changes to a collapsible hamburger menu on the left side of the screen for the smaller screen view. 
There is one delivery banner also which displays the message about the free delivery threshold for the project.

**Footer:**

The Footer is a *Sticky Footer*, which is visible on every page of the project. The footer has 3 sections, one is the copyright information about the site owner, second is the font awesome icons of the social media *Facebook*, *Twitter*, and *Instagram*. The links take the user to the respective sites after clicking on them.
The third section is a *Contact Us* link, which opens the contact form after clicking.

**Index page:**

The Index page or landing page is divided into 3 sections. The first section has a Carousal with 3 images. Each image has a cover text which has some information and a button to take the user to the relative page.
The second section has 2 cards, one is an image of a **Jewellery Collection** and a button to take the user to the **Jewellery shopping** Product page and the second is an image of the **Beauty Accessories** and a button to go to The **Beauty Accessories** Product page.
The last section has a **Special Offer** section which displays the images of special offer category products and a *See All* link to take the user to the special offer section. The product images are also clickable and take the user to the product description page.

**Products page:**

Products can be viewed in many different ways. The product is displayed in the form of a card, which has a *product image*, *product price*, *product category*(which is also a clickable badge to take the user to that category), *product rating*, and *edit and delete* button. 
Product Image takes the user to the Product detail page when clicked. The  edit and delete button are only visible to the superuser.
This page also has a sort button that displays the products in that specific sort order (Price(low to high), Price(high to low), Rating(low to high), Rating(high to low), Name(A-Z), Name(Z-A), Category(A-Z) and Category(Z-A)).

**Product Detail page:**

The Product Detail page has an image of the product on the left side, which is clickable and doenload the product image and zoom the image. The left side of the page has *product name*, *product price*, *product rating*, *category*, *edit /delete* button(for superuser), *product description*, *quantity selector*, and 2 buttons, one for *keep shopping* and another for *Add to bag*.

**Product Management Page:**

The Product management page opens after clicking the product management link in my profile dropdown in the navbar. This link is only visible to the admin. This page can be used to add or edit new products. The add products page opens with a form to select the category in the dropdown menu, Place to write 'sku', 'name', 'description' 'price', 'rating', 'image URL', and a button to select the image. Two buttons are given, one to cancel the action and another to add the product. When the admin selects the edit action the page will open with advance populated with the product information and detail. Product image is also visible to take a better decision. This image section is made with Django widgets for a better user experience. Two buttons are given to edit or cancel the action. After adding or editing the product, the product detail page opens. 

**Profile page:**

The profile page can be accessed by the **My Account** link in the navbar. This page is divided into 2 sections. One is having an information form, which is empty in the beginning and gets filled automatically after the user enters its information on the checkout page. There is an *Update Information* button in the end, for the user to change any detail if he wants. 
The second section is the *Order History* list, which displays the orders placed by The user. It shows *Order Number*, *Date*, *Item Name*, and *Order Total*.
The Order Number shows only 5 digits in the form but when clicked it opens the page of **order history**.

**Order history:**

This page can be accessed by the profile page and by clicking on the order number. The order history page shows *order info* (order number and order details), *order details* (item name and price), *Delivering To* (Full name, Address1, Address2, County, Town or city, Postal Code, Country Phone Number), *Billing Info* (order total, delivery and Grand Total). There is a *Back to Profile* button at the end which takes back to the profile page.

**Shopping Page:**

The shopping page can be viewed by clicking the bag icon on the navbar. The shopping page shows the details of the products added by the user in his/her bag. It shows *product info* (product image, product name, and sku), *Price*, *Quantity selector box*, and *Subtotal*. There are 2 buttons given below the quantity selector, one is the *update* button, to increase or decrease the quantity of the product and another is the *remove* button, to remove the item from the bag.
This page shows *Bag total*, *Delivery cost*, and *Grand Total* also. If the discount threshold is not reached then one message will show about how much to spend more to reach that threshold. There are 2 buttons given at the bottom, one for keep shopping and another for secure checkout.

This page looks different in mobile view, where *Bag total*, *Delivery cost*, and *Grand Total* are at the top of the page. And one *back to top* button is also added in case the user has multiple products and the page becomes very long. 

**Checkout Page:**

The checkout page can be viewed by clicking the secure checkout button on the shopping bag page. The checkout page is divided into two sections horizontally. First one is having the details of the customer 'full name', 'email address', 'phone number', 'address', 'county', 'postal code', and a dropdown selection for the country. One more box is given to enter the card number. If the user is not logged in then one information will display to tell the user to Create a account or log in to save this information and if the user is not registered then he/she can use create account link to register. Two buttons are given at the bottom, one to *adjust bag* and another to *complete order*.
Below the buttons, the total purchase amount is shown in red color.
The second section of the checkout page shows the *order summary* of the order placed by the user. It displays product image, product name, subtotal, delivery, grand total.

**Checkout Success Page:**

This page can be viewed by clicking the *Complete Order* button on the checkout page, This page is the same as the *order history* page. 

**Blog Page:**

The blog is created to view by every user. It can be accessed by any user by clicking the blog link on the home page or blog icon in the top nav. The blog page shows rows of all the blogs. Every row has one blog image, Name of the blog, Name of the person who added the blog, Date and time of blog added, And first 150 characters of the blog details. There is a *read more* button to open the blog on the different page for a full view. The image of the blog will also open the blog in the detail view. There is one edit and delete link, only visible to the superuser. In mobile view, the blog image will take the full width and the blog name and other details will come below the blog.

**Blog Deatils Page:**

The blog details page can be opened by clicking the blog name or image or read more button on the blog page. This page contains a big blog image and full blog detail. There is a **back to blog** button given at the end of the blog detail, which takes back to the main blog page and final section comments form available user can review about the blog.

**Blog Comments section:**

One comment section is added to the blog detail page after the back to blog button. In this comment section, anybody can Enter their name and email id and Add their comments and submit through the submit button. The comments need approval by the Admin. This feature is added for safety reasons to avoid any spam or unacceptable comments. After the approval, the comment is visible with the person's name, date, and time of the comment.

**Blog Management Page:**

The blog management page is visible only to the admin by clicking the blog management link in my profile dropdown in the navbar. The blog management page is made to add new blogs or edit existing blogs easily and without opening the Django admin page. This page has 'Blog name', 'Slug', 'Author', 'body', a button to select the image, or a space to add the image URL. Status can be selected between *draft* or *publish*. Two buttons are given, one to cancel the action and another to add the blog. after adding blog detail page opens. When the admin selects the edit action for the blog, the page opens with populated with the blog information in advance. The blog image is also visible. The blog image section is made using the widgets of Django which gives a very good user experience. The admin will have an option to cancel the action or update the blog.

**Back to top button:**

A back to top button is visible on product and bag pages when the user scrolls past 200 pixels.
