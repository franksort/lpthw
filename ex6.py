# String formatting operations
#
# % is a string operator (in this case)
# the left hand side is the format
# the right hand side contains the value(s)
# % in the format is the start of a format specifier
# http://docs.python.org/library/stdtypes.html#string-formatting-operations

# the format specifier %d is replaced with 10 and formatted as a 
# decimal integer.  the contents of the entire string are then assigned
# to the variable x
x = "There are %d types of people." % 10
# The string binary is assigned to the variable named binary.
binary = "binary"
# The string don't is assigned to the variable named do_not
do_not = "don't"
# EC2 string is put inside a string #1
# EC3 really two strings are put into the format string
y = "Those who know %s and those who %s." % (binary, do_not)

# Simple printing of variables.
print x
print y


print "I said: %r." % x # EC2 string is put inside a string #2
print "I also said: '%s'." % y # EC2 string is put inside a string #3

# Assigning boolean to variable.
hilarious = False
# joke_evaluation is a format string
joke_evaluation = "Isn't that joke so funny?! %r"

# the format specifier in joke_evaluation is replaced by the string value
# of hilarious and formatted according to the format specifier's options
print joke_evaluation % hilarious # EC2 string is put inside a string #4

# Assignment strings to variables.
w = "This is the left side of..."
e = "a string with a right side."

# Since both variables are string objects, the + operator 
# concats them together (notice, no spaces)
# EC4 ^
print w + e
