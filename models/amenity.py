#!/usr/bin/python3
"""defiens the amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represent an amenity

    attributes:
    name (str): the name of the amenity
    """
    
    name = ""
