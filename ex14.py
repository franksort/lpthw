# EC 1: Read a bit about Zork on Wikipedia.
# It was for the PDP-10 at MIT which I remember reading about
# in Hackers by Steven Levvy.
# I'm not going to play it though.
from sys import argv

# EC 3
script, user_name, password = argv
prompt = '>>> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few question."
# EC 3
print "Your password is %s.  Remember it." % password
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

# EC 4: Using a multi-line string as a format string and printing it
# seems intuitive to me.
print """
Alright, so you said %r about liking me.
You live in %r.  Not sure where that is.
And you have %r ocomputer.  Nice.
""" % (likes, lives, computer)
