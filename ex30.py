"""
EC1
elif evaluates its expression and executes its body if the preceding
if-statement does not evaluate to True.
else executes its body if none of the if- or elif-statements evaluate to True

"""
# Assigning numbers to variables
people = 10 
cars = 30
buses = 8

# The greater than operator is a comparison operator that compares the 
# values of cars and people.  The value of cars is greater than the value
# of people therefore that expression evaluates to True.  The if-statement
# executes its body since this expression is True.
# And that explanation is enough for the rest of this program.
if cars > people:
    print "We should take the cars." # EC2 will run
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses." # EC2 will run
else:
    print "We still can't decide."

if people > buses:
    print "Alright, let's just take the buses." # EC2 will run
else:
    print "Fine, let's stay home then."


# EC3
if cars > people and buses < cars:
    print 'Whatever man.'
