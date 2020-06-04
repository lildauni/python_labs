l = []
def prompt(i = 1):
  number = int(input('Введите число, которое нужно вывести, если хотите прекратить, то введите ноль '))
  if(number == 0):
    return
  if(i % 2 != 0):
    l.append(number)
  return prompt(i + 1)
def print_sequence():
  prompt()
  for num in l:
    print(num, end=" ")
  l.clear()
print_sequence()