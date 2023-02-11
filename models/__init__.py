#!/usr/bin/python3
"""Imports modules"""

from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
