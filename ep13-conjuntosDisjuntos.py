def makeSet(S, x):
  S.append([x])

def findSet(S, x):
  for index, valor in enumerate(S):
    if x in valor:
      return index
  return -1

def union(S, x, y):
  i = findSet(S, x)
  j = findSet(S, y)

  if i & j != -1: 
    if i != j:
      S[i].extend(S[j])
      del S[j]
      S.append([])

def main():
  n = int(input())
  S = []

  for _ in range(n):
    operacao = input().split()

    if operacao[0] == 'M':
      makeSet(S, operacao[1])
      print(S)
    elif operacao[0] == 'F':
      idx = findSet(S, operacao[1])
      if idx != -1:
        print(idx, S)
    elif operacao[0] == 'U':
      union(S, operacao[1], operacao[2])
      print(S)

if __name__ == "__main__":
    main()
