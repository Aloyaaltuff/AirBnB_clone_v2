#!/usr/bin/python3
""" the entry point propgramm of the command interpreter"""
import cmd
import re
import json
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Defines a class which is the entry point command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit the interpreter"""
        return True

    def do_EOF(self, line):
        """exits the interpreter cleanly"""
        print()
        pass

    def help_quit(self):
        """help message for quit"""
        print("Quit is a command to exit the program\n")
        return

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def help_quit(self):
        """help message for quit"""
        print("Quit command to exit the program\n")
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
