#!/usr/bin/python3
"""Module that defines all common attributes/methods for other classes """

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        'Quit command to exit the program'
        quit(*parse(arg))

    def do_EOF(self, arg):
        'EOF command to exit the program'
        return True

    def emptyline(self):
        pass

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
