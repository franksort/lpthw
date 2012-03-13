"""
EC 1
The if-statement runs the code underneath it if the boolean expression
evaluates to True

EC 2
The code under an if-statement needs to be indented 4 spaces as
this is the way Python interprets a block of code.  Instead of curly
braces, Python relies on indentation.

EC 3
If an if-statement's body isn't indented it's not considered part of an
the if-statement at all.

EC 4
Sure you can.

EC 5
If you change the variables then the comparisons in the if-statements
will evaluate differently possibly producing a different boolean value.

"""

# EC4
if 'sky' == 'tree':
    print 'The world is insane.'

if 'sky' == 'sky':
    print 'Sanity restored.'

people = 20
cats = 30
dogs = 15


if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"


dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."


if people == dogs:
    print "People are dogs."
