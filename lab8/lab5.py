class Variables:
  def __init__(self, var1, var2):
    self.a = var1
    self.b = var2
  def __del__(self):
    print(f'Переменные {self.a}, {self.b} были удалены')
  