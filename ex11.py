# EC 1: raw_input() reads a line from the input, converts it
# to a string (stripping the newline), and returns it.  
# It can also take an argument which serves as a prompt.
# From docs.python.org/library/functions.html#raw_input

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# EC 2
day = raw_input("What day is it? ")
print "You said that it is %s" % day

# EC 3
print "What's your favorite color?"
color = raw_input(">> ")
print "What's your favorite song?"
song = raw_input(">> ")

print "Your favorite color is %s." % color
print "Your favorite song is %s." % song

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# EC 4
# Still unclear about raw formatting strings.
# What's going on behind the scenes?
# What are they used for besides debugging?
# Are they useful for debugging?  I don't recall using them.
