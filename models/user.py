#!/usr/bin/python3
'''A class user that inherent from BaseModel'''
from models.base_model import BaseModel

class User(BaseModel):
    '''represent a class User'''

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    @classmethod
    def all(cls):
        """
        Return all instances of the class
        """
        from models import storage
        return [obj for obj in models.storage.all().values() if isinstance(obj, cls)]
