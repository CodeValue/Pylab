import lecturer

from lecturer import *

class DevOpsLecturer(Lecturer):
    
    topics = "DevOps"
    
    def __str__(self):
        return "My name is {0} and I'm a DevOps lecturer".format(self.name.title())

    def get_company_name(self):
        return super().self.company + " Israel" 
















