#!/usr/bin/python3
"""
Holds tests to the console
"""


HBNBCommand = __import__('console').HBNBCommand
from models import storage
import unittest
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """
    Contains test cases for the console
    """
    __cache = storage.all()

    def setUp(self):
        storage.reload()


    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(f.getvalue(), 
            "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create MyModel")
            self.assertEqual(f.getvalue(), 
            "** class doesn't exist **\n")
        
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertRegex(f.getvalue(),
            "^[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12}$")
    
    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            self.assertEqual(f.getvalue(), 
            "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show MyModel")
            self.assertEqual(f.getvalue(), 
            "** class doesn't exist **\n")
    
if __name__ == "__main__":
    unittest.main()