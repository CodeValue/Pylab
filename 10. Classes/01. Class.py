import random

# Classes
#------------

# Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object.
# Class instance has a "state" and methods that can modifying its state.


# Define a Class:
#-----------------

class Lecturer:
    pass


haim = Lecturer()
ori = Lecturer()
omer = Lecturer()

print(haim)
print(ori)
print(omer)

# haim != Ori != Omer              # Each of the objects pointint to a different location in memory
















# Define class's methods
#------------------------

# To refer our class from inside our class we use the "self" keyword
# in a certain sense, the "self" keyword is acted the same as "this" in C#\C++\Java 
# self will always be the first argument in a method

lecturers = []

class Lecturer:
    def lecturer_as_dictionary(self, name, lecturer_id = random.choice(range(1,1000))):
      return {"name": name, "lecturer_id": lecturer_id}

lecturer_obj = Lecturer()
haim = lecturer_obj.lecturer_as_dictionary("Haim")
lecturers.append(haim)
print(lecturers)












# Class constructor
#-------------------------------

# The __init__ method is a special method that defines a constructor for a class instance
# Although its a method, it's not allowed to return a value from this special method

lecturers = []

class Lecturer:
    def __init__(self, name, lecturer_id):
        lecturer = {"name": name, "lecturer_id": lecturer_id}
        lecturers.append(lecturer)


haim = Lecturer("haim", 234)
print(haim)










    # def __str__(self):
    #     return "I'm the lecturer of Python course"














# Class attribute & Instance attribute
#--------------------------------------------

# Class attribute are simply data that can be found in your class that can be accessed from all the methods inside the class
# It's important to mention that Python does not define access modifier for methods or class members.
# by default, all of those defined as public. Although, we using conventions to note private data and private methods. 

class Lecturer:
    
    company = "CodeValue"                               # Class attribute (static attribute)

    def __init__(self, name, lecturer_id):
        self.name  = name                               # Instance attribute 
        self.lecturer_id = lecturer_id

    def get_name_capitalize():
        return self.name.capitalize()
    
    def __str__(self):
        return "My name is {0} and I'm a lecturer".format(self.name.title())

    def get_company_name(self):
        return self.company

haim = Lecturer("haim", 234)
print(haim.get_name)
print(Lecturer.company)


