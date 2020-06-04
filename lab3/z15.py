import random
A=[[random.randint(-5,5) for i in range(3)]for i in range(3)]
print(A)
a=A[0][0]*A[1][1]*A[2][2]+A[1][0]*A[1][2]*A[2][0]+A[1][0]*A[2][1]*A[0][2]-A[2][0]*A[1][1]*A[0][2]-A[0][0]*A[2][1]*A[1][2]-A[1][0]*A[0][1]*A[2][2]
print(a)
