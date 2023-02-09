# AirBnB clone - The console

The [AirBnBClone](.) project is a simple implementation of some of the core functionality of the [AirBnB System](https://www.airbnb.com/)

Major componanets include:

| Component | Description |
| ----------- | ------------------------------- |
| [Console](./console.py) | Interface for manipulating data |
| [Models Package](./models/) | Holds templates for data |
| [Storage Engine](./models/engine/) | Interface with data serialization/daserializartion functionality

## The Console
The [console](./console.py) is provides an simple command-line interface for interaction with the system and data

### Start
Run `python console.py` or `./console.py` at the root directory of the folder 

### Commands

| Command | Use |
| -------- | ---- |
| `help` or `help <command>`| Displays succinct description of system functions |
| `quit` | Terminates console application |
| ``create <class>`` | Creates an instace of save class |
| `show <class> <id>` | Prints string representation of an object |
| `destroy <class> <id>` | deletes an object |
| `all <class>` or `all` | Prints string representation of all objects or os a specific class |
| `update <class> <id> <key> <value>` | Updates an objects field |

