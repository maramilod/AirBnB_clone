#!/usr/bin/python3
import json
from os.path import exists
import sys
from models.user import User


class FileStorage:
    __file_path = 'file.json'
    __objects = {}    # key/value ==> obj_class_name.obj_id = obj_name

    def all(self):
        """" returns the dict '__objects' """
        return self.__objects

    def new(self, obj):
        """" add " obj_class_name.obj_id" = obj " to the dict '__objects' """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    # def save(self):
    #     data = {}  # k/v ==> obj_class_name.obj_id = {'__class__': 'BaseModel',     'updated_at': '..', 'id': '..', 'created_at': '..'}
    #     for key, obj in self.__objects.items():
    #         data[key] = obj.to_dict()

    #     with open(self.__file_path, 'w') as file:
    #         json.dump(data, file)
    
    def save(self):
        data = {}
        # Load existing data if file exists
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

        for key, obj in self.__objects.items():
            class_name, obj_id = key.split('.')
            # Store class name as part of the dictionary key
            data[key] = {"class_name": class_name, "obj_dict": obj.to_dict()}

        with open(self.__file_path, 'w') as file:
            json.dump(data, file, indent= 2)

    # def reload(self):
    #     try:
    #         with open(self.__file_path, 'r') as file:
    #             data = json.load(file)
    #             for key, value in data.items():
    #                 # get class_name as a string
    #                 class_name, obj_id = key.split('.')
    #                 # looking from the class of obj in the global scope table with the string name "class_name"
    #                 class_obj = globals()[class_name]
    #                 # create a new obj from the class "class_obj" with attributes values in "value"
    #                 obj_instance = class_obj(**value)
    #                 # add the object to the __objects dictionary
    #                 self.__objects[key] = obj_instance
    #     except FileNotFoundError:
    #         pass


    def reload(self):
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)

                for key, value in data.items():
                    class_name = value.get("class_name")   # BaseModel (str)     
                    if class_name:
                        obj_id = key.split('.')[1]
                        # globals() did not work as expected, idk why :(
                        # class_obj = globals().get(class_name)
                        class_obj = BaseModel  # Use the actual class name
                        if class_obj:
                            obj_instance = class_obj(**value["obj_dict"])
                            self.__objects[key] = obj_instance
                    #     else:
                    #         print(f"Class {class_name} not found")
                    # else:
                    #     print("Class name not specified in loaded data")

        except FileNotFoundError:
            pass
