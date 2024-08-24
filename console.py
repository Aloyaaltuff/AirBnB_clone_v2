#!/usr/bin/python3
""" the entry point propgramm of the command interpreter"""
import cmd
import re
import json
from models.base_model import BaseModel
from models.engine.file_storage import storage

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
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not line:
            print("** class name missing **")
            return
        if line not in storage.classes():
            print("** class doesn't exist **")
            return

        new_instance = storage.classes()[line]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        if line:
            if line not in storage.classes():
                print("** class doesn't exist **")
                return
            instances = [str(obj) for key, obj in storage.all().items() if key.startswith(line)]
        else:
            instances = [str(obj) for key, obj in storage.all().items()]

        print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = line.split(' ', 3)
        if len(args) < 1:
            print("** class name missing **")
            return
        if args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        value = args[3].strip('"')
        instance = storage.all()[key]

        # Update attribute based on type
        if attribute_name in ['name', 'email']:  # Assuming these are strings
            setattr(instance, attribute_name, value)
        elif attribute_name in ['age']:  # Assuming these are integers
            setattr(instance, attribute_name, int(value))
        elif attribute_name in ['height']:  # Assuming these are floats
            setattr(instance, attribute_name, float(value))
        else:
            print("** attribute type not supported **")
            return

        instance.save()

    def help_create(self):
        """Help message for create"""
        print("Creates a new instance of BaseModel, saves it, and prints the id\n")

    def help_show(self):
        """Help message for show"""
        print("Prints the string representation of an instance based on the class name and id\n")

    def help_destroy(self):
        """Help message for destroy"""
        print("Deletes an instance based on the class name and id\n")

    def help_all(self):
        """Help message for all"""
        print("Prints all string representation of all instances based or not on the class name\n")

    def help_update(self):
        """Help message for update"""
        print("Updates an instance based on the class name and id by adding or updating attribute\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
