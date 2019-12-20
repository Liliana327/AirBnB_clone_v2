#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
import BaseModel, Base


class City(BaseModel):

    __tablename__ = 'cities'
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
    """
        #lili....................
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        state_id = ""
        name = ""
        #........................
