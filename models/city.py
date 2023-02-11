#!/usr/bin/python3
"""Instantiates base class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from BaseClass
    Attributes:
        public:
            state_id (str): state id
            name (str): name
    """
    state_id, name = "", ""

    pass
