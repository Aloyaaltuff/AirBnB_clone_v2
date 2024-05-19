#!/usr/bin/python3
"""Defines unittests
for console testing :Test_prompting, Test_help, Test_exit"""
import unittest
import sys
import os
from models.engine.file_storage import FileStorage
from models import storage
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch


class Test_prompt(unittest.TestCase):
    """testing prompting of the HBNB command interpreter."""

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as arg:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", arg.getvalue().strip())

    def test_prompt_str(self):
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)


class Test_help(unittest.TestCase):
    """testing help messages of the HBNB command interpreter."""

    def test_help_create(self):
        help = ("Usage: create <class> \n  "
                "Create a new class instance and print its id.")
        with patch("sys.stdout", new=StringIO()) as arg:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help, arg.getvalue().strip())

    def test_help_EOF(self):
        help = "EOF signal to exit the program."
        with patch("sys.stdout", new=StringIO()) as arg:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help, arg.getvalue().strip())

    def test_help_quit(self):
        help = "Quit command to exit the program."
        with patch("sys.stdout", new=StringIO()) as arg:
            self.assertEqual(help, arg.getvalue().strip())
            self.assertFalse(HBNBCommand().onecmd("help quit"))


if __name__ == "__main__":
    unittest.main()
