import random
a=[random.randint(-5,5) for i in range(5)]
for i in range(5):
    k=0
    for j in range(-5,5):
        if(a[i]==j):
            k+=1
    print(a[i],k)