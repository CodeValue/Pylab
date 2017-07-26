

# Dictionary 
#-------------

# Define a dictionary

lecturer = { "name": "Haim", "lecturer_id": 11, "courses": "Python" }

if lecturer["name"] == "Haim":
    print("You can ask me question about Python")



















# Useful methods
#-----------------

devops_lecturers = [
    { "name": "Ori", "lecturer_id": 10, "courses": "Linux Basics" },
    { "name": "Haim", "lecturer_id": 11, "courses": "Python" },
    { "name": "Omer", "lecturer_id": 12, "courses": "Computer Networking" },
    { "name": "Maor", "lecturer_id": 13, "courses": "CI\CD"},
    { "name": "Hagai", "lecturer_id": 14, "courses": "Kubernetes" },
]


# Get a specific item 
haim = devops_lecturers[1]

# Adding a new key-pair 
haim["surname"] = "Kabesa"

# Returns a list of all keys
keys = haim.keys()

# Returns a list of all values
values = haim.values()

# Add new item to the list of dictionaries
devops_lecturers.append({ "name": "Ido", "lecturer_id": 15, "courses": ""})

# Editing the value of particular 
haim["name"] == "Abu Python"

# Delete a key pair 
del haim["name"]

print(devops_lecturers)










# Customise the error when the key does not exist. 
#-------------------------------------------------

devops_lecturers = [
    { "name": "Ori", "lecturer_id": 10, "courses": "Linux Basics" },
    { "name": "Haim", "lecturer_id": 11, "courses": "Python" },
    { "name": "Omer", "lecturer_id": 12, "courses": "Computer Networking" },
    { "name": "Maor", "lecturer_id": 13, "courses": "CI\CD"},
    { "name": "Hagai", "lecturer_id": 14, "courses": "Kubernetes" },
]


# for lecturer in devops_lecturers:
#     if lecturer["surname"] == "Fridman":                   # will invoke a KeyError exception
#         print("")                                   


# A more errors aware approach

for lecturer in devops_lecturers:
    if lecturer.get("surname", "Unknown Key") == "Unknown Key":                   
        print("This dictionary does not include a key named surname.")                                   





























