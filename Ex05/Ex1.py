
import itertools


def  bounded_subsets(lst: list(), c: int):
    flag=1
    lst.sort()
    
    while(flag and len(lst)>0):
        a=lst.pop()
        if(a<=c):
            flag=0
            lst.append(a)
       
    iter_subsets = iter(list(s) for i in range(len(lst), 0, -1)
            for s in itertools.combinations(lst, i)
            if sum(s) <= c)
    #print(str(iter_subsets))
    
    return iter_subsets

if __name__ == "__main__":
    a = bounded_subsets([1,2,3], 4)
    print()
    print("ex1 - bounded_subsets([1,2,3], 4)")
    print("name of the iterator: "+str(a))
    print("his values:")
    for i in a:
        print(i)
    lst =  [1]+[10]*1000000
    a = bounded_subsets(lst, 9)
    print()
    print("ex2 - bounded_subsets(lst, 9) | lst = [1]+[10]*10000000")
    print("name of the iterator: "+str(a))
    print("his values:")
    for i in a:
        print(i)
    lst =  [6,5,4,3,2,1]
    a = bounded_subsets(lst, 6)
    print()
    print("ex3 - bounded_subsets(lst, 6) | lst = [6,5,4,3,2,1]")
    print("name of the iterator: "+str(a))
    print("his values:")
    for i in a:
        print(i)