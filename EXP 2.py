# -*- coding: utf-8 -*-
"""

EXP 2
"""

def bs(a,l,r,x):
    if l>r:return -1
    m=(l+r)//2
    if a[m]==x:return m
    if x<a[m]:return bs(a,l,m-1,x)
    return bs(a,m+1,r,x)

a=[5,10,15,20,25]
x=20
print("Key found at index",bs(a,0,len(a)-1,x))
