#!/usr/bin/python3
"""Module for the entry point of the command interpreter."""

import json
import cmd
from models.base_model import BaseModel
from models import storage
import re



class HBNBCommand(cmd.Cmd):

    """Class for the command interpreter."""

    prompt = "(hbnb) "
