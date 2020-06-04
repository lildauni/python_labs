d=input("Введите число: ")
m=input("Введите месяц: ")
if(int(d)>1):
    print(int(d)-1,m,sep=".")
else:
    if(int(m)==3 or int(m)==5 or m==7 or m==8 or m==10 or m==12):
        print(31,m-1,sep=".")
    if(m==4 or m==6 or m==9 or m==11):
        print(30,d-1,sep=".")
    if(m==1):
        print(31,12,sep=".")
    if(m==2):
        print(28,1,sep=".")