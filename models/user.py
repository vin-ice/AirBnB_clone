#!/usr/bin/python3
"""Instantiates base class"""

from models.base_model import BaseModel

class User(BaseModel):
    """Inherits from BaseClass
    Attributes:
        public:
            email (str): email
            password (str): password
            first_name (str): name
            last_name (str): name
    """
    email, password, first_name, last_name = "", "", "", ""

    pass