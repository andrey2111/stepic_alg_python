A = input().split()
n = int(A[0])
b = input().split()
k = int(b[0])
answer = []
for i in range(1, k+1):
    l = 1
    r = n
    flag = 0
    while l <= r:
        m = (r+l)//2
        if int(A[m]) == int(b[i]):
            answer.append(m)
            flag = 1
            break
        else:
            if int(A[m]) > int(b[i]):
                r = m - 1
            else:
                l = m + 1
    if flag == 0:
        answer.append(-1)
print(" ".join(str(i) for i in answer))
