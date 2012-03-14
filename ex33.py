
# EC 1, 2
def fill(upto, step=1):
    """Fill a list with numbers upto a limit."""
    i = 0
    numbers = []
    while i < upto:
        numbers.append(i)
        i += step
    return numbers

numlist = fill(7, 2) 
print numlist

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num
