(n, m) = input().split()
n = int(n)
m = int(m)
a = []
for i in range(0, n):
    (ai, bi) = input().split()
    a.append((int(ai), 0))
    a.append((int(bi), 2))
points = input().split()
for i in range(0, m):
    a.append((int(points[i]), 1))
a = sorted(a, key=lambda pair: pair[1])
a = sorted(a, key=lambda pair: pair[0])
count0 = 0
count2 = 0
answerd = {}
for pair in a:
    if pair[1] == 0:
        count0 += 1
    if pair[1] == 2:
        count2 += 1
    if pair[1] == 1:
        answerd.update({pair[0]: count0-count2})
print(' '.join(str(answerd.get(int(i))) for i in points))
# answer = []
# for point in points:
#     answer.append(bisect(a, int(point))-bisect(b, int(point))) #
# print(' '.join(str(answ) for answ in answer))
