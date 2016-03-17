(W, n) = input().split()
wi = input().split()
W = int(W)
n = int(n)
for i in range(0, n):
    wi[i] = int(wi[i])
D = []
for i in range(0, W+1):
    D.append([None]*(n+1))
for w in D:
    w[0] = 0
for w in range(0, n+1):
    D[0][w] = 0
for i in range(1, n+1):
    for w in range(1, W+1):
        D[w][i] = D[w][i-1]
        if wi[i-1] <= w:
            D[w][i] = max(D[w][i], D[w-wi[i-1]][i-1]+wi[i-1])
print(D[W][n])
