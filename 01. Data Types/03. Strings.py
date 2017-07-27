

# Deifine a string
#------------------
str1 = 'Python'
str2 = "Is so"
str3 = """Cool"""

# Use one, two or three quote marks to define a string
# For strings we usually use the one or two quote marks.
# Three quotes are often used for multi-line documentation

if 'Mint' == "Mint" and 'Mint' == """Mint""" and "Mint" == """Mint""":
    print(""" 'Mint' == "Mint" """ + '== """Mint""" ')













# Usfull methods 
#------------------

print("Python".upper())                                         # Retuen a capitalized version of the string


if not "DevOps".islower():                                      # Check if all letters are lowercase
    print("The word DevOps is not completely lowercased")

print("foo".replace('f', 'b'))                                  # Replace a character within the string

if "123".isdigit:                                               # Check if all characters are numeric digit
    print("This string represent a number.")











# format and splits
#------------------

lecturers = " Ori, Haim, Hagai, Maor, Omer".split(",")           # Return a list of the elements splited by 
linux_course_lecturer = lecturers[0]
python_course_lecturer = lecturers[1]
networing_course_lecturer = lecturers[4]                           

print(
    """
    Course                  Lecturer
    ------                  --------     
    Linux Basics            {0}
    Python programming      {1}
    Computers Networking    {2}
    """.format(linux_course_lecturer ,python_course_lecturer, networing_course_lecturer))        











#  String interpolation      
#----------------------

print(
    f"""
    Course                  Lecturer
    ------                  --------     
    Linux Basics            {linux_course_lecturer}
    Python programming      {python_course_lecturer}
    Computers Networking    {networing_course_lecturer}
    """)
