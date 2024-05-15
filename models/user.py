#!/usr/bin/python3
"""This module is for a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for user objects mangment"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
