n = int(input())
A = input().split()
for i in range(0, n):
    A[i] = int(A[i])
D = [None]*n
for i in range(0, n):
    D[i] = 1
    for j in range(0, i):
        if A[i] <= A[j] and D[j]+1 > D[i]:
            D[i] = D[j] + 1
ans = 0
for i in range(0, n):
    ans = max(ans, D[i])
print(A)
print(D)
print(ans)
answer = [None]*ans
for i in range(n-1, -1, -1):
    if D[i] == ans:
        answer[-1] = i
        break
k = answer[-1]
print(answer)
for i in range(k-1, -1, -1):
    if A[i] >= A[k] and D[i] == D[k]-1:
        answer[k-2] = i
        break
print(answer)
print(k)
