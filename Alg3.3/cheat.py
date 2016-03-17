from heapq import heappush, heappop
n = int(input())
heap = []
for i in range(0, n):
    a = input().split()
    if len(a) == 1:
        print(-heappop(heap))
    else:
        heappush(heap, -int(a[1]))
