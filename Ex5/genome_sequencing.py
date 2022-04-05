# https://www.codingame.com/training/hard/genome-sequencing

# Help source
# https://www.xarg.org/puzzle/codingame/genome-sequencing/


import sys
import math
from itertools import permutations



n = int(input())
lst=[]
for i in range(n):
    lst.append(input())

# list of all the permotation
lst2 = list(permutations(lst))


min_len = 60
for cur in lst2:
    st = cur[0]
    for i in range(1, len(cur)):
        j = 0
        while j < len(st):
            sub_st = cur[i]
            # check if the sub_st is contained in st
            if st.find(sub_st) != -1:
                break
            # check if there is a partial match
            if st[j:] == sub_st[:len(st) - j]:
                st += sub_st[len(st) - j:]
            j += 1
        # if there is no match
        if j == len(st):
            st += sub_st
    min_len = min(min_len, len(st))

print(str(min_len))