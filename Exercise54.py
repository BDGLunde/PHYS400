#Exercise 5.4 - Koch Curves and Snowflakes!

from TurtleWorld import *
from math import *

def kochCurve(t,length):
    """Uses a turtle from TurtleWorld to draw a Koch curve of a certain length"""
    angle = 60
    if length < 3:
        fd(t,length)
    else:
        kochCurve(t,length/3.0)
        lt(t,angle)
        kochCurve(t,length/3.0)
        rt(t,angle*2)
        kochCurve(t,length/3.0)
        lt(t,angle)
        kochCurve(t,length/3.0)

def snowflake(t,length):
    """Draws three kochCurves such that they outline a snowflake"""
    for i in range(3):
        kochCurve(t,length)
        rt(t,120)            #3*120 = 360

        
world = TurtleWorld()
bob = Turtle()
pu(bob)
bk(bob,80)
pd(bob)
bob.delay = 0.0001
snowflake(bob,220)

        
    

wait_for_user()






