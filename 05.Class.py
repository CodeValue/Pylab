# region class v1.0

  # students = []

  # class Student:
  #     def add_student(self, name, student_id=332):
  #         student = {"name": name, "student_id": student_id}
  #         students.append(student)

  # student = Student()
  # student.add_student("Mark")
  # print(students)

# endregion

# region class v1.1 (constructor)
  # students = []

  # class Student:
  #     def __init__(self, name, student_id=332):
  #         student = {"name": name, "student_id": student_id}
  #         students.append(student)

  #     def __str__(self):
  #         return students[0]["name"]

  # haim = Student("haim", 234)
  # print(haim)

# endregion

# region class v1.2 (instance && class attributes)

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

print(Student.school_name)

# endregion
