# -*- coding: utf-8 -*-
"""

EXP 6
"""

def merge(a):
    if len(a)>1:
        m=len(a)//2
        L=merge(a[:m])
        R=merge(a[m:])
        a=[]
        while L and R:
            a.append((L if L[0]<R[0] else R).pop(0))
        a+=L+R
        return a
    return a

print(merge([38,27,43,3,9,82,10]))
