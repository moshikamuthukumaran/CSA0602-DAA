# -*- coding: utf-8 -*-
"""

Q25. Linear Search – First Element Detection
"""

a=[55,21,39,47,63,70]
x=55
for i in range(len(a)):
    if a[i]==x:
        print("Found at index",i)
        break

"""Q27. Closest Pair – Real-World Tower Placement Scenario"""

p=[(2,8),(5,6),(9,4),(4,7),(8,3)]
m=999
for i in range(5):
    for j in range(i+1,5):
        d=((p[i][0]-p[j][0])**2+(p[i][1]-p[j][1])**2)**.5
        if d<m:
            m=d
            pair=(p[i],p[j])
print("Closest pair:",pair)
print("Distance:",round(m,2))

"""Q84. Bubble Sort – Repeated Local Inversions"""

a=[26,17,35,29,48,12]
for i in range(5):
    for j in range(5-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
