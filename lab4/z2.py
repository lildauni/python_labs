b=int(input("Введите первый член прогрессии: "))
q=int(input("Введите знаменатель прогрессии: "))
n=int(input("Введите количество чисел в прогрессии: "))
def prog(b,q,n,count):
    if(n==count):
        return b
    else:
        return prog(b*q,q,n,count+1)
n1=int(input("Введите номер елемента, который хотите найти"))
print(prog(b,q,n1,1))
s=0
for i in range(n):
   s+=b
   b*=q
print(s)