


# Exercise #3:
# 
# Create a program that addresses the following requirements: 
# 1. The user will be asked to enter a "lecturer name" and "lecturer id".
# 2. Those inputs will be preserved until the user answer "no" to the "Do you want to proceed?" question.
#   2.1 The user can answer to the question "Do you want to proceed?" with "Yes" or "No" only. 
# 3. Before the program exit, the program will print all the lecturers details that were entered by the user
#   3.1 The name of the lecturer should be capitlized in its first letter no matter what the user use when type the name

































# Solution (exc. 3)
#---------------------

devops_lecturers = []
to_continue = True 

while to_continue:
    lecturer_name = input("Enter lecturer name:") 
    lecturer_id = input("Enter lecturer ID:")   

    def get_lecturer_titlecase():
        lecturer_titlecase = []
        for lecturer in devops_lecturers:
            lecturer_titlecase.append(lecturer["name"].title())
        return lecturer_titlecase

    def print_lecturer_titlecase():
        lecturers_titlecase = get_lecturer_titlecase()
        print(lecturers_titlecase)

    def add_lecturer(name, lecturer_id=332):
        lecturer = {"name": name, "lecturer_id": lecturer_id}
        devops_lecturers.append(lecturer)

    add_lecturer(lecturer_name, lecturer_id)

    answer = input("Do you want to proceed?")
    if answer == "No":
        to_continue = False
        print_lecturer_titlecase()
    




































# Files 


def save_file(lecturer):
    try:
        f = open("lecturers.txt", "a")
        f.write(lecturer + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def read_file():
    try:
        f = open("lecturers.txt", "r")
        for lecturer in f.readlines():
            add_lecturer(lecturer)
        f.close()
    except Exception:
        print("Could not read file.")