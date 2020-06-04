import random
def doublef(n):
  if(n > 2):
    return n * doublef(n - 2)
  return n
for i in range(0, 5):
  a = random.randint(1, 10)
  print(f'Двойной факториал числа {a} = {f(a)}')
