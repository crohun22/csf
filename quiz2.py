# From a module called lab2
# import a variable called n
# peint one of the following things:
# "greater than 50"
# "less that 50"
# "equal to 50"
# based on the value of n

from lab2 import n
if n > 50:
    print "n is greater than 50"
elif n < 50:
    print "n is less than 50"
elif n == 50:
    print "n is equal to 50"
else:
    print "n is not a recognizable number"
