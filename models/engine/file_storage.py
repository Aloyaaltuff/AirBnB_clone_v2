#!/usr/bin/python3
"""
Module for serializing and deserializing data
"""
import json
import os

class FileStorage:
     """
    FileStorage class for storing, serializing and deserializing data
    """
     __file_path = "file.json"
     __objects = {}
     
     def all(self):
        """
        Returns the __objects dictionary.
        It provides access to all the stored objects.
        """
        return FileStorage.__objects

     def new(self, obj):
         """
         Sets an object in the __objects dictionary with a key of
         <obj class name>.id.
        """
         if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

     def save(self):
         """
        Serializes the __objects dictionary into
        JSON format and saves it to the file specified by __file_path.
        """
         obj_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
         with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file)

     def reload(self):
        """
        This method deserializes the JSON file
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value.pop('__class__')
                    cls = globals()[class_name]
                    FileStorage.__objects[key] = cls(**value)

