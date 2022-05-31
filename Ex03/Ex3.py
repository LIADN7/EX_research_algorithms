
from sklearn.utils import resample


class List(list):
    def __init__(self, *args):
        self.arr = []
        if(len(args)<1):
            return
        for i in args:
            if(not isinstance(i, list)):
                raise Exception("this not a list!!!")
            self.arr.append(i)

    def __getitem__(self, *args):
        res=self.arr
        
        for i in args[0]:
            res = res[i]
            
        return res

    def __append__(self, *args):
        if(len(args)<1):
            return
        for i in args:
            if(not isinstance(i, list)):
                raise Exception("this not a list!!!")
            self.arr.append(i)

    def append(self, *args):
        if(len(args)<1):
            return
        for i in args:
            if(not isinstance(i, list)):
                raise Exception("this not a list!!!")
            self.arr.append(i)
    
    def remove(self, num: int) -> None:
        return self.arr.pop(num)
        
    def __str__(self):
        return str(self.arr)



#-------------------------------------
#MAIN   Q3
#-------------------------------------

if __name__ == "__main__":
    print()
    print("--------")
    print("Q3")
    print("--------")
    a = List(["L","i","a","d"],["N","a","g","i"],["L","i","s","t"])
    print("First init List")
    print(a)
    print()
    print("Append list of [[0,1,2,[0,'Liad Nagi list']],1,2]")
    a.append([[0,1,2,[0,"Liad Nagi list"]],1,2])
    print(a)
    print()
    print("Get [3,0,3,1]")
    print(a[3,0,3,1])
    print()
    print("Remove the 0 from the List")
    a.remove(0)
    print(a)
    print()
