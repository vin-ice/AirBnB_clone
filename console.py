#!/usr/bin/python3
"""
A command-line tool for manipulating data
It provides an interface for fast and in-expensive interaction\
    with the underlying structures
"""

import cmd
import ast
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Console class providing a command-line interface
    """
    __cache = storage.all()
    prompt = "(hbnb) "
    use_rawinput = False
    

    def _parse(line):
        """
        Parses a function to a simple command line
        Args:
            line (str): Non-standeard command
        """
        parts = line.split(".")
        _cls = parts[0]
        _cmd = parts[1].split("(")[0]
        _params = parts[1].split("(")[1].strip(")") .split(",")
        if len(_params) >= 1:
            _id = _params[0]
            if len(_params) > 1:
                _args = ",".join(_params[1:]).strip()
                if '{' in _args:
                    _val = []
                    for k, v in ast.literal_eval(_args).items():
                        _val.append(" ".join([_cmd, _cls, _id, k, str(v)]))
                    return (" ; ".join(_val))
                else:
                    _val, _vals = [_cmd, _cls, _id], _args.split(",")
                    for i in _vals:
                        _val.append(str(i))
                    return (" ".join(_val))
            return (" ".join([_cmd, _cls, _id]))
        else:
            return (" ".join([_cmd, _cls]))

    def precmd(self, line):
        if "." in line:
            return HBNBCommand._parse(line)
        return line

    def do_create(self, args):
        """
        Creates a new instance, saves it to JSON a file
            and prints its id
        args:
            args (str): name of Class to instantiate
        Usage:
            create <class>
        """
        args = args.split()
        if HBNBCommand.__check_err(args, 1) is True:
            obj = HBNBCommand.__get_m_class(args[0])()
            obj.save()
            print(obj.id)

    def do_show(self, args):
        """Prints the string repr of an instance based on class name and id
        Args:
            args: arguments 
        """
        args = args.split()
        if HBNBCommand.__check_err(args, 2) is True:
            instance = HBNBCommand.__get_m_instance(args[0], args[1])
            print("{}".format(instance.__str__()))

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        args:
            args (str): Arguments
        """
        args = args.split()
        if HBNBCommand.__check_err(args, 2) is True:
            key = ".".join([args[0], eval(args[1])])
            del(HBNBCommand.__cache[key])
            storage.save()

    def do_all(self, args):
        """
        Prints all string repr of all instances based on the class name
        """
        args = args.split()
        if len(args) == 0:
            for _, v in HBNBCommand.__cache.items():
                print(v.__str__())
        elif HBNBCommand.__check_err(args, 1) is True:
            for _, v in HBNBCommand.__cache.items():
                if isinstance(v, HBNBCommand.__get_m_class(args[0])):
                    print("{}".format(v.__str__()))

    def do_update(self, args):
        """
        Updates an instance based on class name and id
        """
        args = args.split()
        if HBNBCommand.__check_err(args, 4):
            k, v = args[2], args[3]
            obj = HBNBCommand.__get_m_instance(args[0], args[1])
            setattr(obj, k, v)
            obj.save()

    def do_count(self, args):
        """
        Counts Number of instances of a given Class
        Args:
            args (str): class name
        """
        args = args.split()
        if HBNBCommand.__check_err(args, 1):
            count = 0
            for _, v in HBNBCommand.__cache.items():
                if isinstance(v, HBNBCommand.__get_m_class(args[0])):
                    count += 1
            print(count)

    def emptyline(self):
        """Overides implementation of empty+ENTER input"""
        pass

    def do_quit(self, _):
        """Handles the quit command and exits program"""
        return True

    def do_EOF(self, _):
        """Quit command to exit the program"""
        return True
    
    def help_quit(self):
        """
        Implements help for quit
        """
        print("Quit command to exit the program")
        print()        
    
    def help_EOF(self):
        """
        Implements help for quit
        """
        print("Quit command to exit the program")
        print()        

    @classmethod
    def __get_m_class(cls, name):
        """
        Returns a Model Class if present
        Args:
            name (str): Possible class name
        Return:
            Class identifier if present else None
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        for ele in dir():
            if name == ele:
                return eval(ele)
        return None

    @classmethod
    def __get_m_instance(cls, cls_name, id):
        """
        Returns object referenced by class and id else None
        Arg:
            cls: Class reference
            id: objects id
        """
        _cls = cls.__get_m_class(cls_name)
        for _, v in cls.__cache.items():
            if v.__class__ == str(_cls) and v.id == ast.literal_eval(id):
                return v
        return None

    @classmethod
    def __hasclass(cls, _, name):
        """
        Verifies if class name exists
        Returns True if exists else False
        """
        if cls.__get_m_class(name) is None:
            return False
        return True

    @classmethod
    def __hasinstance(cls, cls_name, id):
        """
        Checks if there is an instance of class and specified id
        Args:
            cls_name (str): Class name
            id (str): Instance id
        """
        if cls.__get_m_instance(cls_name, id) is None:
            return False
        return True

    @classmethod
    def __check_err(cls, argv, fields):
        """
        Loops through argv checking for errors
        if error, prints it on console else returns
        Args:
            argv (str): Vector of arguments
            fields (int): Fields in argv to error check
        Return:
            argv if no errors else False
        """
        errors = {
            "0": ["** class name missing **", "** class doesn't exist **"],
            "1": ["** instance id missing **", "** no instance found **"],
            "2": ["** attribute name missing **"],
            "3": ["** value missing **"]
        }
        ops = {
            "0": cls.__hasclass,
            "1": cls.__hasinstance
        }
        id = 0
        op = False

        if len(argv) == 0 and fields >= 1:
            print("{}".format(errors[str(id)][0]))
            return False
        else:
            for id, arg in enumerate(argv):
                id, op = str(id), False
                if id in ops:
                    if int(id) > 0:
                        op = ops[id](argv[0], arg)
                    else:
                        op = ops[id](argv[int(id) - 1: int(id)], arg)
                    if op is False:
                        print(errors[id][1])
                        return False
            id = int(id)
            if id < fields - 1 and id < 3:
                print("{}".format(errors[str(id + 1)][0]))
                return False
            return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
