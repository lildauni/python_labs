from typing import List
class Array:
  length: int
  capacity: int
  elems: List[str]
  def __init__(self, elems: List[str], capacity: int = None):
    self.length = len(elems)
    self.elems = []

    if(capacity is None):
      capacity = self.length
    self.capacity = capacity
    
    for elem in elems:
      self.elems.append(elem)
    
  def __getitem__(self, key):
    assert(key < self.length)
    return self.elems[key]

  def append(self, value):
    assert (self.length < self.capacity)
    self.elems.append(value)
    self.length += 1
  
  def concat(self, arr):
    united = Array([], self.capacity + arr.capacity)
    for elem in self.elems:
      united.append(elem)
    for elem in arr.elems:
      united.append(elem)
    return united
  
  def fuse(self, arr):
    fused = Array([], self.capacity + arr.capacity)
    considered = {}
    for elem in self.elems:
      if elem not in considered:
        fused.append(elem)
        considered[elem] = True
    for elem in arr.elems:
      if(elem not in considered):
        fused.append(elem)
        considered[elem] = True
    return fused

  def __str__(self):
    description = ''
    for elem in self.elems:
      description += elem + ' |> '
    return description
  
  
arr1 = Array(['5', 'new str', 'str'], 5)
arr2 = Array(['str', 'val', 'val'], 6)

united = arr1.fuse(arr2)
print(united)