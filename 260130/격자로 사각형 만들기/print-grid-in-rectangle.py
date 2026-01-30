N = int(input())

arr = [ [1]* N for _ in range(N)]

for i in range(1, N):
    for j in range(1,N):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j] + arr[i][j-1]
    
for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()