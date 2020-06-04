import random
l=[random.randint(0, 100) for i in range(10)]
m=min(l)
for i in range(10):
    print(l[i],"\n")
for i in range(10):
    if(m==l[i]):
        j=i
        for j in range(i,0,-1):
            t=l[j]
            l[j]=l[j-1]
            l[j-1]=t
            if(j==1):
                t=l[0]
                l[0]=l[1]
                l[9]=t

for i in range(10):
    print(l[i])