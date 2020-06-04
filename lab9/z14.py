try:
    f=open('dates.txt','r',encoding='windows-1251')
except FileNotFoundError:
    print('Файл не найден')
else:
    dstr=f.readlines()
    f.close()
    dint=list()
    for i in dstr:
        dint.append([int(j) for j in i.split('/')])
    f1=open('days.txt','w')
    f2=open('months.txt','w')
    for i in dint:
        f1.write(str(i[0])+'\n')
        f2.write(str(i[1]) + '\n')
    f1.close()
    f2.close()