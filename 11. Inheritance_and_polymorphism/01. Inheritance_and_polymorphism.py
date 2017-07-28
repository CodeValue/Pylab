
# Inheritance_and_polymorphism
#-------------------------------

# Inheritance defines a relation-tree between different data types
# In Python it's allow to inherit from multiple base classes - DON'T DO IT!

class Lecturer:
    
    topics = "General"                                  # Class attribute (static attribute)
    self.name  = name                                   # Instance attribute 
    self.lecturer_id = lecturer_id
    
    def __init__(self, name, lecturer_id):
        self.name  = name                               # Instance attribute 
        self.lecturer_id = lecturer_id

    def get_name_capitalize(self):
        return self.name.capitalize()
    
    def __str__(self):
        return "My name is {0} and I'm a lecturer".format(self.name.title())

    def get_topics_name(self):
        return self.topics

ori = Lecturer("Ori", 234)
print(ori.get_name_capitalize())
print(Lecturer.topics)


class DevOpsLecturer(Lecturer):
    
    topics = "DevOps"
    
    def __str__(self):
        return "My name is {0} and I'm a DevOps lecturer".format(self.name.title())


    def get_topics_name(self):
        return super().self.topics + " Israel" 

ido = DevOpsLecturer("Ido", 456)
print(DevOpsLecturer.topics)














