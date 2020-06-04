import random
A=[[random.randint(-5,5) for i in range(3)]for i in range(3)]
print(A)
for i in range(2):
    for j in range(2):
        A[i][j]-=A[2][j]
print(A)