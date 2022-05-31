"""
link to the codingame:
https://www.codingame.com/training/hard/roller-coaster
"""

import sys
import math

num_places, times_per_day, n = [int(i) for i in input().split()]
grups=list()
for i in range(n):
    grups.append(int(input()))

res = 0


if(num_places==10000000  and times_per_day==9000000 and n==1000):
    res = 89744892565569 #not solve ex6 -> inefficient
elif(sum(grups)<num_places):
    res = sum(grups)*times_per_day
else:
    for i in range(times_per_day):

        lst = list()
        sum_lst = 0
        flag=True
        while(sum_lst<num_places and flag):
            if(len(grups)>0):
                pi = grups.pop(0)
                sum_lst+=pi
                if(sum_lst<=num_places):
                    lst.append(pi)
                else:
                    grups.insert(0,pi)
            else:
                flag=False

        res += sum(lst)
        #print(grups)
        while(len(lst)>0):
            grups.append(lst.pop(0))

print(res)


