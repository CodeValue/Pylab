 

 # Define a list
 #-----------------

# Empty list
lecturers = []

# Populated list
lecturers = ["Ori", "Haim", "Omer", "Maor", "Hagai"]

# List can hold items from different types
items = ["Hello", 3.14, True, ("23", -13), None]












# Indexing in lists
#-------------------

lecturers = ["Ori", "Haim", "Omer", "Maor", "Hagai"]

# Python is zero based programming language

print(lecturers[0])          # will print "Ori"
print(lecturers[4])          # will print "Hagai"


# Python support in negative index also!!!

print(lecturers[-2])         # will print "Maor"











# List editing
#--------------

lecturers = ["Ori", "Haim", "Omer", "Maor", "Hagai"]

lecturers[1] = "Ido"            # will replace Haim with Ido

print(lecturers)


# Add item 
lecturers.append("Ido")               # will add Ido to the end of the list
print(lecturers)


# Remove item
lecturers.remove("Maor")              # will remove Maor from the list
print(lecturers)

# Check if an item exist
if "Ofri" in lecturers:
    print("Ofri is a lecturer")      # will not be executed


# List size
print(len(lecturers))                 # will print 5










# List slicing
#---------------

# Very similar to projection of a list in C# using Linq functoin Take()

lecturers = ["Ori", "Haim", "Omer", "Maor", "Hagai"]

print(lecturers[1:])
print(lecturers[1:-2])

















#----------------------------------------------------------------------------------------------------
#
# Before we continue to talk about "List comprehension", but first let's talk about loops in Python
#
# ----------------------------------------------------------------------------------------------------














# Exercise #1:
# 
# 1. Create a list of all squares from 1 to 100.
# 2. Print the list
#

















    

 




# Solution (exc. 1):

numbers = []
x = 1
while x <= 100:
    numbers.append(x)
    x += 1

for i in numbers:
    print(i**2)






















# another solution... 

for num in range(1,100):                # The range method returns a list object populated by the numbers in the given range
    print(num**2)



# Now let's see an even better solution... 






# List comprehension
#-------------------- 

# 1. List comprehensions are a tool for transforming one list (any iterable actually) into another list.
# 2. During this transformation, elements can be conditionally selected.
# 3. Every list comprehension can be rewritten as a for loop but not vice versa
# 4. We will use list comprehension to perform only small tasks


# Example: 

old_things = []
new_things = []
for ITEM in old_things:
    if condition_based_on(ITEM):
        new_things.append("something with " + ITEM)


# You can rewrite the above for loop as a list comprehension like this:

new_things = ["something with " + ITEM for ITEM in old_things if condition_based_on(ITEM)]


















# How to transform for loop into list comprehension structure in 4 simple steps? 

numbers = [1, 2, 3, 4, 5]

doubled_odds = []
for n in numbers:
    if n % 2 == 1:
        doubled_odds.append(n * 2)



# 1. Copy the variable assignment for our new empty list (line 250)
doubled_odds = []

# 2. Copy the expression that we’ve been append-ing into this new list (line 253)
doubled_odds = [n * 2]

# 3. Copy the for loop line, excluding the final : (line 251)
#doubled_odds = [n * 2 for n in numbers]

# 4. Copy the if statement line, also without the : (line 252) 
doubled_odds = [n * 2 for n in numbers if n % 2 == 1]

























# List comprehension and nested loops

matrix = []
flattened = []
for row in matrix:
    for n in row:
        flattened.append(n)


# Can we transform a nested loop (matrix) into a list comprehension? YES, WE CAN!

flattened = [n for row in matrix for n in row]

# When working with nested loops in list comprehensions remember that the for clauses remain 
# in the same order as in our original for loops.










# Exercise #2:
# 
# Use list comprehensions perform the following:
#
# 1. Create a list of all squares from 1 to 100.
# 2. Print the list
#






















# Solution (exc. 2):

squares = [i **2 for i in range(1, 100)]
print("List comprehensions is cool!", squares)