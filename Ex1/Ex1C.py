import sys
from copy import deepcopy
from sympy import *
import numpy as np
EPS=0.000001



#-------------------------------------
#Q3
#-------------------------------------

def find_root(y, x1, x2):
    """
        temp is a tempderived function and yprime is lambda of temp
        return xn -> inf | y < EPS
    """
    x = Symbol('x')
    temp = y(x).diff(x)
    yprime = lambda x: eval(str(temp))
    return "%.3f"%find_root_rec(y, yprime, x1)


def find_root_rec(y, yprime, x0):
    if(yprime(x0)==0):
        return find_root_rec(y, yprime, x0-(y(x0)/(yprime(x0)+EPS)))
    elif(abs(y(x0))<EPS):
        return x0
    else:
        return find_root_rec(y, yprime, x0-(y(x0)/yprime(x0)))



#-------------------------------------
#MAIN
#-------------------------------------

if __name__ == "__main__":
    #q3
    print("Q3:")
    print("__________")

    y1=lambda x: x**2-4
    print("f(x) = x**2-4")
    print(find_root(y1 , 1, 3))
    print()

    print("f(x) = x**2+8*x+16")
    y1=lambda x: x**2+8*x+16
    print(find_root(y1 , -10, 3))    
    print()

    #check if divade by 0 (f'(-1)=0)
    y1=lambda x: x**2+2*x-3
    print("f(x) = x**2+2*x-3")
    print(find_root(y1 , -1, 2))  
    print()
    print()

