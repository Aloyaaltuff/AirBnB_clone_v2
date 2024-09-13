#!/usr/bin/python3
"""Defines a class City for city object"""
from models.base_model import BaseModel


class City(BaseModel,Base):
    """Class for city"""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False
