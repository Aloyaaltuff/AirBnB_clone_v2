#!/usr/bin/python3

"""This module creates a state class"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, base):
    """Class for  state objects mangment """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
@property
    def cities(self):
        from models import storage
        return [city for city in storage.all(City).values() if city.state_id == self.id]
