n,m = map(int,input().split())

num = 1 
arr = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        arr[i][j] = num
        num+=1


for row in arr:
    for elem in row:
        print(elem, end =" ")
    print()