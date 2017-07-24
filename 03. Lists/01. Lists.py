 

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
if "Esti" in lecturers:
    print("Esti is a lecturer")      # will not be executed


# List size
print(len(lecturers))                 # will print 5










# List slicing
#---------------

# Very similar to projection of a list in C# using Linq functoin Take()

lecturers = ["Ori", "Haim", "Omer", "Maor", "Hagai"]

print(lecturers[1:])
print(lecturers[1:-2])





# We Will back to talk about lists in the next session










# List comprehension
#-------------------- 

# Exercise #1:
# 
# Create a list of all squares from 1 to 100.
#




















# Structure:
#      [<expr> for item in collection]
# 
# 