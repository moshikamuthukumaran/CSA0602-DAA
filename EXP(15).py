# -*- coding: utf-8 -*-
"""

EXP 15
"""

from math import sqrt

p=[(1,2),(4,5),(7,8),(3,1)]
d=999

for i in range(len(p)):
    for j in range(i+1,len(p)):
        x=(p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2
        if x<d:
            d=x
            pair=(p[i],p[j])

print("Closest pair:",pair)
print("Distance:",sqrt(d))
