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


class FileStorageTest(unittest.TestCase):
    """Unittests for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_wrong_args(self):
        '''all the methods with wrong args'''
        with self.assertRaises(TypeError):
            FileStorage(None)
        with self.assertRaises(TypeError):
            storage.save(None)
        with self.assertRaises(TypeError):
            storage.all("what")
        with self.assertRaises(AttributeError):
            storage.new("is")
        with self.assertRaises(TypeError):
            storage.save("you'r")
        with self.assertRaises(TypeError):
            storage.reload("Name")

    def test_attributes(self):
        """Test attributes"""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))
        self.assertFalse(hasattr(storage, '__file_path'))
        self.assertFalse(hasattr(storage, '__objects'))
        self.assertEqual(type(storage), FileStorage)

    def test_all_empty(self):
        """Test all empty"""
        new_fs = FileStorage()
        FileStorage._FileStorage__objects = {}
        new_fs.reload()
        self.assertEqual(new_fs.all(), {})
        self.assertEqual(dict, type(new_fs.all()))

    def test_new_object(self):
        """Test new object"""
        a_fs = FileStorage()
        FileStorage._FileStorage__objects = {}
        new_user = User()
        new_BM = BaseModel()
        a_fs.new(new_user)
        a_fs.new(new_BM)
        expected = {f"User.{new_user.id}": new_user,
                    f"BaseModel.{new_BM.id}": new_BM}
        self.assertEqual(a_fs.all(), expected)

    def test_save_object(self):
        """Test save objects"""
        new_fs = FileStorage()
        new_user = User()
        new_fs.new(new_user)
        new_BM = BaseModel()
        new_fs.save()
        U_key = f"User.{new_user.id}"
        BM_key = f"BaseModel.{new_BM.id}"
        with open("file.json", "r") as file:
            file_content = json.load(file)
            self.assertTrue(file_content.get(U_key))
            self.assertTrue(file_content.get(BM_key))

    def test_reload_file_not_exist(self):
        """Test reload file not exists"""
        new_fs = FileStorage()
        new_fs.reload()
        self.assertEqual(new_fs.all(), {})

    def test_reload_file_exists(self):
        """Test reload file exists"""
        storage.reload()
        content = storage.all()
        self.assertNotEqual(content, {})

    def test_all_non_empty(self):
        """Test all non-empty"""
        new_fs = FileStorage()
        new_user = User()
        new_base_model = BaseModel()
        new_fs.new(new_user)
        new_fs.new(new_base_model)
        self.assertNotEqual(new_fs.all(), {})

    def test_reload_invalid_json(self):
        """Test reload with invalid JSON"""
        with open("file.json", "w") as file:
            file.write("Invalid JSON")
        new_fs = FileStorage()
        new_fs.reload()
        self.assertEqual(new_fs.all(), {})

    def test_save_reload_multiple_objects(self):
        """Test saving and reloading multiple objects"""
        new_fs = FileStorage()
        new_user1 = User()
        new_user2 = User()
        new_fs.new(new_user1)
        new_fs.new(new_user2)
        new_fs.save()
        new_fs.reload()
        self.assertIn(f"User.{new_user1.id}", new_fs.all())
        self.assertIn(f"User.{new_user2.id}", new_fs.all())

    def test_new_empty_dict(self):
        """Test new method with an empty dictionary"""
        new_fs = FileStorage()
        new_fs.new({})
        self.assertEqual(new_fs.all(), {})

    def test_save_reload_multiple_models(self):
        """Test saving and reloading multiple model instances"""
        new_fs = FileStorage()
        new_state = State()
        new_city = City()
        new_fs.new(new_state)
        new_fs.new(new_city)
        new_fs.save()
        new_fs.reload()
        self.assertIn(f"State.{new_state.id}", new_fs.all())
        self.assertIn(f"City.{new_city.id}", new_fs.all())

    def test_new_invalid_dict(self):
        """Test new method with an invalid dictionary"""
        new_fs = FileStorage()
        with self.assertRaises(AttributeError):
            new_fs.new("invalid")

    def test_reload_invalid_file(self):
        """Test reload with an invalid file"""
        with open("file.json", "w") as file:
            file.write("Invalid JSON")
        new_fs = FileStorage()
        new_fs.reload()
        self.assertEqual(new_fs.all(), {})

    def test_save_reload_mixed_models(self):
        """Test saving and reloading instances of different models"""
        new_fs = FileStorage()
        new_user = User()
        new_place = Place()
        new_fs.new(new_user)
        new_fs.new(new_place)
        new_fs.save()
        new_fs.reload()
        self.assertIn(f"User.{new_user.id}", new_fs.all())
        self.assertIn(f"Place.{new_place.id}", new_fs.all())


if __name__ == "__main__":
    unittest.main()
