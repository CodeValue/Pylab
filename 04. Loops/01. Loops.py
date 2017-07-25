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

















# Python for loop act like foeach in C# 
for lecturer in lecturers:
    print(lecturer)

# While loops
i = 0
while i < 10:
    print(i)
    i += 1  






# Exercise #1:
# 
# 1. Create a list of all squares from 1 to 100.
# 2. Print the list
#

















    

 




# Solution:

numbers = []
x = 1
while x <= 100:
    numbers.append(x)
    x += 1

for i in numbers:
    print(i**2)




# Preferred solution
for num in range(1,100):
    print(num**2)




















