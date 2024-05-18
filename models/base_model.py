#!/usr/bin/python3
import json
import uuid
from datetime import datetime
"""the class that all classes will inherit from"""


class BaseModle:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == 'created_at' or key == 'updated_at':
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
                        else:
                            self.id = str(uuid.uuid4())
                            self.created_at = datetime.now()
                            self.updated_at = datetime.now()

    def __str__(self):
        """a method that print class name, id"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updats updated_at"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        key and value  of an instance"""
    my_dict = self.__dict__.copy()
    for key, value in self.__dict__.items():
        if key == 'created_at' or key == 'updated_at':
            my_dict[key] = value.isoformat()

    my_dict['__class__'] = type(self).__name__
    return my_dict

if __name__ == "__main__":

    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
