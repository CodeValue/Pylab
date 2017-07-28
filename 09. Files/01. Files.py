import json















# Solution (ex. #3)
#---------------------

lecturers = []

def print_lecturers_details():
    for lecturer in lecturers:
        print("Name: {0} ID: {1}".format(lecturer["name"].title(), lecturer["lecturer_id"]))

def add_lecturer(name: str, lecturer_id: int):
    lecturer = {"name": name, "lecturer_id": lecturer_id}
    lecturers.append(lecturer)
    print("Lecturer's details were added successfully \n")


### Program: Lecturers List Organizer ###

print("""

Dear User,

Please note that this program meant to help you with organizing lecturers details lists.

The program will ask you to provide details about a lecturer.
Those details will be preserved by the program.
If you wish to exit the program, please respond with No when you will be asked by the program if you would like to proceed.

Have Fun!
""")

to_continue = True 

while to_continue:
    lecturer_name = input("Please enter lecturer name: ") 
    lecturer_id = input("Please enter lecturer ID: ")   

    add_lecturer(lecturer_name, lecturer_id)

    user_answer = ""
    is_valid_answer = False
    while not is_valid_answer:
        user_answer = input("Do you want to proceed? ")
        
        if user_answer != "No" and user_answer != "Yes":
            print("Please answer with Yes or No only. \n")
        else:
            is_valid_answer = True
            if user_answer == "No": 
                to_continue = False
            break

print_lecturers_details()
    











#------------------------------------------------------------
#
#  Let's learn how to make a data persistent app with files
# 
#-------------------------------------------------------------














# Files 
#-----------

f = open("lecturers.txt", "a")

# open() returns a file object, and is most commonly used with two arguments: open(filename, mode).
# The first argument is a string containing the filename. 
# The second argument is another string containing a few characters describing the way in which the file will be used.
#   'r' - for read purpose only, it's also the default mode when mode argument is omitted
#   'w' - for write purpose only, an existing file with the same name will be erased
#   'a' - for append purpose, any data written to the file is automatically added to the end
#   'r+' - opens the file for both reading and writing
#   'b[r | w| r+|' - for read and write binary files (JPEG, exe etc.)
















# Useful methods:
#-----------------

f = open("lecturers.txt", "a")

f.read()                # read the entire file unless a size argument was provided

f.readline()            # read a single line (use yield and iteratable object.
                        # for more details http://anandology.com/python-practice-book/iterators.html)

f.readlines()           # returns a list of all lines in the file

f.write("Hello")        # write the conetet of a string into the file
                        # To write something other than a string, it needs to be converted to a string first:
                        # >>> value = 23
                        # >>> s = str(value)
                        # >>> f.write(s)

f.close()              # save & close the file, also free the stream resource it was used

f.closed               # returns True if the file is closed and False if not


with open('lecturers.txt', 'r') as f:              # with statements are a best practice when working with files
     read_data = f.read()                          # There is no need to explicitly call f.close(), this is done by the with statement

f.closed                                           # the answer for this call will be false.  









# Saving structured data with (json)
#------------------------------------

lecturers = json.dumps(['Ori', 'Haim', 'Omer'])             # json format
# will print the following: ["Ori", "Haim", "Omer"]


# Serialization and Deserialization
#-----------------------------------

json.dump(x, f)                 # x is the object to serialize and f is a already opened file

x = json.load(f)                # creat an object from opened file f 












# # Exercise #4
# #-------------
# # 
# # Following the previous exercise - ex. #3.
# # 1. Support data-persistency functionlity. Store the lecturers' details into a file called lecturer.txt  
# #     1.1 The implementation should take into account data loss and exceptions handling   
# # 2. Print all stored lecturers before the first time the program asks the user to add new lecturer's details.
























# # Solution (ex. #4)
# #---------------------

storage_file = "lecturers.txt"

def print_lecturers_details():
    lecturers = read_lecturers_from_storage_file()
    print_title = True
    if not len(lecturers):
        print("Lecturers list is currently empty. \n")
        return
    for lecturer in lecturers:
        if print_title:
            print("Lecturer List:")
            print("---------------")
            print_title = False
        print("Name: {0}     ID: {1}".format(lecturer["name"].title(), lecturer["lecturer_id"]))


def add_lecturer(name: str, lecturer_id: int):
    lecturer = {"name": name, "lecturer_id": lecturer_id}
    save_lecturer_details_to_storage_file(lecturer)
    print("Lecturer's details were added successfully \n")


def save_lecturer_details_to_storage_file(lecturer):
    try:
        with open(storage_file, "a") as f:
            f.write(lecturer["name"] + "," + lecturer["lecturer_id"] + "\n")
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))


def read_lecturers_from_storage_file():
    lecturers = []
    try:
        with open(storage_file, "r") as f:
            for lecturer in f.readlines():
                lecturer_details = str(lecturer).split(",")
                lecturers.append({"name": lecturer_details[0], "lecturer_id": lecturer_details[1]})
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except Exception as e:
        print("Unexpected error:".format(e.errno, e.strerror))
        raise
    return lecturers


### Program: Lecturers List Organizer ###

print("""

Dear User,

Please note that this program meant to help you with organizing lecturers details lists.

The program will ask you to provide details about a lecturer.
Those details will be preserved by the program.
If you wish to exit the program, please respond with No when you will be asked by the program if you would like to proceed.

Have Fun!
""")

print_lecturers_details()

to_continue = True 

while to_continue:
    lecturer_name = input("Please enter lecturer name: ") 
    lecturer_id = input("Please enter lecturer ID: ")   

    add_lecturer(lecturer_name, lecturer_id)

    user_answer = ""
    is_valid_answer = False
    while not is_valid_answer:
        user_answer = input("Do you want to proceed? ")
        
        if user_answer != "No" and user_answer != "Yes":
            print("Please answer with Yes or No only. \n")
        else:
            is_valid_answer = True
            if user_answer == "No": 
                to_continue = False
            break

print_lecturers_details()


    














