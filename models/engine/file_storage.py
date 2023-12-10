#!/usr/bin/python3
"""
Define the class that manage storing data
"""
import json


class FileStorage:
    """
    A class that serializes instances to
    a JSON file and deserializes JSON file to instances
    """

    __file_path = 'file.json'
    __objects = {}    # key:value <==> obj_class_name.obj_id = obj_name

    def all(self):
        """" returns the dict '__objects' """
        return self.__objects

    def new(self, obj):
        """" add " obj_class_name.obj_id" = obj " to the dict '__objects'. """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file. """
        data = {}  # k:v <==> obj_class_name.obj_id = obj.to_dict()
        for key, obj in self.__objects.items():
            data[key] = obj.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(data, file, indent=2)

    def reload(self):
        """ deserializes the JSON file to __objects. """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity  import Amenity 
        from models.review import Review

        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

                for key, value in data.items():
                    # get class_name as a string
                    class_name = key.split('.')[0]  # BaseModel (str)
                    if class_name:
                        # Evaluate the class name and assign it to class_obj
                        class_obj = eval(class_name)
                        if class_obj:
                            ''' create a new obj_instance from
                            the class "class_obj" & initialize its attributes
                            with the dict "value"'''
                            obj_instance = class_obj(**value)
                            # add the new obj_instance to the __objects dict
                            self.__objects[key] = obj_instance

        except FileNotFoundError:
            pass
