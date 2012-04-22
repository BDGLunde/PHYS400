#Exercise 7.5, Computing pi

from math import *

def estimate_pi():
    """Uses the infinite series constructed by Srinivasa to numerically approximate
    pi. The infinite series is evaluated in the while loop starting at k = 0. Sum and term
    are initialized to zero outside of the loop. Once inside, each term is calculated for a given k
    and is added to the previous sum. k is then incremented by 1. The loop terminates when the new term
    becomes smaller than our threshhold.
    """
    
    term = 0.01 
    sum = 0.0
    k = 0.0
    while term>0.0000000000001:
        term = (factorial(4*k)*(1103 + 26390.0*k))/(((factorial(k))**2)*(396.0**(4*k)))
        sum = sum + term
        k=k+1

    inverse =((2.0*sqrt(2))/9801)*sum
    return 1.0/inverse



print estimate_pi()
print pi
print estimate_pi() - pi
