"""
Researching these keywords can get deep very quickly.

Take the innocent looking global keyword for instance.  In order
to truly understand what global does, a programmer would have to
understand the execution model at:
http://docs.python.org/reference/executionmodel.html which is 
not beginner material.

I don't agree with what Zed is forcing the reader to do here.

and           Ands together two boolean values.
del           Deletes a variable from the local namespace.  It can 
              also delete a slice from a list using the list indices.
              ex. a = [30, 2, 4]
                  del a[0]
from          Used for importing packages/modules.
not           Negates a boolean value.
while         Begins a while loop.
as            Importing a package/module as a certain name.
elif          Else if in an if-statement.
              In an if-statement if "expressions" are evaluated in order.
              The first one that evaluates to True gets its block run.
global        Must be used before a variable is assigned.  Once used it 
              pushes the variable to the global namespace.
or            Ors together two boolean values.
with          Allows you to wrap a piece of code with enter and exit
              operations that are gaurenteed to run.  Opening a file is a
              good example.  When using with, <obj>.__enter__ and
              <obj>.__exit__ are run.
              Ex.  with open("x.txt") as f
                       data = f.read()
                       // do stuff
              Can replace try/catch/finally statements.
              Lots of possibilities.
assert        Assert that an expression is True, exit program if not?
else          In an if-statement, executes a block of code if no if
              or elif evaluates to True
if            Begins an if-statement.
pass          Does nothing.  A null statement that can be used as a place
              holder in your code.
yield         Used to create generators.  NOTE: I have no idea.
break         Breaks out of the closest for or while loop.
except        Exception handling.
import        Brings a Python modules into the current namespace?
print         Prints a string to STDOUT.
class         Creates classes.
exec          Executes Python statements stored in a string.
              ex. exec 'print "Hello"'
              eval evaluates valid Python expressions which are stored
              in a string.
              Know the difference between statements and expressions.
              ex. eval('3*3')   is going to be 9
in            Comparison operator that tests for set membership.
              3 in [3, 4, 5] == True
              Ref: http://docs.python.org/release/2.5.2/ref/comparisons.html
raise         Exception handling.  Raises an exception.
continue      Skips the rest of the instructions in a loop and continue
              with the next iteration of the loop.
finally       Exception handling.  In a try/catch/finally statement
              the block under finally will always execute regardless
              of what exceptino is raised or if an exception is raised
              at all.
is            Comparison operator that checks to see if two objects
              are the same instance.
return        Used in functions to return a value.
              When no return expression is specified (ex. return)
              return None is substituted.
def           Used for defining functions and methods.
for           Used to begin a for loop.
lambda
try           Exception handling.  Begins a try/catch block.

Data Types

True          Boolean True
False         Boolean False
None          None type
strings       "blah", 'whatever'
numbers       3, 3e10, -3
floats        3.0, -4.3
lists         [1, 2, 3, 4], ["something", "else"]
"""
