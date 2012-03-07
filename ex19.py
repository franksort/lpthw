# Reviewed the difference between parameter and argument.
#
# A "formal parameter" is a reference the actual argument being passed
# into a function.  When you define a function, you specify a formal
# paramaters if any.
# 
# "Actual parameters" are values passed into a function.

# The following line defines a function named 'cheese_and_crackers'
# with formal parameters 'cheese_count' and 'boxes_of_crackers'.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # The following lines use format strings to print out
    # the arguments supplied to this function.  Plus some 
    # simple print statements.
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"

# Printing a string.
print "We can just give the function numbers directly:"
# Calling the function cheese_and_crackers with arguments 20 and 30.
cheese_and_crackers(20, 30)


# Printing a string.
print "OR, we can use variables from our script:"
# Assigning integers to variables.
amount_of_cheese = 10
amount_of_crackers = 50

# Calling the function cheese_and_crackers with arguments
# amount_of_cheese and amount_of_crackers which are variables
# containing 10 and 50 respectively.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Printing a string.
print "We can even do math inside too:"
# Calling the function cheese_and_crackers with mathematical expressions
# as arguments.  The first evaluates to 30, while the second evaluates to
# 11.
cheese_and_crackers(10 + 20, 5 + 6)


# Printing a string.
print "And we can combine the two, variables and math:"
# Calling the function cheese_and_crackers with the expression
# amount_of_cheese + 100, which evaluates to 110 since amount_of_cheese
# contains the value 10 and 10 + 100 = 110.  Similar story with
# amount_of_crackers + 1000.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
