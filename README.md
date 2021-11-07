# AirBnB Clone Project
This is the first part of building our first web application: the AirBnB clone. This project was built with OOP in Python and using the "cmd" module, to create the console that will be the command interpreter.

## Description
In this first step, the objects will be created, updated, destroyed and read through the console (command interpreter) with the help of a JSON file (the objects will be stored).

## How to start it
You have to give permissions to file ```console.py``` and then execute with ```./console.py```

## How to use it


| Command | Description |
| :---       |     :---         |
| ```EOF```, ```quit``` or ```Ctrl + c``` | Allows you to exit the program      |
| ```create <class>```     | Creates a new instance of ```class```, saves it (to the JSON file) and prints the ```id```       |
| ```show <class> <id>``` | Prints the string representation of an instance based on the class```class``` name and ```id``` |
| ```destroy <class> <id>``` or ```<class name>.destroy(<id>)``` | Deletes an instance based on the ```class``` name and ```id``` (save the change into the JSON file) |
| ```all <class>``` , ```<class name>.all()```  or ```all``` |  Prints all string representation of all instances based or not on the ```class``` name |
| ```update <class name> <id> <attribute name> "<attribute value>"``` | Updates an instance based on the ```class``` name and ```id``` by adding or updating attribute (save the change into the JSON file) |
| ```<class name>.count()``` | Update your command interpreter (```console.py```) to retrieve the number of instances of a class |
| ```<class name>.show(<id>)``` | Update your command interpreter (```console.py```) to retrieve an instance based on its ```id``` |


## EXAMPLES
