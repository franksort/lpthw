# Assigning a string to a variable.
formatter = "%r %r %r %r"

# Using formatter as a format string for the values...
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# I have no idea why %r or repr() prints strings with quotes around them
# I know repr converts an object to str
# saying fuck it right now.  I'll learn about it later.
