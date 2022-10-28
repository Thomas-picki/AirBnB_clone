#!/usr/bin/python3
"""define the class city"""
from models.base_model import BaseModel



class City(BaseModel):
    """represent a city
    attribute:
    state_id (str): the state id
    name(str): the name of city
    """
    state_id = ""
    name = ""
    
