A = [22, 7, 6, 5]
B = [11, 9, 2]
def reverse(A, B):
  i = 0
  j = 0
  C = []
  while i < len(A) and j < len(B):
    if(A[i] > B[j]):
      C.append(A[i])
      i += 1
    else:
      C.append(A[j])
      j += 1
  if i < len(A) - 1:
    C += A[i:]
  else:
    C += B[j:]
  return C
C = reverse(A, B)
print(C)