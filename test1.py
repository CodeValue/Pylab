import random


print("Hello World")

# BAD:                          |
counter = 0
while counter < 5:
    print(counter)
    counter += 1

# GOOD:                         |
for i in range(5):
    print(i)






items = ["Go", "Go", "Power", "Rangers", "Yeh!"]
selected_item = random.choice(items)

# BAD:
def do_complicated_thing(*args):
    x, y = args
    return dict(**locals)

# GOOD:
def do_the_same_but_simpler(x, y):
    return {'x' : x, 'y' : y}


NAME = "PythonBo"
MACHINE = NAME + "HAL"

print("Nice to meet you {0}. I am {1}".format(NAME, MACHINE))

if 5:
    print("Hi")
else:
    print("Ho no...")


number = 5
if number == 5: 
    print("Number is 5")
else:
     print("Number is not 5")


student_names = []
student_names = ["Mark", "Katarina", "Jessica"]

student_names[0] = "Haim"

student_names.append("Hagai")

print(student_names)

print("yes") if "Mark" in student_names == True else print("no")

print(len(student_names))

del student_names[2]

print(student_names)


print(student_names[1:-1])

for name in student_names:
    print("Student name is {0}".format(name))

