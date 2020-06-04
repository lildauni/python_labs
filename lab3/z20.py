def isPower5(a):
    for i in range(10):
        if (a == 5 ** i):
            return True
import random
a=[random.randint(0,1000) for i in range(10)]
k=0
for i in range(10):
    if(isPower5(a[i])==True):
        k+=1
print(k)

