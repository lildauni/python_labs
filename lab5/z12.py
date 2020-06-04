import re
expr = input('Введите выражение \n')
def parseExpr(expr):
  symbols = re.sub(r'\s', '', expr)
  symbols = re.split(r'(\+|\-)', symbols)
  assert(len(symbols) != 0)
  if len(symbols) == 1:
    return symbols[0]
  result = int(symbols[0])
  for i in range(0, len(symbols)):
    if(symbols[i] == '+'):
      result += int(symbols[i+1])
    elif(symbols[i] == '-'):
      result -= int(symbols[i+1])
  return result
print(f'Выражение {expr} = {parseExpr(expr)}')