# the game:
# https://www.codingame.com/training/easy/ascii-art

import sys
import math
def string_print(arr,k: int):
    for i in range(len(arr[k])):
        st=""
        for j in range(len(arr[k][i])):
            st+=arr[k][i][j]
        print(st)

l = int(input())
h = int(input())
t = input()
arr = [[["" for k in range(l)] for j in range(h)] for i in range(27)]
for i in range(h):
    row = input()
    j_tag=0
    for k in range(27):
        j=0
        while(j<l):
            arr[k][i][j]=row[j_tag]
            j_tag+=1
            j+=1
t  = t.upper()



for i in range(h):
    st = ""
    for f in range(len(t)):
            if(ord(t[f])<=ord('Z') and ord(t[f])>=ord('A')):
                k = ord(t[f])-ord('A')
                for j in range(len(arr[k][i])):
                    st+=arr[k][i][j]
            else:
                
                for j in range(len(arr[26][i])):
                    st+=arr[26][i][j]
    print(st)

        



