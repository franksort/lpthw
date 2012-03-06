# EC is about pydoc.
# Interesting that pydoc can spawn a webserver and serve the Python docs.
# Useful if you're connection is knocked out.

# I looked up some modules with pydoc but didn't read them line for line.

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
