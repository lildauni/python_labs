try:
    f = open('realn.txt', 'r', encoding='windows-1251')
except FileNotFoundError:
    print('Файл не обнаружен')
except IsADirectoryError:
    print('Объект по указанному пути является директорией')
else:
    n = [float(i) for i in f.readlines()]
    f.close()
    print(n)
    for i in range(len(n)):
        n[i] = n[i] ** 2
    print(n)
    f = open('realn.txt', 'w', encoding='windows-1251')
    for i in n:
        f.write(str(i) + '\n')
    f.close()