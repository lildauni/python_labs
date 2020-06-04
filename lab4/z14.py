a=int(input("Введите число: "))
for i in range(a):
    if(pow(2,i)==a):
        print("YES")
        quit()
    if(pow(2,i)>a):
        print("NO")
        quit()