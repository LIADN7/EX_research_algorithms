import matplotlib.pyplot as plt
import numpy as np
import cvxpy as cp
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

EPS=0.1


def plotIntersection(pl, f, g ):

    #Check when f(x)-g(x)=0
    y1 = lambda x: f(x) - g(x)
    start = int(pl.min())
    end = int(pl.max())+1
    arr_x = list()
    for i in range(start,end):
        s = float(format(fsolve(y1, i)[0], ".3f"))
        if s not in arr_x:
            arr_x.append(s)
    #build all the f(x) ("y")
    arr_y = list()
    for i in arr_x:
        s = float(format(f(i), ".3f"))
        arr_y.append(s)
    
    # Get all the points were f(x0)=g(x0) and in the range of <- x ->
    arr_true_x = list()
    arr_true_y = list()
    for i in arr_x:
        fx = f(i)
        gx = g(i)
        if ((fx>=gx-EPS and fx<=gx+EPS) and (i<=end and i>=start)):
            arr_true_x.append(i)
            arr_true_y.append(gx)



    print("x = ", arr_true_x)
    print("y = ", arr_true_y)
    # Plot the graphs and the cutting points
    plt.plot(pl, f(pl))
    plt.plot(pl, g(pl))
    for i,j in zip(arr_true_x, arr_true_y ):
        plt.plot(i, j, color='blue', marker='o', markerfacecolor='blue')    
    plt.xlabel("X -->")
    plt.ylabel("Y -->")
    plt.title("f(x)")
    plt.show()
    



#-------------------------------------
#MAIN
#-------------------------------------

if __name__ == "__main__":

    #Example 1 : f(x) = x^2 g(x) = x+10
    f = lambda x: x**2
    g = lambda x: x+10
    p = np.linspace(-10, 10, 1000)
    plotIntersection(p, f, g)

    #Example 2 : f(x) = sin(x) g(x) = 0.2*x    
    f = lambda x: np.sin(x)
    g = lambda x: 0.2*x
    p = np.linspace(-10, 10, 1000)
    plotIntersection(p, f, g)
    
    #Example 3 : f(x) = sin(x) g(x) = cos(x)    
    f = lambda x: np.sin(x)
    g = lambda x: np.cos(x)
    p = np.linspace(-11, 11, 1000)
    plotIntersection(p, f, g)
    
    #Example 4 : f(x) = x**3-(7*(x**2))+6 g(x) = -2*x    
    f = lambda x: x**3-(7*(x**2))+6
    g = lambda x: -2*x
    p = np.linspace(-4, 7, 100)
    plotIntersection(p, f, g)

