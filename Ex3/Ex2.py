import sys


x = None
f_x = None
f_name = None
def lastcall(func):
    def wrapper(*args, **kwargs):
        global x
        global f_x
        global f_name
        arg = args[0]
        if (f_name is None):
            x = arg
            f_x=func(x)
            f_name = func.__name__
            print(str(f_x))
        elif(arg == x and f_name == func.__name__):
            print("I already told you that the answer is ",str(f_x),"!")
        else:
            x = arg
            f_x=func(x)
            f_name = func.__name__
            print(str(f_x))
        return
    return wrapper


@lastcall
def func_pow2(x:float):
    return x**2

@lastcall
def func_sqrt(x:float):
    return x**(0.5) #if x<0 then return a Complex number

@lastcall
def func_is_even(x:int) -> bool:
    return (x % 2 ==0) #if x<0 then return a Complex number

#-------------------------------------
#MAIN   Q2
#-------------------------------------

if __name__ == "__main__":
    print("--------")
    print("Q2")
    print("--------")
    #Example num 1, pow 2:
    print()
    print("Chack on func_pow2")
    print("--------------------")
    print("Send 2.0:")
    func_pow2(2.0)
    print()

    print("Send again 2.0:")
    func_pow2(2.0)
    print()
    
    print("Send 3.0:")    
    func_pow2(3.0)
    print()

    print("Send 4.0:")
    func_pow2(4.0)
    print()

    print("Send again 4.0:")
    func_pow2(4.0)
    print()

    #Example num 2, sqrt:
    print()
    print("Chack on func_sqrt")
    print("--------------------")
    print("Send 4.0:")
    func_sqrt(4.0)
    print()

    print("Send again 4.0:")
    func_sqrt(4.0)
    print()
    
    print("Send 9.0:")    
    func_sqrt(9.0)
    print()

    print("Send -2.0:")
    func_sqrt(-2.0)
    print()
    print("Send -3.0:")
    func_sqrt(-3.0)
    print()
    print("Send again -3.0:")
    func_sqrt(-3.0)
    print()

    
    #Example num 3, is even?:
    print()
    print("Chack on func_is_even")
    print("--------------------")
    print("Send 4:")
    func_is_even(4)
    print()

    print("Send 2:")
    func_is_even(2)
    print()
    
    print("Send again 2:")
    func_is_even(2)
    print()

    print("Send 9:")    
    func_is_even(9)
    print()

    print("Send 3:")
    func_is_even(3)
    print()

    print("Send 3:")
    func_is_even(3)
    print()

  