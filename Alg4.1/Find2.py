A = input().split()
n = int(A[0])
l = 1
r = n
flag = 0
while l <= r:
    m = (r+l)//2
    if int(A[m]) == m:
        answer = m
        flag = 1
        break
    else:
        if int(A[m]) > m:
            r = m - 1
        else:
            l = m + 1
if flag == 0:
    answer = -1
print(answer)
