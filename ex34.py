# Accessing items in a list

# EC 1
# 
# Ordinal Number
# Specifies the position of an element in an ordered set. (Math)
# 
# Cardinal Number
# The real definition is lengthy and not all that necessary to 
# the proper use of a Python lists.  Just remember Python lists 
# start at 0.

# EC 2
# Dates are in order, using Ordinal Numbers.

# Why do arrays usually start with 0?
# Dijkstra gives us a mathematical argument as to why they *should*.
# http://www.cs.utexas.edu/users/EWD/transcriptions/EWD08xx/EWD831.html

# C arrays just reference memory address offsets.
# So array[0] is the memory address of the array + 0.
# array[1] is the memory location of the array + 1
# Something like that.

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

"""
1. The animal at index 1 is the 2nd animal and is a python.
   The 2nd animal is at index 1 and is a python.

2. The 3rd animal is at index 2 and is a peacock.
   The animal at index 2 is the 3rd animal and is a peacock.

3. The 1st animal is at index 0 and is a bear.
   The animal at index 0 is the 1st animal and is a bear.

4. The animal at index 3 is the 4th animal and is a kangaroo.
   The 4th animal is at index 3 and is a kangaroo.

5. The 5th animal is at index 4 and is a whale.
   The animal at index 4 is the 5th animal and is a whale.

6. The animal at index 2 is the 3rd animal and is a peacock.
   The 3rd animal is at index 2 and is a peacock.

7. The 6th animal is at index 5 and is a platypus.
   The animal at index 5 is the 6th animal and is a platypus.

8. The animal at 4 is the 5th animal and is a whale.
   The 5th animal is at index 4 and is a whale.
"""

guesses = ['python',
           'peacock',
           'bear',
           'kangaroo',
           'whale',
           'peacock',
           'platypus',
           'whale']

def get_animal_by_cardinal_number(number, animals):
    return animals[number-1]

print 1, animals[1], guesses[0]
print 2, get_animal_by_cardinal_number(3, animals), guesses[1]
print 3, get_animal_by_cardinal_number(1, animals), guesses[2]
print 4, animals[3], guesses[3]
print 5, get_animal_by_cardinal_number(5, animals), guesses[4]
print 6, animals[2], guesses[5]
print 7, get_animal_by_cardinal_number(6, animals), guesses[6]
print 8, animals[4], guesses[7]
