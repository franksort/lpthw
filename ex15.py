# From the sys module, import argv (argument variable function)
from sys import argv

# Use argv to get the command arguments (the first one being
# the name of the script)
script, filename = argv

# Creating a file object and storing it in the txt variable.
txt = open(filename)

# Use a format string to print the filename.
print "Here's your file %r:" % filename
# Running the read() method on the file object txt
# to get the contents of the file.
print txt.read()

# Printing a string.
print "Type the filename again:"

# Using raw_input to read a string from stdin with a the prompt
# being "> "
file_again = raw_input("> ")

# Creating a file_object from file_again and storing it in txt_again
txt_again = open(file_again)

# Using the read() method of the file object txt_again to 
# return the contents of the file and printing it.
print txt_again.read()

# EC 3
# This is how a function is typically defined.
def something(somearg):
    """This is a docstring telling you about the function."""
    print "This is a function and the argument is: %r" % somearg

# Here's one with a multi-line docstring according to PEP 0257
def something_else(somearg):
    """This is a function
    that does something about whatever.
    """
    print "Some function and here's the arguments: %r" % somearg

# Calling the function:
something("hello")

# Calling the other function:
something_else("hi")
