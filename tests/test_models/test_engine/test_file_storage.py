#!/usr/bin/python3
""" Unittest for File Storage """
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import unittest
import os
import json


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up for test cases."""
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects

    def tearDown(self):
        """Tear down after test cases."""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test the all method."""
        storage = FileStorage()
        self.assertEqual(storage.all(), self.objects)

    def test_new(self):
        """Test the new method."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all())

    def test_save_reload(self):
        """Test the save and reload methods."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        storage.save()

        # Create a new storage instance to test reload
        new_storage = FileStorage()
        new_storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)

        self.assertIn(key, new_storage.all())
        self.assertIsInstance(new_storage.all()[key], BaseModel)


if __name__ == '__main__':
    unittest.main()
