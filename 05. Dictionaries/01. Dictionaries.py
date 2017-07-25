

# Dictionary 
#-------------

# Define a dictionary

devops_lecturers = [
    { "name": "Ori", "lecturer_id": 10, "courses": "Linux Basics" },
    { "name": "Haim", "lecturer_id": 11, "courses": "Python" },
    { "name": "Omer", "lecturer_id": 12, "courses": "Computer Networking" },
    { "name": "Maor", "lecturer_id": 13, "courses": "CI\CD"},
    { "name": "Hagai", "lecturer_id": 14, "courses": "Kubernetes" },
]

for lecturer in devops_lecturers:
    if lecturer["name"] == "Ori":
        print("You can ask a question about Linux!")
    else:
        if lecturer["courses"] == "CI\CD": 
            print("You can ask a question about CI\CD!")










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

# Returns a list of all keys
keys = haim.keys()

# Returns a list of all values
values = haim.values()

# Add new item to the list of dictionaries
devops_lecturers.append({ "name": "Ido", "lecturer_id": 15, "courses": ""})

# Editing particular key in specific item
haim["name"] == "Haim Kabesa"

del haim["name"]

print(devops_lecturers)