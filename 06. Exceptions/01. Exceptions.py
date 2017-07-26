
# Exceptions
#------------
 
lecturer =  { "name": "Ori", "lecturer_id": 10, "courses": "Linux Basics" }

#surname = lecturer["surname"]                  # This code will throw an KeyError exception


 # Let's handle this exception properly

try: 
    surname = lecturer["surname"]
except KeyError:
    print("Error finding surname key")

print("This line code is reachable")






















# Chaining exceptions

lecturer["surname"] = "Kabesa"

try:
    surname = lecturer["surname"]
    number = surname + 5
except KeyError:
    print("Erro finding surname")
except TypeError as error:
    print("Cannot adding string to an integer.")

print("This line code is reachable")


# Exception object - it's a bad idea most of the times (explicity is better than implicity).
# Use the "as" keyword to get the real exception message.
# Get the Line number for debugging purposes

