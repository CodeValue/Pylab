import os
import pathlib


current_directory = os.getcwd()      # Return the current working directory
print("Current directory: {0}".format(current_directory))

home = os.path.expanduser("~")
os.chdir(home + "/PyLab")   # Change current working directory to user's home directory
print("Current directory: {0}".format(os.getcwd()))

pathlib.Path(home + "/PyLab/new_dir").mkdir(parents=True, exist_ok=True)
os.chdir(home + "/PyLab/new_dir")
print("Current directory: {0}".format(os.getcwd()))
