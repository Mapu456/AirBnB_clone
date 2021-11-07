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


## Examples

### ```EOF```, ```quit``` or ```Ctrl + c``` command

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) help quit
Quit command to exit the program

(hbnb) 
(hbnb) 
(hbnb) quit 
guillaume@ubuntu:~/AirBnB$ 
```

### ```create``` command

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```

### ```show``` command

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

### ```destroy``` command

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
```

or

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.destroy("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
```

### ```all``` command

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) all MyModel
** class doesn't exist **
(hbnb)
(hbnb) all
["[Amenity] (96c742c6-48ea-4c37-b3e2-d60913253db9) {'id': '96c742c6-48ea-4c37-b3e2-d60913253db9', 'created_at': datetime.datetime(2021, 11, 6, 12, 31, 48, 485365), 'updated_at': datetime.datetime(2021, 11, 6, 12, 31, 48, 485393)}"]
```

or

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb) 
```

### ```update``` command

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb)
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb)
```

### ```count``` command

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.count()
2
(hbnb)
```

### ```show``` command

```
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel My_First_Model
** no instance found **
(hbnb)
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

or

```
guillaume@ubuntu:~/AirBnB$ ./console.py
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb) User.show("Bar")
** no instance found **
(hbnb)
```
