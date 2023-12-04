#!/usr/bin/python3
"""
 class that defines all common
 attributes/methods
 for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """ starting of the class """

    def __init__(self):
        """ Public instance attributes """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """ updates the public instance
        attribute updated_at """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """  returns a dictionary """
        copy_dict = self.__dict__.copy()
        copy_dict["__class__"] = self.__class__.__name__
        copy_dict["created_at"] = self.created_at.isoformat()
        copy_dict["updated_at"] = self.updated_at.isoformat()
        return copy_dict

    def __str__(self):
        """ print formated string """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
