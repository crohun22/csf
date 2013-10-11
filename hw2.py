# Name: Hunter Crook
# Evergreen Login: crohun22
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

from hw2_test import n  #import the variable from the module
t = 0 # t for total

while (n > 0):
    t = n + t    # While "n" is greater than 0, the total will be added to "n"
                 # the porgram will print the current total and then subtract from "n"
    print str(t)
    n = n-1

print "\n"      # I decided to put a break after each section for clarity
###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

d = 11                  # d is the denominator
for i in range (1, d):
    i = 1.0/i           # From 1 to decided number the loop will repeat while 
    print i             # showing the decimal of 1 over said number in loop


print "\n"
###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
tri = 0
for i in range(0, n+1):     # During loop repeat, the program will show a running
    tri = i + tri           # total until the decided times is repeated
    print tri
    
    
print "Triangular number", n, "via loop:", tri
print "Triangular number", n, "via formula:", n*(n+1)/2

print "\n"
###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

n = 5
f = 1
for i in range(1, n+1):         
    f = i * f
    print "when i = " + str(i) + " f = " + str(f)
print "\n"

###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10


for n in range(numlines, 0, - 1):   #this is loop to count from decided number to 1
    f = 1
    for i in range(1, n+1):         #this loop gets the factorial of said number
        f = i * f
    
    print str(f) + " is " + str(n) + "!"
    
print "\n"        
###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

numlines = 10
sums = 0

for n in range(1, numlines+1):
    f = 1
    
    for i in range(1, n+1):
        f = i * f
 
    sums = (1.0/f) + sums  
print sums + 1.0

print "\n"
###
### Collaboration -
###     In Part with what I used from the homework that was given and a very small
###     amount of code given from Stubbycat85
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?

#   The overall time this project took was around approx. 3 hours from lab today
#   and from home time including referencing the book. 
#       The book had much more info that I believe we were told in class but was
#       still easily accessible
