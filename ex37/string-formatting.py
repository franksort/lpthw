print """
From docs.python.org/release/2.6.7/library/stdtypes.html
about the string format function:

"This method of string formatting is the new standard in
Python 3.0, and should be preferred to the % formatting
described in String Formatting Operations in new code."

The language specification for format specifiers is:

format_spec ::= [[fill]align][sign][#][0][width][.precision][type]
fill        ::= <a char. other than '}'>
align       ::= "<" | ">" | "=" | "^"
sign        ::= "+" | "-" | " "
width       ::= integer
precision   ::= integer
type        ::= "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" |
                "o" | "s" | "x" | "X"

Python 2.7 added support for the thousands comma seperator:
format_spec ::= [[fill]align][sign][#][0][width][,][.precision][type]

"""
print "b Binary"
print "Formats the number in binary."
print "{0:b}".format(34)
print
print "c Character"
print "Converts the number to the cooresponding unicode character"
print "before printing."
print "{0:c}".format(88)
print 
print "d Decimal Integer"
print "{0:d}".format(34)
print
print "e Exponent notation"
print "Prints the number in scientific notation using the letter"
print "'e' to indicate the exponent."
print "{0:e}".format(3000)
print
print "E Exponent notation."
print "Same as 'e' except it uses an upper case 'E'."
print "{0:E}".format(3000)
print
print "f Fixed Point"
print "Displays the number as a fixed-point number."
print "When using 'f', [precision] specifies the number of digits"
print "after the decimal point."
print "{0:f}".format(3000)
print
print "F Fixed Point"
print "Same as 'f'."
print "{0:F}".format(3000)
print
print "g General Format"
print "For a given precision (p >= 1), this sounds the number to p"
print "signifigant digits and then formats the result in either fixed-point"
print "format or in scientific notation, depending on its magnitude."
print "When using 'g', precision specifies the number of digits"
print "before and after the decimal point."
print "{0:0.6g}".format(32.839247382)
print 
print "G General Format"
print "The same as 'g' except uppercase E is used for scienfitic notation."
print "The representations of infinity and NaN are uppercased too."
print "{0:0.6G}".format(32.839247382)
print
print "n Number"
print "Same as 'd' except uses commas according to the current locale"
print "settings."
print "{0:n}".format(300000)
print
print "o Octal Format"
print "Base 8"
print "{0:o}".format(64)
print
print "s String Format"
print "Default for strings.  May be omited."
print "{0:s}".format("a wild string appear!")
print
print "x Hex Format"
print "Base 6"
print "{0:x}".format(14)
print
print "X Hex Format"
print "Base 6, uppercase letters."
print "{0:X}".format(14)
print
print "% Percent"
print "Multiplies by 100"
print "{0:1.2%}".format(0.03)


"""
Zed's list includes 'i' and 'u' which are part of the old %-notation for
string formatting but not supported by str.format().

%i is a signed integer.
%u is deprecated, synonymous with 'd'
"""
