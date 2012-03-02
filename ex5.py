name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_cm = height * 2.54 # height in cm
weight = 180 # lbs
weight_kg = weight / 2.2
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# %d, %s, %f, etc... are called format specifiers
# according to www.python.org/dev/peps/pep-3101
print "Let's talk about %r." % name
print "He's %d inches or %d centimeters tall." % (height, height_cm)
print "He's %d pounds or %d kilograms heavy." % (weight, weight_kg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
