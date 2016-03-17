import sys
n = sys.stdin.read().split()
a = []
for i in range(1, int(n[0])+1):
    a.append((int(n[2*i-1]), int(n[2*i])))
a.sort(key=lambda r: r[1])
m = []
while len(a) > 0:
    k = a[0][1]
    m.append(k)
    while len(a) > 0 and k in range(a[0][0], a[0][1]+1):
            a.pop(0)
print(len(m))
print(" ".join(str(i) for i in m))
