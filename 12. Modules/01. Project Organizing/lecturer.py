class Lecturer:
    
    topics = "General"                                  # Class attribute (static attribute)

    def __init__(self, name, lecturer_id):
        self.name  = name                               # Instance attribute 
        self.lecturer_id = lecturer_id

    def get_name_capitalize(self):
        return self.name.capitalize()
    
    def __str__(self):
        return "My name is {0} and I'm a lecturer".format(self.name.title())

    def get_company_name(self):
        return self.company