from bisect import bisect

(n, m) = input().split()
n = int(n)
m = int(m)
a = []
b = []
for i in range(0, n):
    (ai, bi) = input().split()
    a.append(int(ai))
    #bisect.insort(a, int(ai))
    b.append(int(bi))
    #bisect.insort(b, int(bi))
points = input().split()

a.sort()
b.sort()
answer = []
for point in points:
    answer.append(bisect(a, int(point))-bisect(b, int(point))) #
print(' '.join(str(answ) for answ in answer))
