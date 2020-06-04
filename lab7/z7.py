A = [10, 20, 30]
B = [421, 124, 23, 1, 1]
def unique(ls: list):
  for li in ls:
    if(ls.count(li) != 1):
      return False
  return True
if unique(A):
  print(f'Элементы массива {A} - уникальные')
if not unique(B):
  print(f'Элементы массива {B} - не уникальные')