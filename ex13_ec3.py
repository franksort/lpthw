from sys import argv

script, fn, ln = argv

print "Hello %s %s!" % (fn, ln)
color = raw_input("What's your favorite color? ")
day = raw_input("What's your favorite day of the week? ")
print "I hope you have a %s %s." % (color, day)
