#!/usr/bin/python3
"""
Specifies instructions for non-volatile storage and\
    retrieval of data
Provides an interface to interact with file system\
     via a file storage
"""

from json import dumps, load
import models.base_model as base_model
import models.user as user_model
import models.state as state_model
import models.city as city_model
import models.amenity as amenity_model
import models.place as place_model
import models.review as review_model

class FileStorage:
    """Primary interface to file-system storage.\
        Exposes functions to instance for data storing\
            , maipulation, and retrival

            all(self): returns the dictionary: (__objects)
            new(self, obj): sets obj into local dict(__objects) with a key 
            save(self): serializes __objects to JSON file
            reload(self): deserializes the JSON to __objects
    """
    
    __file_path, __objects = "file.json", {}

    def all(self):
        """
        returns dictionary: __objects
        """
        return type(self).__objects

    def new(self, obj):
        """sets obj in __objects
        Args:
            obj (obj)- Object whose att are to be saved 
        """
        type(self).__objects[".".join([obj.__class__.__name__, obj.id])] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        with open(type(self).__file_path, "w", encoding="utf-8") as f:
            f.write(dumps({k:v.to_dict() for (k,v) in (type(self).__objects).items()}, indent=4))
       
    def reload(self):
        """Deserializes JSON file to __objects"""
        classes = {
            "BaseModel" : base_model.BaseModel,
            "User" : user_model.User,
            "State" : state_model.State,
            "City" : city_model.City,
            "Amenity" : amenity_model.Amenity,
            "Place" : place_model.Place,
            "Review" : review_model.Review 
        }
        try:
            f = open(type(self).__file_path, "r", encoding="utf-8")
            json_dict = load(f)
            for _, v in json_dict.items():
                obj = classes[v['__class__']](**v)
                self.new(obj)
        except Exception:
            pass
        else:
            f.close()