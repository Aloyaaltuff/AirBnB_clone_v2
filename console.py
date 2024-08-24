#!/usr/bin/python3
""" the entry point propgramm of the command interpreter"""
import cmd
import re
import json


class HBNBCommand(cmd.Cmd):
    """Defines a class which is the entry point command interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, line):
        """quit the interpreter"""
        return True

    def do_EOF(self, line):
        """exits the interpreter cleanly"""
        print()
        return True

    def help_quit(self):
        """help message for quit"""
        print("Quit command to exit the program\n")
        return

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass
    def enter(self):
        """Do nothing when enter is entered"""
        pass

    def default(self, line):
        """Handle unrecognized commands"""
        print(f"*** Unknown syntax: {line}")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
