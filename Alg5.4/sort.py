# answer = 0
# for i in range(0, n-1):
#     for j in range(i+1, n):
#         if int(A[i]) > int(A[j]):
#             answer += 1
# print(answer)
from queue import Queue
c = 0


def merge(m, a, b):
    global c
    if len(a) == 0:
        for bi in b:
            m.append(bi)
            print('add all right:'+str(m))
        return
    if len(b) == 0:
        for ai in a:
            m.append(ai)
            print('add all left:'+str(m))
        return
    if a[0] <= b[0]:
        m.append(a[0])
        print('add left:'+str(m))
        merge(m, a[1:], b)
    else:
        if b[0] != 1000:
            c += len(a)
        m.append(b[0])
        print('add right:'+str(m))
        merge(m, a, b[1:])

# k = []
# merge(k, [2, 3, 5, 7], [1, 6, 7, 13])

n = int(input())
A = input().split()
step = 1
while n > step:
    step *= 2
if n < step:
    for i in range(n, step):
        A.append('1000')
print(A)
n = len(A)
q = Queue()
for i in A:
    q.put([int(i)])
while q.qsize() > 1:
    k = []
    merge(k, q.get(), q.get())
    #print(k)
    q.put(k)
#print(q.get())
print(c)
