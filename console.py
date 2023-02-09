#!/usr/bin/python3
"""
A command-line tool for manipulating data
It provides an interface for fast and in-expensive interaction\
    with the underlying structures
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage

class HBNBCommand(cmd.Cmd):
    """
    Console class providing interface for HCI
    """
    
    __classes = { "BaseModel": BaseModel }
    prompt = "(hbnb) "
    def do_quit(self, _):
        """Handles the quit command and exits program"""
        quit()

    def do_EOF(self, _):
        """Handles programme termination on end-of-file"""
        quit()

    def do_create(self, cls_name):
        """
        Creates a new instance, saves it in JSON\
        and prints its id
        args:
            cls_name (str): name of Class to instantiate
        """
        if not cls_name:
            print("** class name missing **")
        else:
            if cls_name in type(self).__classes:
                obj = type(self).__classes[cls_name]()
                obj.save()
                print("{}".format(obj.id))
            else:
                print("** class doesn't exist **")
    def do_show(self, args):
        """Prints the string repr of an instance based on class name and id
        args:
            cls_name (str): __Classes' name 
            id (str): of an object
        """
        args = args.split()
        cls_name, id = args[0], args[1]
        if not cls_name:
            print("** class name missing **")
        elif not cls_name in type(self).__classes:
            print("** class doesn't exist **")
        elif not id:
            print ("** instance id missing **")
        else:
            key = ".".join([cls_name, id])
            objects = FileStorage().all()
            if key in objects:
                print("{}".format(objects[key]))
            else:
                print("** no instance found **")

    def do_destroy(self, cls_name=None, id=None):
        """Deletes an instance based on the class name and id
        args:
            cls_name (str): Class name
            id (str): Obj id
        """
        this = type(self)
        if not cls_name:
            print("** class name missing **")
        elif not cls_name in this.__classes:
            print("** class doesn't exist **")
        elif not id:
            print("** instance id missing **")
        else:
            objects = FileStorage().all()
            key = ".".join([cls_name, id])
            if not key in objects:
                print("** no instance found **")
            else:
                store = FileStorage()
                del objects[key]
                for _, v in objects.items():
                    obj = this.__classes[v['__class__']](**v)
                    store.new(obj)

    def do_all(self, args):
        """Prints all string repr of all instances based on the class name"""
        if args:
            cls_name = args[0]
            if not cls_name in type(self).__classes:
                print("** class doesn't exist **")
            else:
                for _, v in storage.all().items():
                    if v['__class__'] == cls_name:
                        obj = type(self).__classes[cls_name](**v)
                        print(obj.__str__()) 
        else:
            for _, v in storage.all().items():
                cls_name = v['__class__']
                obj = type(self).__classes[cls_name](**v)
                obj.__str__()
                
    def do_update(self, args):
        """Updates an instance based on class name and id"""
        if len(args) == 0:
            print("** class name missing **")
        else:
            cls_name = args[0]
            if not cls_name in type(self).__classes:
                print("** class doesn't exist **")
            else: 
                if len(args) >= 2:
                    id = args[1]
                    for k, v in storage.all.items():
                        if v['id'] == id:
                            if len(args) >=3:
                                attr = args[2]
                                if attr in v:
                                    if len(args) >= 4:
                                        val = args[3]
                                        v[attr] = val
                                        cpy = v
                                        del storage.__objects[k]
                                        obj = type(self).__classes[v['__class__']](**cpy)
                                        obj.save()
                                    else:
                                        print("** value missing **")    
                            else:
                                print("** attribute name missing **")    
                    print("** no instance found **")
                else:
                    print("** instance id missing **")    
                

    def emptyline(self):
        """Overides implementation of empty+ENTER input"""
        pass
if __name__ == "__main__":
    HBNBCommand().cmdloop()