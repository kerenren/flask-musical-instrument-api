 Create a musical instruments API
Background:
As a part of the venue showcasing many performers, you've been assigned to write an API to manage the instruments that will be used in the venue.


Please read carefully the assignment before starting to write any code.


This assignment refactors the Musical instruments assignment from Python intro week, and it relies also on the ninja part of it, where the band class acts as the data layer.


Tasks:

First we will build a basic flask API that will replace the previous command line API. 
Then we will add to it advanced features.




Mandatory Tasks

Get all instruments (e.g. guitar, piano, violin).


Get all instruments by a specific musician’s email.


Get an instrument by type, manufacturer, model, musician’s email.


add a new instrument to a musician (send json with the required parameters).


Upload link to youtube video (share link) of an instrument.


Add a new musician (send json with the required parameters).


Delete an instrument by musician_email, name, manufacturer, model.



Musician’s fields:
* first name
* last name
* email
* instruments
* created_at
* last_accessed






Basic API:

When building the Basic API, approach it like you did in the previous exercises. 

For creating the connections between musicians and instruments you can choose between the following 2 options regarding the data structure (band.py):


  Data structure: 
  Option 1: have a dictionary for the instruments 
  (key: instrument_id, value: instrument instance), 
  and a separate dictionary for the users
  (key: user_id, value: user instance).
  
  Option 2: have one dictionary for both users and instruments
  E.g. user dictionary with an entry for instruments for each user.

You may choose whichever option you prefer but first, in a .txt file within the project, write Pros & Cons for each option and why you made your decision.
  

- The data within any dictionary will contain class instances.

- Now that you’ve set up your data structures, start writing routes for serving the POST requests required by the Basic Tasks section above. Use your dictionary for saving the data of the POST requests. Send several POST requests to your routes in order to populate your dictionary with data. Then, in the next step, we can implement GET requests to retrieve that data. You can use POSTMAN or any other way you prefer to test your POST requests. Remember to validate the incoming data and to handle exceptions. 
   
- With data in your dictionary, you can now write routes for the GET requests described in the Basic Tasks above. After writing the routes, you can use POSTMAN or any other way you prefer to test your GET requests. Remember to validate the incoming request and to handle exceptions. 
   


Ninja:

Now that your Basic API is finished, you should add advanced features. Write routes for searching for an instrument by its name.
Remember to validate and to handle exceptions.

Search for an instrument by name.
Return a JSON results object representing a list of instruments that contain the search term given and a timestamp representing how long the search took (in milliseconds).
User Query params for this task.


Instead of using type,manufacturer and model for distinguishing between musical instruments, generate a unique id string using:
https://pynative.com/python-generate-random-string/
And refactor your code accordingly.


In band.py add a function for persisting data into a json file, and another function for loading data from the json file and populate the data into the dictionary/ies.
The load data function will be invoked on flask server startup.
Implement a function with @app.before_first_request decorator
 

Additional Tips:
Don’t forget to add validations when necessary.
Don’t forget to handle exceptions.
Every object should also have a property indicating its creation time, and a property indicating its last accessed time.
Create a requirements.txt file which contains all the installed python packages
https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e
Think carefully regarding the return objects of each route.
Don’t rush through this; please be thoughtful and thorough in your development; this is not a race!


Testing API with postman:

**post musician json**

{
   "musician" : "Musician",
    "first_name" : "John",
    "last_name":"Doe",
    "email":"doe@mail.com"
}

**post instrument json**
{
   "type" : "StringInstrument",
    "manufacture":"Wittner",
    "model":"Pro",
    "musician_email":"doe@mail.com"
}
{
    "type" : "electric piano",
    "manufacture":"Fender",
    "model":"Rhodes",
    "musician_email":"doe@mail.com"
}
{
    "type" : "electric piano",
    "manufacture":"Yamaha",
    "model":"S90",
    "musician_email":"doe@mail.com"
}

**post delete json**
{
    "action": "RemoveInstrument",
    "name" : "StringInstrument",
    "manufacture":"Wittner",
    "model":"Pro",
    "musician_email":"doe@mail.com"
}
{
    "action": "RemoveInstrument",
    "name" : "electric piano",
    "manufacture":"Fender",
    "model":"Rhodes",
    "musician_email":"doe@mail.com"
}
{
    "action": "RemoveInstrument",
    "name" : "electric piano",
    "manufacture":"Yamaha",
    "model":"S90",
    "musician_email":"doe@mail.com"
}