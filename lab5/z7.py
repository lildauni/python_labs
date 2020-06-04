def GCD(a, b):
  if(b == 0):
    return a
  if(a == 0):
    return b
  if(a > b):
    return GCD(a % b, b)
  return GCD(a, b % a)
a = 6
b = 9
c = 3
d = 4
print('НСД 1 и 2 числа: ', GCD(a, b))
print('НСД 3 и 4 числа: ', GCD(c, d))
print('НСД 1 и 4 числа: ', GCD(a, d))
