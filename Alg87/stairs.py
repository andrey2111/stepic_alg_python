n = int(input())
A = input().split()
for i in range(0, n):
    A[i] = int(A[i])
D = [None]*(n+1)
D[0] = 0
D[1] = A[0]
for i in range(2, n+1):
    D[i] = A[i-1] + max(D[i-1], D[i-2])
print(D[n])
