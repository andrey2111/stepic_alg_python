n = int(input())
start = 1
answer = []
while n > 0:
    if start > n:
        answer[-1] += n
        break
    for i in range(start, n + 1):
        if n - i != i:
            n = n - i
            start = i + 1
            answer.append(i)
            break
print(len(answer))
print(" ".join(str(i) for i in answer))
