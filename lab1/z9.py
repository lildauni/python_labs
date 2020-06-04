a=55
s=0
while a!=0:
    k=int(a)%10
    s+=k
    a/=10
print("s =",s)