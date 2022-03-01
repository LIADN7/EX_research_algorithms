import sys
from copy import deepcopy
from sympy import *
import numpy as np
import operator

EPS=0.000001


#-------------------------------------
#Q2
#-------------------------------------

def print_sorted(arr):
    """
        sordet in d level
    """
    temp_x = deepcopy(arr)
    return print_sortedRec(temp_x)


def print_sortedRec(arr):
    """
        if list or tuple sort else if set or dict sorted by key and go next, else is a 1 val
    """

    if(isinstance(arr, set) or isinstance(arr, dict)):
        temp_x = dict(sorted(arr.items()))
        for key,val in arr.items():
            if(isinstance(val, list) or isinstance(val, tuple)):
                arr[key] = val.sort()
            elif(isinstance(val, set) or isinstance(val, dict)):
                temp_x[key] = print_sortedRec(val)
        arr = deepcopy(temp_x)
        return arr
    else:
        return arr

#-------------------------------------
#MAIN
#-------------------------------------

if __name__ == "__main__":
    #q2
    print("Q2:")
    print("__________")
    arr = {"a": 5, "c": 6, "b": [1, 3, 2, 4]}
    print("The arr number 1 (2d): "+str(arr))
    print("Sorted arr: "+str(print_sorted(arr)))
    print()

    arr = {"a": 5, "c": 6, "b": {1: [2,1], 3: [2,1], 2: [2,1], 4: [2,1]}}
    print("The arr number 2 (2d): "+str(arr))
    print("Sorted arr: "+str(print_sorted(arr)))
    print()

    arr = {"a": 5, "c": {"A": [2,1], "R": [1,2], "C": [2,1], "B": [2,1]}, "b": {1: [2,1], 3: [2,1], 2: [2,1], 4: [2,1]}}
    print("The arr number 3 (3d): "+str(arr))
    print("Sorted arr: ")
    print(str(print_sorted(arr)))
    print()

    arr = {"a": {"a": {"a": {"a": {"b": [1, 3, 2], "a": ["b", "h", "a"]}}}}}
    print("The arr number 4 (5d): "+str(arr))
    print("Sorted arr: "+str(print_sorted(arr)))
    print()

    print()
    print()

