# Importing module argv from sys module.
# Am I saying that right?  Maybe sys is a package and argv is just a
# function?  Save this for later.
from sys import argv

# Assigning script, input_file to the argument variables.
script, input_file = argv

# Defining a function named print_all with formal paramter f,
# which is to be a file object.
def print_all(f):
    print f.read()

# Defining a function named rewind with formal parameter f,
# which is to be a file object.
def rewind(f):
    # The seek method of a file object moves the file position by n bytes.
    # In this case, it's moved to the beginning of the file.
    f.seek(0)

# Defining a function print_a_line which have two formal parameters:
# line_count is a line number of the file object f.
# f is a file object.
def print_a_line(line_count, f):
    # Prints line_count and the next line of a file object f.
    print line_count, f.readline()

# Creates a file object from input_file using the open function.
current_file = open(input_file)

# Printing a string.
print "First let's print the whole file:\n"

# Calling the print_all function, with the value of current_file
# as an actual argument.
print_all(current_file)

# Printing a string.
print "Now let's rewind, kind of like a tape."

# Calling the rewind function with the value of current_file as
# an actual argument.
rewind(current_file)

# Printing a string.
print "Let's print three lines:"

# Assigning the interger 1 to current_line.
current_line = 1
# Calling the print_a_line function with the values of 
# current_line and current_file as actual arguments.
print_a_line(current_line, current_file)

# Incrementing the value of current_line by 1.
current_line = current_line + 1
# Calling the print_a_line function with the values of 
# current_line and current_file as actual arguments.
print_a_line(current_line, current_file)

# Incrementing the value of current_line by 1.
current_line = current_line + 1
# Calling the print_a_line function with the values of 
# current_line and current_file as actual arguments.
print_a_line(current_line, current_file)
