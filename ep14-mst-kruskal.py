def findSet (S, x):
    for i in range (len(S)):
        for j in S[i]:
            if j == x:
                return i

def makeSet(S,x):
    S.append([x])
             
def union (S, x, y):
    i = findSet(S,x)
    j = findSet(S, y)
    S[i] += S[j]

S = []
makeSet(S, "a")
print (S)
makeSet(S, "b")
print (S)
makeSet(S, "c")
print (S)
union(S, "b", "c")
print (S)


