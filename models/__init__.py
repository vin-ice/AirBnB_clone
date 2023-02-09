#!/usr/bin/python3
"""Imports modules"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
