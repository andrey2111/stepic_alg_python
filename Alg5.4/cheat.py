c = 0

def mergeSort(alist):
    global c
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                #if righthalf[j] != 1000:
                c += i+1
                alist[k] = righthalf[j]
                j=j+1
            k = k + 1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)


n = int(input())
alist = input().split()
for i in range(0, n):
    alist[i] = int(alist[i])
# step = 1
# while n > step:
#     step *= 2
# if n < step:
#     for i in range(n, step):
#         alist.append('1000')
mergeSort(alist)
print(alist)
print(c)
