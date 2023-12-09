#!/usr/bin/python3
from models.engine.file_storage import FileStorage

# Create a unique FileStorage instance
storage = FileStorage()

# Call reload() method on this variable
storage.reload()


from models.base_model import BaseModel

classes = {
    'BaseModel': BaseModel,
}
