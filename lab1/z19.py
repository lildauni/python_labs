import math
a=1
b=5
c=6
d=b*b-4*a*c
x1=(-1*b-math.sqrt(d))/(2*a)
x2=(-1*b+math.sqrt(d))/(2*a)
if x1>x2:
    print(x2,x1)
else:
    print(x1,x2)