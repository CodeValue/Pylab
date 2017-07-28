

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
    



