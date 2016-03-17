import sys
n = sys.stdin.read().split()
a = []
cap = int(n[1])
maxsum = 0
for i in range(1, int(n[0])+1):
    a.append((int(n[2*i]), int(n[2*i+1])))
a.sort(key=lambda r: r[0]/r[1], reverse=True)
for i in a:
    if cap > 0:
        if i[1] <= cap:
            maxsum += i[0]
            cap -= i[1]
        else:
            maxsum += cap*i[0]/i[1]
            cap = 0
print(maxsum)
