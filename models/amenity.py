#!/usr/bin/python3
"""Instantiates base class"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """Inherits from BaseClass
    Attributes:
        public:
            name (str): name
    """
    name = "", ""

    pass