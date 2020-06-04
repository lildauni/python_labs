def isSymetric(str, i, j):
  if(str[i] == str[j]):
    if(i == j or i + 1 == j):
      return True
    return isSymetric(str, i+1, j-1)
  return False
print(isSymetric('aba', 0, 2))