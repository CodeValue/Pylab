
# Complex
#------------

# In python, you can put ‘j’ or ‘J’ after a number to make it imaginary, so you can write complex literals easily:

complex_num1 = 1j
complex_num2 = 1J

print(complex_num1 * complex_num2)

# Constructor and methods

complex_num3 = complex(2,3)                 # Constructor will create a complex number
print(complex_num3)
print(complex_num3.real)                    # Get the real part of the number
print(complex_num3.imag)                    # Get the imaginary part of the number 




















# Tuple 
#--------

# An immutable list of values
tup1 = ('DevOps', 'ALM', 1997, 2000);
tup2 = (1, 2, 3, 4, 5);
tup3 = "a", "b", "c", "d";

print(tup1, tup2, tup3)


# Set 
#--------

# An unordered list of uniqe values
my_set = set([1, 1, 4, 16, 3, 4])
print(my_set)           

my_set.add(3)


# Frozenset
#------------

# Same as set but immutable
my_frozenset = frozenset([1, 5, 2, 3, 3, 2, 1])
print(my_frozenset)



