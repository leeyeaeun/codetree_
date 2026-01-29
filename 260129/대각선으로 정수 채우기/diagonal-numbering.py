n, m = map(int, input().split())

# Please write your code here.
arr = [[1]*m for _ in range(n)]
num = 2

for k in range(1,m):
    for i in range(k+1):
        if i >=n:
           continue
        arr[i][k-i] = num
        num +=1
    k +=1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()