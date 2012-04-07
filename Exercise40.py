#preExercise titled Exercise40

from TurtleWorld import *
from math import *

def polygon(n,t,length):
    for i in range(n):
        fd(t, length)
        lt(t,360/n) #turns to the left at angle 360/n degrees

def circle(t,r):
    n=60
    circumference = 2*pi*r
    length = circumference/n #Must fit the right amount of equivalent lengths on the "circle"
    polygon(n,t,length)


def arc(t,r,angle):
    arclength=r*angle*(2*pi/360) #Converts input angle in degrees to radians to calculate arc length
    n=60
    length=arclength/n
    arcangle=float(angle)/n

    for i in range(n):
        fd(t,length)
        lt(t,arcangle)



world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
arc(bob,50,360)



wait_for_user()


