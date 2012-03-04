tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# Using ''' as a triple quote
# EC 2: Not sure why I'd want to use that 
# unless it's to print three normal quotes in a row.
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# EC 4
somevar = "this str has \"double quote\" and \'single quote\' escapes"
# This print statement shows the escape characters for the
# single quotes but not the double quotes.  Strange.
# It also prints single quotes around the string.
print "%r" % somevar
# This statement doesn't show any escape characters.
print "%s" % somevar
