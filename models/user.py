#!/usr/bin/python3
""" Defines the user"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User
    Attribute:
    email(str): the email of user
    password (str): the password of user
    first_name (str): the first name of user
    last name(str): the last name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
