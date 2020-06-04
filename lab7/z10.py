import re
def country():
  s = input('Введите страну и ее города) ')
  a = s.split(' ')
  return a
c = {}
while True:
  a: list = country()
  country = a[0]
  a.remove(a[0])
  c[country] = a
  if(input('Если хотите остановится, введите 0 ') == '0'):
    break 
print('Словарь стран и городов', c)