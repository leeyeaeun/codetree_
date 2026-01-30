N = int(input())

arr=  [[1]* N for _ in range(N)]
num=1
for i in range(N):
    if i % 2 == 1:
        for j in range(N):
            #print(N-i-1, j, num)
            arr[j][N-i-1] = num
            num+=1
    else:
        for j in range(N-1,-1,-1):
            #print(N-i-1, j, num)
            arr[j][N-i-1] = num
            num +=1


for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()
