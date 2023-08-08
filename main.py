def isOdd(n):
  return True if n % 2 == 1 else False

def numToBinary(N):
  if N == 0:
    return ""
  elif isOdd(N):
    return numToBinary(N // 2) + "1"
  else:
    return numToBinary(N // 2) + "0"

def binaryToNum(S):
  if S == '':
    return 0
  elif isOdd(int(S[-1])):
    return binaryToNum(S[:-1]) * 2 + 1
  else:
    return binaryToNum(S[:-1]) * 2 + 0

def increment(S):

  if S == '':
    return 0
  else:
    binaryNumber = numToBinary(int(binaryToNum(S)+1))
    return '0' * (8 - len(binaryNumber)) + binaryNumber

def count(S, n):

  print(S)
  if S == '':
    print('')
  elif n == 0:
    print('')
  else:
    count(increment(S), n-1)


