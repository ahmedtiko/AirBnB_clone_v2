#!/usr/bin/python3
'''
Module: base_model
'''

# Import necessary modules
import uuid
from datetime import datetime
import models


class BaseModel():
    '''
    Class: BaseModel
    '''
    def __init__(self, *args, **kwargs):
        '''
        Constructor for the BaseModel class
        '''
        if kwargs:
            # Convert string datetime values to datetime objects
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            # Assign key-value pairs to instance attributes
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            # Generate a unique ID and set creation and update times
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # Add the instance to the storage system
            models.storage.new(self)

    def __str__(self):
        '''
        Method: __str__
        Returns a string representation of BaseModel instance
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        '''
        Method: save
        Updates 'updated_at' instance with the current datetime
        '''
        self.updated_at = datetime.now()
        # Save changes to storage
        models.storage.save()

    def to_dict(self):
        '''
        Method: to_dict
        Returns a dictionary representation of the instance
        '''
        # Create a dictionary containing instance attributes
        new_dict = dict(self.__dict__)
        # Convert datetime objects to ISO format strings
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        # Add the class name to the dictionary
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
