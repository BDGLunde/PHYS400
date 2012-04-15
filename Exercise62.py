#Exercise 6.2 - Scaffolding code (Example is hypotenuse function)

from math import *


# def hypotenuse(legA,legB):
#   print 'leg A is', legA
#   print 'leg B is', legB


# def hypotenuse(legA,legB):
#   print 'leg A is', legA
#   print 'leg B is', legB
#   cSquared = legA**2 + legB**2
#   print 'C squared is', cSquared

def hypotenuse(legA,legB):
    """Takes two float values for the first and second leg of a right triangle
    and returns the length of its hypotenuse using the Pythagorean theorem
    """
    cSquared = legA**2 + legB**2
    c = sqrt(cSquared)
    return c

print hypotenuse(3,4)
