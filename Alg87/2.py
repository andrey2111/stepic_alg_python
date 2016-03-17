n = int(input())
A = [None]*(n+1)
answer = []
for i in range(1, n+1):
    A[i] = i-1
for i in range(2, n+1):
    if i % 3 == 0:
        A[i] = min(A[i-1]+1, A[int(i/3)]+1)
    else:
        if i % 2 == 0:
            A[i] = min(A[i-1]+1, A[int(i/2)]+1)
        else:
            A[i] = A[i-1]+1
print(A[n])
answer.append(n)
for i in range(0, A[n]):
    if n % 3 == 0:
        if A[n-1] > A[int(n/3)]:
            answer.append(int(n/3))
            n = int(n/3)
        else:
            answer.append(A[n-1])
            n -= 1
    else:
        if n % 2 == 0:
            if A[n-1] > A[int(n/2)]:
                answer.append(int(n/2))
                n = int(n/2)
            else:
                answer.append(n-1)
                n -= 1
        else:
            answer.append(int(n-1))
            n -= 1
print(' '.join(str(c) for c in reversed(answer)))
