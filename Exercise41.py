#Exercise 4.1 - Building building blocks

from TurtleWorld import *
from math import *

def polygon(n,t,length):
    """Uses a turtle (t) to draw a regular n-sided polygon of
    given segment length (length)
    """
    for i in range(n):
        fd(t, length)
        lt(t,360/n) #turns to the left at angle 360/n degrees

def circle(t,r):
    """Uses a turtle (t) to draw a circle of radius r
    rendered using an approximation of an n-sided regular polygon
    where n is 'very large'
    """
    n=100
    circumference = 2*pi*r
    length = circumference/n #Must fit the right amount of equivalent lengths on the "circle"
    polygon(n,t,length)

def myArc(t,r,angle):   # My solution to constructing an arc. Assuming book's
                        # solution is better, so will be using that.
    n=100
    circumference = 2*pi*r
    length=circumference/n
    for i in range(n*angle/360):  #Say if I want it to go 60 degrees, n must be
        fd(t,length)            #affected by the ratio angle/360)
        lt(t,360.0/n)




def arc(t,r,angle):  #Book's solution
    """Uses a turtle (t) to draw an arc of would-be radius r. Angle is
    specified such that an input of 360 would produce a circle.
    """
    arc_length=r*angle*(2*pi/360) #Converts input angle in degrees to radians to calculate arc length
    n = int(arc_length/3)+1
    step_length = arc_length/n
    step_angle = float(angle)/n

    for i in range(n):
        fd(t,step_length)
        lt(t,step_angle)

def tripoly(t,n,length):
    for i in range(n):
        polygon(3,t,length)
        fd(t,length)
        lt(t,360.0/n)
        

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
myArc(bob,50,176)





wait_for_user()


