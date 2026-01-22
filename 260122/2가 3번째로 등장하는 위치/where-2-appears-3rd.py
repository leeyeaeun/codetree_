N = int(input())
arr=list(map(int,input().split()))
i=0

for idx, elem in enumerate(arr):
    if elem == 2:
        i +=1
    if i == 3:
        print(idx+1)
        break
