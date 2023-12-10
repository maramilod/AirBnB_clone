#!/usr/bin/python3
"""
 class that defines all common
 attributes/methods
 for other classes
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ starting of the class """

    def __init__(self, *args, **kwargs):
        """ Public instance attributes """
        if kwargs:
            formated = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, formated))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            # add this new instance to the FileStorage __objects
            models.storage.new(self)

    def save(self):
        """ updates the public instance
        attribute updated_at """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        copy_dict = self.__dict__.copy()
        # Convert created_at and updated_at to string
        for key, value in copy_dict.items():
            if key in ['created_at', 'updated_at'] and isinstance(
                    value, datetime):
                copy_dict[key] = value.isoformat()

        # Add the class name to the dictionary
        copy_dict["__class__"] = self.__class__.__name__

        return copy_dict

    def __str__(self):
        """ print formated string """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
