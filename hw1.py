# Name: Hunter Crook
# Evergreen Login: crohun22
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

A = 1
B = -5.86
C = 8.5408


X1 = (-B + math.sqrt((B*B) - (4*A*C))) / (2*A)

X2 = (-B - math.sqrt((B*B) - (4*A*C))) / (2*A)

print "For X when A = " + str(A) + " when B = " + str(B) + " and when C = " + str(C)
print str(X1)
print str(X2)
###
### Problem 2
###

print "Problem 2 solution follows:"

from hw1_test import a, b, c, d, e, f

print str(a)
print str(b)
print str(c)
print str(d)
print str(e)
print str(f)


###
### Problem 3
###

print "Problem 3 solution follows:"

z = (a*b) + ((-c) * -(d+e+f))

print str(z)
###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
