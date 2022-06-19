# Sprints' Online Store Backend API (Django):

## Introduction ##

This is a REST API for an E-commerce website that interacts with any Frontend.

---
## Setup ##
### Database config ###
The API backend connects with sqlite database, but any other database can be used instead in case of production.
### Database Schema ###
***Schema.png*** is located in the root folder.
### Start ###
Clone the repo:  ***git clone*** **https://github.com/Ahmed-Abdelgawad-Dev/Sprints_Online_Store.git**

Install the required packages:
```shell
pip install -r requirements.txt
```
Apply migrations:
```shell
python manage.py migrate
```
Create an admin user:
```shell
python manage.py createsuperuser
```
Run the server:
```shell
python manage.py runserver
```
### Environment variables ###

**.env is required  and must be inside .git ignore for security.**
Here python dotenv package is used, feel free to use any other solution, also put any other credentials here like api secrets key ...etc.
Example for the required `.env` could be as below and the values can be accessed :.
```dotenv
SECRET_KEY=django-insecure-9kr=#(!7bp2n65^e4i!5vm6e_3ux3qd7nb0jc2j@i7jyhw)6qa
DATABASE=....etc
```
### Release port 8000 if needed: Unix based OS ###
`sudo lsof -t -i tcp:8000 | xargs kill -9
`
---
## Endpoints ##

```http request
        'users/'
        POST: 'login/' 
        GET:  'get_user/'
        GET:  'get_users/'
        PUT:  'update_user/'
        POST: 'register_user/'

        'products/' 
        GET:  ''                          |     get all products
        GET:  '/{id}'                     |     get a product

        'orders/'
        GET: ''                           | get orders of user  
        POST:  'add_order/'               | add items to order or make an order and put items inside
        GET:  'my_orders/'                | get orders of a user
        POST: '{order_id}/Delivered/'     | change the order status to delivered after delivery
        GET:  '{order_id}/'               | get order by order id
        POST: '{order_id}/paid/'          | change the payment status to paid
