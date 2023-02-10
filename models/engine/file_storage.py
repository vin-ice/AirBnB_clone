#!/usr/bin/python3
"""
Specifies instructions for non-volatile storage and\
    retrieval of data
Provides an interface to interact with file system\
     via a file storage
"""

from json import dumps, load

class FileStorage:
    """Primary interface to file-system storage.\
        Exposes functions to instance for data storing\
            , maipulation, and retrival
        Class:
            Private:
                __file_paths (str): Name of file to hold objects
                __objects (dict): Object representation of all stored data
        
        Instance: 
            Public:
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
        """
        Adds a new object to the local __objects structure
        Args:
            obj (obj)- Address of Dictionary with native &\
                 non-native data types
        """
        type(self).__objects[".".join([obj.__class__.__name__, obj.id])] = obj

    def save(self):
        """
        Serializes __objects to JSON string values and stores in a json file
        """
        with open(type(self).__file_path, "w", encoding="utf-8") as f:
            f.write(dumps({k:v.to_dict() for (k,v) in (type(self).__objects).items()}, indent=4))
       
    def reload(self):
        """
        Deserializes JSON strings to Model class objects
        Stores then in local __objects dictionary
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        try:
            f = open(type(self).__file_path, "r", encoding="utf-8")
            json_dict = load(f)
            for _, v in json_dict.items():
                obj = eval(v['__class__'])(**v)
                self.new(obj)
        except Exception:
            pass
        else:
            f.close()