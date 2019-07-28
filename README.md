# Project by Ronit Raj
# Tummy-Truck 
A food ordering website with some basic features as of now.

## Demo : 
https://drive.google.com/drive/folders/1f2QjL_rMtXg7T3E9nsu5fzlh_KFkQDEX?usp=sharing
 
 ### How to run the project?
 1. Clone and unzip the repo
 2. Install all dependencies using the requirements file
 3. Open command prompt and cd into the above directory. 
 4. Run py manage.py runserver
 5. Open http://localhost:8000 in a web browser.
 
 ## Features of website
 -  Login usinng a username password or signup for it. Users can also login through facebook.
 -  A 5 stars rating system for each restaurant. Ratings provided by the user after every order.
 -  Once a user is logged in he can view his past orders.
 -  The restaurant menu has navigation buttons to jump to specific cuisines and also has the list of 5 bestselling dishes.
 -  Fully responsive frontend for all devices.
 -  All the data is automatically fed to the frontend by the database and nothing is stored in the html files.
 -  All the forms i.e the input values (example ratings and quantity of each fooditem) have been tested to make sure no out of bound value causes errors. 
 ## Overview of database columns
  - Restaurants stores the name and details of resaturants.
  - Food stores the name and details of each food item present in all the restaurants.
  - PastOrders stores all the orders placed and has details regarding all the orders.
  - FoodOrders is not of use for the user.
  
  Note: Whenever a new 'Place'(city) is added make sure to add an image with the same name to the 'static/store/images/' directory

 

