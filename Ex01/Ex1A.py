import sys
from copy import deepcopy
from sympy import *
import numpy as np
EPS=0.000001

#-------------------------------------
#Q1
#-------------------------------------
def safe_call(f , x ,y ,z ):
    """
        safe call question
    """
    anno_x = f.__annotations__.get('x')
    anno_y = f.__annotations__.get('y')
    anno_z = f.__annotations__.get('z')
    if((type(x)==anno_x or anno_x == None) and (type(y)==anno_y or anno_y == None) and (type(z)==anno_z or anno_z == None)):
        return f(x,y,z)
    else:
        raise Exception("One of the parameters is wrong")
            

def f1(x: int, y: int, z: float):
    """
        func 1 check for safe call
    """
    return x+y+z

def f2(x: int, y: int, z):
    """
        func 2 check for safe call
    """
    return x+y+z



#-------------------------------------
#MAIN
#-------------------------------------

if __name__ == "__main__":
    #q1
    print("Q1:")
    print("__________")

    try:
        print("Check 1 exeption: f1(x: int, y: int, z: float)")
        print("Send: (f1 , 5, 6, 7)")
        print(safe_call(f1 , 5, 6, 7)) 
    except Exception as e:
        print("1 currect exeption int is not float")
    print()
    print()
    try:
        print("Check 2 exeption: f1(x: int, y: int, z: float)")
        print("Send: (f1 , 5, 6.0, 7.0)")
        print(safe_call(f1 , 5, 6.0, 7.0)) 
    except Exception as e:
        print("2 currect exeption int is not float")
    print()
    print()
    try:
        print("Check 3 ok: f1(x: int, y: int, z: float)")
        print("Send: (f1 , 5, 6, 7.0)")
        print(safe_call(f1 , 5, 6, 7.0)) 
    except Exception as e:
        print("not need to be exeption")
    print()
    print()
    try:
        print("Check 4 ok: f2(x: int, y: int, z)")
        print("Send: (f2 , 5, 6, 7)")
        print(safe_call(f2 , 5, 6, 7)) 
    except Exception as e:
        print("not need to be exeption")

