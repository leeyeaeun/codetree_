N,M = map(int,input().split())

arr= [[0]* (N) for _ in range(N)]
num = 1
for _ in range(M):
    x,y = map(int,input().split())
    arr[x-1][y-1] = num
    num +=1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()

