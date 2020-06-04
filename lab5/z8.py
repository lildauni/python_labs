from random import randint
def DigitSum(a):
  return (a % 10) + DigitSum(a // 10) if a != 0 else 0
for i in range(0, 6):
  a = randint(0, 100)
  print(f"Сума цифр числа {a} = {DigitSum(a)}")