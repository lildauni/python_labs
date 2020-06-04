try:
    f1=open('file1.txt','r+')
    f2=open('file2.txt','r+')
except FileNotFoundError:
    print('Файл не найден')
except (UnicodeEncodeError, UnicodeDecodeError, UnicodeTranslateError):
    print('Ошибка кодирования в Unicode')
else:
    str1=f1.read()
    str2=f2.read()
    f2.write('\n'+str1)
    f1.write('\n'+str2)
    f1.close()
    f2.close()