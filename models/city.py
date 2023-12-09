#!/usr/bin/python3
"""inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """ handel state id and ame attributes """
    state_id = ""
    name = ""
