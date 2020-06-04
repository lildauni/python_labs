try:
    fin=open('m.txt','r')
except FileNotFoundError:
    print('Файл не найден')
except IsADirectoryError:
    print('Объект по указанному пути является директорией')
else:
    m=list()
    for i in fin.readlines():
        m.append([float(j) for j in i.split(' ')])
    fin.close()
    for i in m:
        if len(i)<len(m[0]):
            for j in range(len(m[0])-len(i)):
                i.insert(0,0.0)
    try:
        fout=open('m2.txt','w')
    except FileExistsError:
        print('Файл с указанным именем уже открыт')
    else:
        for i in m:
            for j in i:
                fout.write(str(j)+' ')
            fout.write('\n')
        fout.close()