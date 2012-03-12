def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

# EC1
def hello_generator(times):
    return "hello" * times
hellos = hello_generator(3)
print hellos

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

# EC2
# EC3 changed it
what_verify = (height - ((iq / 2) + weight)) + age
print "Verifying value of puzzle: %d" % what_verify

# EC3 changed it
what = add(age, subtract(height, add(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"


# EC4: (2 + 3) * 20
ec4 = multiply(add(2, 3), 20)
print "ec4 = %d" % ec4



