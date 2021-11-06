#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """

import cmd
import json
import sys
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Class that contains the entry point of the command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        ' Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id'
        if arg == "":
            print("** class name missing **")
        elif arg == "BaseModel":
            p = BaseModel()
            p.save()
            print(p.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        'Prints the string representation of an instance based on the class name and id'
        arguments = arg.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arguments[0] == "BaseModel" and len(arguments) == 1:
            print("** instance id missing **")
        else:
            if arguments[0] == "BaseModel" and len(arguments[1]) != 0:
                all_objects = storage.all()
                switch = 0
                for obj_id in all_objects.keys():
                    obj = all_objects[obj_id]
                    if obj.id == arguments[1]:
                        print(obj)
                        switch = 1
                if switch == 0:
                    print("** no in stance found **")

    def do_destroy(self, arg):
        'Deletes an instance based on the class name and id (save the change into the JSON file)'
        arguments = arg.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arguments[0] == "BaseModel" and len(arguments) == 1:
            print("** instance id missing **")
        else:
            if arguments[0] == "BaseModel" and len(arguments[1]) != 0:
                all_objects = storage.all()
                try:
                    del all_objects["{}.{}".format(arguments[0], arguments[1])]
                    storage.save()
                except KeyError as e:
                    print("** no in stance found **")

    def do_all(self, arg):
        'Prints all string representation of all instances based or not on the class name'
        objs_list = []
        arguments = arg.split(" ")
        if arguments[0] == "":
            all_objects = storage.all()
            for obj_id in all_objects.keys():
                obj = all_objects[obj_id]
                objs_list.append(str(obj))
            print(objs_list)
        if arguments[0] == "BaseModel":
            all_objects = storage.all()
            for obj_id in all_objects.keys():
                obj = all_objects[obj_id]
                if obj.__class__.__name__ == "BaseModel":
                    objs_list.append(str(obj))
            print(objs_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        'Updates an instance based on the class name and id by adding or updating attribute'
        arguments = arg.split(" ")
        if arguments[0] == "":
            print("** class name missing **")
        elif arguments[0] != "BaseModel":
            print("** class doesn't exist **")
        elif arguments[0] == "BaseModel" and len(arguments) == 1:
            print("** instance id missing **")
        elif len(arguments) == 3:
            print("** value missing **")
        elif len(arguments) == 2:
            print("** attribute name missing **")
        else:
            if arguments[0] == "BaseModel" and len(arguments[1]) != 0:
                all_objects = storage.all()
                switch = 0
                for obj_id in all_objects.keys():
                    obj = all_objects[obj_id]
                    if obj.id == arguments[1]:
                        string_cast = json.loads(arguments[3])
                        setattr(obj, arguments[2], string_cast)
                        storage.save()
                        switch = 1
                        break
                if switch == 0:
                    print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
