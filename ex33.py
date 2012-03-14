
# EC 1
def fill(upto):
    """Fill a list with numbers upto a limit."""
    i = 0
    numbers = []
    while i < upto:
        numbers.append(i)
        i += 1
    return numbers

numlist = fill(7)
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
