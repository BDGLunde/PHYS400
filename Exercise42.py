from TurtleWorld import *
from math import *
from Exercise41 import *

def petal(t, r, angle):
    """Uses a turtle (t) to trace a petal formed by two arcs reflected
    about a common line. The length of these petals is inputted as the radius,
    r. The input angle defines the 'width' of each petal.
    """

    for i in range(2):
        arc(t,r,angle)
        lt(t,180-angle) #turns the turtle around and faces him such that he will return to original point
        #Note that after the second iteration, the turtle will be
        #ready for another petal.

def flower(n,t,r,angle):
    """Uses a turtle (t) to draw a flower inscribed on an 'invisible' circle
    with n petals of specified length and width"""

    for i in range(n):
        petal(t,r,angle)
        lt(t,360.0/n)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001

flower(20,bob,200,20)

wait_for_user()
