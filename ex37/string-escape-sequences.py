"""
String Escape Sequences
"""

# \\ backslash
print "This is a backslash: \\"

# \' single quote
print "This is a single quote: \'"

# \" double quote
print "This is a double quote: \""

# \a ASCII bell
# I couldn't get this to work.
print "This sound a bell: \a"

# \b ASCII backspace
# replaces the character preceding it with the character after it
print "This should spell whatevr: whateve\br"

# \f ASCII formfeed?  no idea
# starts a new line and indents to the end of the string preceding it.
# ex. this
#         is
#           some
#               formfeeding     
print "this\fis\fsome\fformfeeding"

# \n ASCII newline
print "This will print John on the next line:\nJohn"

# \r ASCII carriage return
# Resets the cursor to the beginning of the line and begins
# overwriting any characters with what follows it.
print "John saw the monolith.\rMary"

# \t ASCII horizontal tab
print "\tThis line is tabbed in 1 tab."

# \v ASCII vertical tab
# Moves a string down one terminal line from its current horizontal position.
print "This will print John two vertical tabs down:\v\vJohn"
