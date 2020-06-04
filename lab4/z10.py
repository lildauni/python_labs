n=int(input("Введите количество членов в последовательности: "))
def sequence(n, a = 1, b = 0, c = 0):
  if(c == a):
    c = 0
    a += 1
  if b == n:
    return
  print(a)
  return sequence(n, a, b + 1, c + 1)
sequence(n)