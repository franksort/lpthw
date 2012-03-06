# EC1: I feel I understand it.
# file.truncate() is not necessary since creating a file object
# with the write argument wipes the file.
# From pydoc file:
#   The file will be created if it doesn't exist
#   when opened for writing or appending; it will be truncated when
#   opened for writing.
# The above explanation also covers EC5.
# EC4, without an argument, open defaults to 'r' or read.
from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file.  Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# EC3
target.write("%s\n%s\n%s\n" % (line1, line2, line3))

print "And finally, we close it."
target.close()
