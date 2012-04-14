from TurtleWorld import *
from math import *
from Exercise41 import *


def tri(t,length,angle):
    b=length*sin(angle/2*pi/180)
    rt(t,angle/2)
    fd(t,length)
    lt(t,90+(angle/2))
    fd(t,2*b)
    lt(t,90+(angle/2))
    fd(t,length)
    lt(t,180-(angle/2))

def tripie(n,t,length):
    angle = 360.0/n
    for i in range(n):
        tri(t,length,angle)
        lt(t,angle)
            

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.1

tripie(6,bob,100)

    

