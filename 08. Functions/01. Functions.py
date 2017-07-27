# Functions
#------------


# Functions are reuseable block of code.
# Python have many built in functions


print("Hello DevOps!")
str(3)                              # Parse the int into a string 
int("15")                           # Parse the string into an int

user_answer = input("Do you believe in life after love?")
print(user_answer)




























# Define a function 
#--------------------

devops_lecturers = [
    { "name": "Ori", "lecturer_id": 10, "courses": "Linux Basics" },
    { "name": "Haim", "lecturer_id": 11, "courses": "Python" },
    { "name": "Omer", "lecturer_id": 12, "courses": "Computer Networking" },
    { "name": "Maor", "lecturer_id": 13, "courses": "CI\CD"},
    { "name": "Hagai", "lecturer_id": 14, "courses": "Kubernetes" },
]


def get_lecturer_names():
    lecturers_names = []
    for lecturer in devops_lecturers:
        lecturers_names.append(lecturer["name"])
    return lecturers_names


print(get_lecturer_names())

























# Function can perform an action without returning a value (void function C#)

def get_lecturer_names():
    lecturers_names = []
    for lecturer in devops_lecturers:
        lecturers_names.append(lecturer["name"])
    print(lecturers_names)


get_lecturer_names()





















# Function arguments

def add_new_lecturer(name, id):
    lecturer = {"name": name, "id": id}
    devops_lecturers.append(lecturer)


add_new_lecturer("Ido", 123)
print(devops_lecturers)



# Default arguments 

def add_new_lecturer(name, id):
    lecturer = {"name": name, "id": id}
    devops_lecturers.append(lecturer)


# Named arguments

add_new_lecturer(name="haim", id=13)






# Variable number of arguments

print("Shalom")
print("Shalom", "Hello")
print("Shalom", "Hello", "Haaln",12)
print("Shalom", "Hello", "Haaln",12, "x")
print("Shalom", "Hello", "Haaln",12, "x", 902)



def print_args(item, *args):
    print(item)
    print(args)


print_args("Haim", 12, "Hello", 234, "DevOps")
























# Keyword arguments 

def print_args(item, **kwargs):
    print(item)
    print(kwargs["my_age"], kwargs["where_i_live"])


print_args("Haim", my_age=34, where_i_live="Israel", what_i_like="Python & Beer")











# Exercise #3:
# 
# Create a program that addresses the following requirements: 
# 1. The user will be asked to enter a "lecturer name" and "lecturer id".
# 2. Those inputs will be preserved until the user answer "no" to the "Do you want to proceed?" question.
#   2.1 The user can answer to the question "Do you want to proceed?" with "Yes" or "No" only. 
# 3. Before the program exit, the program will print all the lecturers details that were entered by the user
#   3.1 The name of the lecturer should be capitlized in its first letter no matter what the user use when type the name

