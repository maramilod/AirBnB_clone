#!/usr/bin/python3
""" class inherits from BaseModel """
from models.base_model import BaseModel


class User(BaseModel):
    """ class that have user info attributes """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
