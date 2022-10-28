#!/usr/bin/python3
"""define the review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review
    attribute:
    place_id (str): the place id
    user_id (str): the user id
    text (str): the text of the review
    """
    
    place_id = ""
    user_id = ""
    text = ""
