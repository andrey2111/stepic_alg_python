n = int(input())
coins = [25, 10, 5, 1]
answer = 0
while n > 0:
    for c in coins:
        if n >= c:
            answer += n // c
            n %= c
print(answer)
