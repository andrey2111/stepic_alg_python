A = input()
B = input()
n = len(A)
m = len(B)
D = []
for i in range(0, n+1):
    D.append([None]*(m+1))
for i in range(0, n+1):
    D[i][0] = i
for j in range(0, m+1):
    D[0][j] = j
for i in range(0, n):
    for j in range(0, m):
        if A[i] == B[j]:
            c = 0
        else:
            c = 1
        D[i+1][j+1] = min(D[i][j+1]+1, D[i+1][j]+1, D[i][j]+c)
print(D[n][m])
