#!/usr/bin/python3
"""Module containing base class for the AirBnB_clone Project"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    Defines common attributes for all sub classes
    Public
        Instance Properties
            id (uuid): unique id of object
            created_at (datetime): creation time
            updated_at (datetime): update time

            save (def): Updates refrectoring time
            to_dict(def): Serializer/Desirializer
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes objects 
        Serializes fields into python objects if fields are passed (**kwargs)
        """                    
        if len(kwargs) > 0:
            for k,v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                self.__dict__[k] = v
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute; 'updated_at' with current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """
        Deserializes objects' fields to 'simple object types'
        """
        s_dict = {"__class__": type(self).__name__}
        for k, v in self.__dict__.items():
            if k == "created_at" or k == "updated_at":
                v = v.isoformat()
            s_dict[k] = v
        return s_dict
                   
    def __str__(self):
        """Returns a human readable representation of the object"""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)