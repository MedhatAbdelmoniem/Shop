Auth0 Domain Name = fsndmedhat.eu.auth0.com

Auth0 Client ID = RhbVQ3WiBA5AmLYs7I5ipUft5pgGcFxl

https://udacityshopproject.herokuapp.com/

seller token = eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ3OTlmNjM1YjkwMDA3MTE5YmEyNyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA2Mjg1MjcsImV4cCI6MTYzMDcxNDkyNywiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpwcm9kdWN0IiwiZ2V0OnByb2R1Y3QiLCJwYXRjaDpwcm9kdWN0IiwicG9zdDpwcm9kdWN0Il19.Arv4n-HS3JQI1Ygn8859kx4MVdWmcMo-QpQOQRxg-vk_e0hC-H1NcTQTQ-HaLeFBq-D1rHDBXBlHAF-qaCWlyFEvmCKK8dkulydQFxu-Gz8NwthlOQqMzhOpdeY7USNgA9Ve0rIS5XLu3IbXrEF3y-RwbocixV-ZPiDPTcsppDJtleOi8tdxUT25oLS_k8BC3lPvVnxyAS0cvXcVYx7EVGu4LQI_4T9HJcFTyh3-DhMDROmoHLxLpEsdX0m9reKF1TiUtnwzaBrIXwcPfD2L7pLqvMF5dUl4WD419EmxzyDvnR3sOR85dJQ_Gq1bTduG52CFaBv78wRKVwRCgyTXtQ

buyer token = eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVqOFhsTFRTaWlJQW1VSzlkZFdBaCJ9.eyJpc3MiOiJodHRwczovL2ZzbmRtZWRoYXQuZXUuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYxMmQ5M2ExZDdlZTU0MDA3MmE1MzZmMyIsImF1ZCI6InNob3AiLCJpYXQiOjE2MzA2Mjk5NTAsImV4cCI6MTYzMDcxNjM1MCwiYXpwIjoiUmhiVlEzV2lCQTVBbUxZczdJNWlwVWZ0NXBnR2NGeGwiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpwcm9kdWN0Il19.bPuQ497wzcKCqfn7Am1GiZtom0tPtpa2rsE4HqmgmVEYOrxhGjnrT9Si-LxmOoxcRsleKGnO7vKbSnSwRS91Vvo1MWZfYkeBK8tM8KObD_oTseoL6LyllKZgNCeVxAGD1dJF1gamu_dbY6TQ80axFXjvqq86lHrKdVNfyZNS6D88lrBmvCcgXtFKJn_1SdpdDjn2ZCeDzJcLpfHn_645zNO40vUyqeY-YovHqQu51goT8fqTKQE0tT_Fa1nsMzi_6wPT63W81lFMAACB7-82_HoFlQhdlP9kvQiU2GE5EO6SnbDDIfLflPESjNYNJJCHvQcy1CvpJS-VXE0uSditRA


tests included in ShopTest.postman_collection.json

-------------------------------------------------

This project was created for udacity project

-------------------------------------------------

to start first run this code
pip install requirements.txt
in this direction shop\backend
in the terminal



-------------------------------------------------

The website that hosting the app is https://udacityshopproject.herokuapp.com/

where the main page does nothing but print hello

https://udacityshopproject.herokuapp.com/home

this returns all the sellers info that that works with the front end project

"sellers": [
        {
            "description": "newDescription",
            "id": 3,
            "image": "new.link",
            "name": "newSeller",
            "number": 222230,
            "product": "newLaptop",
            "type": "Tech"
        }
           ]

this does not require any permission of the user
============================================================================
to create account using auth0 simply open index.html and press sign-in to create account

if you want a specific seller info you get it by

https://udacityshopproject.herokuapp.com/home/<id>

but it requires to have a buyers account

using postman with a valid token and good id gives sellers info


{
    "success": "true"
}


=============================================================================

also
https://udacityshopproject.herokuapp.com/edit/<id>
and
https://udacityshopproject.herokuapp.com/delete/<id>

the same they needs a valid token and good id


------------------------------------------------------------------------------

if failed it can be from different reasons, the return may give you a hint:

422 Unprocessable Entity

might mean wrong key names that does not match
=========================
{
    "code": "unauthorized",
    "description": "Permission not found."
}

means that the user does not have permission to do this task

============================

{
    "error": 404,
    "message": "resource not found",
    "success": false
}

might mean wrong address or the id does not exist

-------------------------------------------------------------------------------

local files is used for testing the api using test_app.py

--------------------------------------------------------------------------------

there are two roles buyer and seller

their permissions is as follow:

buyer=> get:product

means he can only see the specific product


seller=> get:product, delete:product, patch:product, post:product

means he can see the product, edit it , delete it or create a new product