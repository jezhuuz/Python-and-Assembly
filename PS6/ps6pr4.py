#
# Jenna Zhu
# jennazhu@bu.edu
#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# Estimating the value of pi
#
# Computer Science 111    
#

import random  
import math


def throw_dart():
    """ Simulates the throwing of a random dart at a 2 x 2 square that.
        is centered on the origin. Returns True if the dart hits a circle
        inscribed in the square, and False if the dart misses the circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)

    if x**2 + y**2 <= 1.0:
        return True
    else:
        return False

### PUT YOUR WORK FOR PROBLEM 4 BELOW. ###

### IMPORTANT NOTES:
###  - One of your functions must use a for loop, and the other function 
###    must use a while loop. You should decide which type of loop is 
###    more appropriate for each function.
###
###  - Each function must call throw_dart() from inside its loop. 
###    For full credit, each function must have *EXACTLY ONE* line of
###    code that calls throw_dart(). If a given function has fewer 
###    or more than one line of code that calls throw_dart(), you 
###    will lose points. 
###
###    In addition, your functions must *NOT* make their own calls 
###    to random.uniform(), and you will lose points if they do so.


def est_pi1(n):
    ''' takes a positive integer n and returns an estimate of pi that is based
        on n randomly thrown darts
    '''
    t = 1
    hits = 0
    pi = 0
    
    for t in range(1,(n+1)):
        
        if throw_dart() == True:
            hits += 1
       
        pi = (hits * 4) / t
        print(hits, "hits out of", t, "throws so that pi is", pi)
        
    return pi


def est_pi2(error):
    ''' takes positive floating-point input error and returns the number of dart throws
        needed to produce an esetimate of pi that is less than error away from the "actual"
        value of pi
    '''

    t = 0
    hits = 0
    pi = 4
    difference = pi - math.pi
    
    while (difference > error):
        
        t += 1
        
        if throw_dart() == True:
            hits += 1
            
        pi = (hits * 4) / t
        #print(pi)
        print(hits, "hits out of", t, "throws so that pi is", pi)
        difference = pi - math.pi
        #print(difference)
        
    return t
