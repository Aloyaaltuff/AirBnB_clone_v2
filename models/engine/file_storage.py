#!/usr/bin/python3
import json
import os

class FileStorage:
    """Serializes instances to a JSON file and deserializes JSON file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):

        return self.__objects

    def new(self, obj):

        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):

        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):

        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value.pop('__class__')
                    cls = globals().get(class_name)
                    if cls:
                        self.__objects[key] = cls(**value)


storage = FileStorage()
storage.reload()
