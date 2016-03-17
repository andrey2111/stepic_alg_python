n = int(input())
A = input().split()
for i in range(0, n):
    A[i] = int(A[i])
D = [None]*n
for i in range(0, n):
    D[i] = 1
    for j in range(0, i):
        if A[i] % A[j] == 0 and D[j]+1 > D[i]:
            D[i] = D[j] + 1
ans = 0
for i in range(0, n):
    ans = max(ans, D[i])
print(ans)
