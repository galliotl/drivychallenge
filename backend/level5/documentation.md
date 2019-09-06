# Deezer technical test

Disclaimer: this is one of my few experiences with python. Therefore, the type of error raised, detailed in the behaviour section, might not be the best one for each case.

## Structure 

```
+-- data/
|   +-- test/
|       +-- wrong_date.json
|       +-- wrong_date_format.json
|   +-- expected_output.json
|   +-- input.json
|   +-- output.json
|
+-- models/
|   +-- options.py
|   +-- car.py
|   +-- rental.py
|
+-- data_from_db.py
+-- checkout.py
+-- main.py
|
+-- test_main.py
|
```

#### Models

In the models folder you can find the 3 classes we use to represent data fetched from the database. We create objects for each rows in the file so that we can add methods and alter some fields. 

As an exemple in rental instead of storing the dates, we compute the duration and those are the one we store since they are the one we need.

It also allows us to verify the input and raise some exceptions if needed.

#### Data

Data that we use. The given input and the excpected output, plus some test cases for automated unittests.

## Classes

Those stored in models are the simplest classes possible. A cleaned version of the one we get from the input file. They are pretty self-explainatory and only store the main fields of each object plus verifies the input.

#### Checkout

Checkout is our class that given a rental object, a car, and a list of named options can compute price, actions, and edit a formatted result that is modelled after the expected output file. 

We use a separated class so that the models classes don't have to mess with each other's instances and stay simple. Each class is simple and has an as simple role.

#### DataFromDB

Given an input param, is going to look for the file and extract the desired parameters, shape them into more usable data structures like hashmaps. It instanciates all the correspondant objects from the model classes.

## Behaviour

Since the exception behaviour wasn't specified in the specifications, here's a list of how it's going to react in our case.

Case | Behaviour
--- | --- 
Normal | the output.json file is equal to the expected_output.json file
End date is before start date | The rental class throws an assertion error
Date format is wrong | The rental class throws a Value error
Car created with a negative price | The car class raises an Assertion error
Path to input is wrong | The DataFromDB class raises an IOError
Input doesn't contain cars or rental | The DataFromDB class raises a ValueError
Car creation raises an exception | The DataFromDB class passes and does not add it into the cars hashmap
Rental creation raises an exception | The DataFromDB class passes and does not add it into the rentals hashmap
Option creation raises an exception | The DataFromDB class passes and does not add it into the rentals hashmap
Rental created with a car that doesn't exist | Rental isn't added to the rentals list
Option created with a rental that doesn't exist | Options isn't added to the rentals' option list
Checkout creation raises an exception | The main function won't add it to the main rental's list

## Unit test

a main_test file is used to verify all the behaviours specified before. Run with:

```python
python -m unittest test_main
```