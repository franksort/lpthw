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
