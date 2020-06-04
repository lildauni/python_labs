import random
n=int(input())
A=[random.randint for i in range(n)]
def MaxElem(A,n,max):
    if(A[n]>max):
        max=A[n]
    if(n==0):
        return max
    else:
        return MaxElem(A,n-1,max)
print(MaxElem(A,n,A[0]))