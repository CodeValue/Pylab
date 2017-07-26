students = []


class Student:
    
    school_name = "Springfield Elementry"
    
    def __init__(self, name, student_id=332):
      self.name = name
      self.student_id = student_id
      students.append(self)

    def __str__(self):
          return "Student " + self.name
        # return students[0]["name"]

    def get_name_capitalize(self):
          return self.name.capitalize()

    def get_school_name(self):
          return self.school_name
