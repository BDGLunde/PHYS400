#Exercise 4.2 - Flowers

# Build petals, then flowers.
# For each petal, we essentially want to create an arc and then have it reverse.

from TurtleWorld import *
from math import *
from Exercise41 import *

def petal(t,r,angle):  # After testing petal individually using arc and myArc, it's evident that the book's version is cleaner at the petal tips.
    """Uses a turtle (t) to trace a petal formed by two arcs reflected
    about a common line. The length of these petals is inputted as the radius,
    r. The input angle defines the 'width' of each petal.
    """
    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle) #turns the turtle around and faces him such that he will return to original point
        #Note that after the second iteration, the turtle will be
        #ready for another petal. Use geometry at the turning point to see why this is the correct angle to use
        
def flower(n,t,r,angle): #Creates a flower of n petals
    """Uses a turtle (t) to draw a flower inscribed on an 'invisible' circle
    with n petals of specified length and width"""
    for i in range(n):
        petal(t,r,angle)
        lt(t,360.0/n)

        

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

flower(10,bob,150,70)

wait_for_user()
