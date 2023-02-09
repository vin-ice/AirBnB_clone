#!/usr/bin/python3
"""Instantiates base class"""

from models.base_model import BaseModel

class Review(BaseModel):
    """Inherits from BaseClass
    Attributes:
        public:
            place_id (str): Place.id
            user_id (str): User.id
            text (str)
    """
    place_id, user_id, text = "", "", ""

    pass