# Testing Page for Dhanvi Fashion

### An E-commerce site for online shopping.

[Main README.md file](README.md)

[View live site here](https://dhanvi-fashion-ms4.herokuapp.com/)

## Testing

* [Code Testing](#code-testing)
    * [Markup](#markup)
    * [CSS](#css)
    * [Javascript](#javascript)
    * [Python](#python)

* [User Stories Testing](#user-stories-testing)

* [Manual Testing](#manual-testing)

    * [Elements on every page](#elements-on-every-page)
       * [Navigation Bar](#navigation-bar)
       * [Footer](#footer)
       * [Toasts](#toasts)
    * [Elements on separate page](#elements-on-separate-page)
       * [Home Page](#home-page)
       * [Product Page](#product-page)
       * [Product Detail Page](#post-ad-page)
       * [Product Management Page](#product-management-page)
       * [Profile Page](#profile-page)
       * [Shopping Bag Page](#shopping-bag-page)
       * [Checkout Page](#checkout-page)
       * [Checkout Success Page](#checkout-success-page)
       * [Order History](#order-history)
       * [Blog Page](#blog-page)
       * [Blog Detail Page](#blog-detail-page)
       * [Blog Management Page](#blog-management-page)
       * [Back to Top](#back-to-top)
       * [Contact Page](#contact-page)
       * [Delete Modal](#delete-modal)

* [Responsiveness](#responsiveness)

* [Browser Compatibility](#browser-compatibility)

* [Lighthouse](#lighthouse)

***

## **Code Testing**
  [W3C Markup Validation Service](https://validator.w3.org/)

### **Markup**
 [W3C Markup Validation Service](https://validator.w3.org/)

 * W3C markup validation service is used for the testing of the **HTML** of all  HTML pages and 

    The  result was this.

    ![image]()

### **CSS**
[W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

* W3 CSS validation service is used for the testing of the **CSS** of the project and .

    The result can be seen here.

    ![image]()

### **Javascript**
[JSHint](https://jshint.com/)

* JSHint, a JavaScript code quality tool was used to test the **JavaScript** codes of all 2 js pages from the project.

    The result can be seen here.
* Stripe_elements.js

* ![script.js]() 

* Countryfield.js

* ![image]()

These warnings can be overlooked.

### **Python**
[Python Validator](http://pep8online.com/)

 The result can be seen here.

 ![python]()

 Further testing was done by typing this code in command line

     python3 -m flake8

And the result found was this

![image]()

[Go to Top](#testing)
***

## **User Stories Testing**

Testing User stories from UX part of [README.md](README.md) 

**Viewing and Navigation** 

1. Immediately get an overview of what products this site offers.
    * This site has a main nav for the desktop which is collapsible in mobile view. This main nav has links to all the product categories. 
    * The products are sorted in many ways. For example, price, rating, and category.
    * Other than this products are displayed based on deals, new arrivals, and clearance.
    * So, it is very easy to find what products are available if the site.

2. View a list of products.
    * When the user clicks on a certain category from the main nav, the product page opens with that category. 
    * It also shows the number of products available on the left-hand side of the page.

3. View details about a specific product.
    * When a user chooses a product and clicks on the image of the product on the product page, It opens a product detail page. 
    * The product detail page has a zoom the image of the product, while click to download the image of the product, Name, description, category, and rating is also there.
    * A quantity selector box is also given so that user can select more than one product if he/she wants.
    * Size box will appear only for clothes and dresses.

4. See the total of all items in my shopping bag.
    * The Shopping bag page shows every detail related to the price of the product. 
    * It shows bag total, delivery cost (if Bag total is less than the threshold amount, in this project it is €50), and Grand Total.
    * One bag icon is given on the top right corner of the navbar, which shows the bag total, which makes it very convenient for the user to see the total irrespective of on what page he/she is.

5. See the rating of every product.
    * Rating of every product is given ate the product page, where every product is displayed. 
    * Rating is shown in number out of 5. For example 4.5/5.
    * Product rating is also given on the product detail page, where an individual product is displayed.

6. View the blog about the site.
    * This site has a very nice blog icon, which can be visit the blog page.
    * This blog section opens every blog in a detailed view when clicked. 
    * The detailed Card displays the Full blog content, as well as the name of the author and the date and time of its posting.
    * So that the user will get to know if it is a recent or old post.

7. Add comments on the blog.
    * The blog detail page has a comments section also, which displays the comments added by the user.
    * One form is given, which takes the User name, email, and comment about the blog.
    * The comments added by the user do not reflect on the page immediately. Admin has to approve it for display.
    * This feature is added for the safety from spam messages.

 **Registration and User accounts**

8. Easily register for an account.
    * Registering for the account is very easy. The register link is given in the dropdown of my account in the top navbar.
    * After clicking the register, the Register page opens, which asks the user to enter the Username, Email, and password.
    * After filling out the form the user gets an email on his/her email account to verify the email account.
    * After Verification Login page opens. And after filling that the user can log in easily.
  
9. Easily Login or Logout.
    * The login link is given at my profile dropdown in the top navbar.
    * The user is asked to enter a username and password, which he has used while registering.
    * After the correct entry, the user can easily log in.
    * If the user is not registered already then he is asked to sign up first before login.
    * When the user is logged in, the logout options display in my account dropdown. Which asks about the confirmation if the user wants to sign out.
    * When the user clicks the sign-out button, he can easily sign out from the site.

10. Easily recover my password in case I forget it.
    * A Very nice password reset feature is added from the Django allauth.
    * Which opens when the user clicks forgot password on the login page.
    * Forgot password page asks for the email address and sends a password recovery email to the user account.
