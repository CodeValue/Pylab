# IF statements
#-----------------

# Python uses indentation insted of curly braces for any code block
# By convention each level of indentation include four more spaces
#
# Example:
#
#          code_block:
#          ----inner_code_block:            # 4 spaces
#          --------inner_code_block2:       # 8 spaces
#          ------------inner_code_block3:   # 12 spaces














# If statements structure
#-------------------------

# Simple structure

todo_bom = True

if todo_bom == True:
    print("Everything is just fine!")
else:
    print("@#$R--=&^%%#@")       



# Canonical structure
honey_have_i_gained_weight = None

if honey_have_i_gained_weight == True:
    print("You are an idiot!")
else: 
    if honey_have_i_gained_weight == False: 
        print("You are an idiot!")
    else: 
        print("Well, surprisedly you're still an idiot!")






















# Negativity check  
#---------------------


# Use the keyword "not" or "!="

if todo_bom != True:
    print("Everything is just fine!")
else:
    print("You are an idiot!")       














# Truty values
#----------------

temp = 7

if temp:
    print("Any number other than 0 has a truty value.")


# PEP20: Explicit is better than implicit

is_found = False

if is_found:
    print("We found it!!!")
else:
    print("We didn't found it yet!")
















# Concatenation conditions
# ------------------------ 


# Use the keywords "and" and "or" (equivalent to "&&" and "||" in C#)

we_learning_python = True
we_enjoy = True

if we_learning_python and we_enjoy:
    print("<print here some positive motivational message...>")






















