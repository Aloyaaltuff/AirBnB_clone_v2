##!/usr/bin/python3
import uuid
from datetime import datetime
from models.engine.file_storage import storage
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class BaseModel:
    """A base class for all other classes in the project"""

    def __init__(self, *args, **kwargs):

        def __init__(self, *args, **kwargs):
    for key, value in kwargs.items():
        if key != "__class__":
            setattr(self, key, value)

    def save(self):
        self.updated_at = datetime.now()
 self.updated_at = datetime.utcnow()
    models.storage.new(self)
    models.storage.save()

    def to_dict(self):
    my_dict = self.__dict__.copy()
    if "_sa_instance_state" in my_dict:
        del my_dict["_sa_instance_state"]
    return my_dict
    def delete(self):
    models.storage.delete(self)

id = Column(String(60), primary_key=True, nullable=False)
created_at = Column(DateTime, default=datetime.utcnow(), nullable=False)
updated_at = Column(DateTime, default=datetime.utcnow(), nullable=False)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
