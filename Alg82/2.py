from math import ceil

N = int(input())
X = [int(i) for i in input().split()]
# with open('input.txt') as inf:
#     N = int(inf.readline())
#     X = [int(i) for i in inf.readline().split()]
P = [0]*N
M = [0]*(N+1)
L = 0
for i in range(N):
    lo = 1
    hi = L
    while lo <= hi:
        mid = ceil((lo+hi)/2)
        if X[M[mid]] >= X[i]:
            lo = mid+1
        else:
            hi = mid-1
    newL = lo
    P[i] = M[newL-1]
    M[newL] = i
    if newL > L:
        L = newL
S = [None]*L
k = M[L]
for i in range(L-1, -1, -1):
    S[i] = k + 1
    k = P[k]
print(L)
for i in S:
    print(i, end=' ')
