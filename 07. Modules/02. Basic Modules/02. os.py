import os


current_directory = os.getcwd()      # Return the current working directory
print("Current working directory is: {0}".format(current_directory))

home = os.path.expanduser("~")
os.chdir(home + "/PyLab")   # Change current working directory to user's home directory
print("Current working directory is: {0}".format(os.getcwd()))

result_code = os.system("mkdir /new_dir")   # Run the command mkdir in the system shell 0

if result_code == 256:
    os.chmod(os.getcwd(), 0o777)
    os.system("mkdir./new_dir")



os.system("sudo mkdir /new_dir")   # Run the command mkdir in the system shell 0

os.chdir(home + "/new_dir")   
print("Current working directory is: {0}".format(os.getcwd()))
