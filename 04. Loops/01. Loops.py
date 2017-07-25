import random












# Loops
#--------

lecturers = ["Ori", "Haim", "Omer", "Maor", "Hagai"]

# print all the elements in the lecturer list
print(lecturers[0])
print(lecturers[1])
print(lecturers[2])
#
# ...
# 
# this method doesn't scale...
















# For Loops
#---------------

lecturers = ["Ori", "Haim", "Omer", "Maor", "Hagai"]

# Python for loop act like foeach in C#
 
for lecturer in lecturers:
    print(lecturer)






















# While Loops
#---------------

i = 0
while i < 10:
    print(i)
    i += 1  


# When using a while loops you must to increment the counter manually to avoid from an infinite loop.

# Example #1

prime_minister = "Bibi"

# while prime_minister == "Bibi":
#     print("Nope. This loop will never end")

num = 5


# Example #2

# while True:
#     if num == 10:
#         print("This line of code will never execute")














# Skipping iterations

num = 0

while num < 30:
    num = random.choice(range(1,20))
    if num > 10 and num < 15:
        break
    else:
        if num == 7:
            continue
        print("The chosen number was smaller than 10, greater than 15 and not the number 7")












