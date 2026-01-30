N = int(input())

arr= [[1]*N for _ in range(N)]
print('1')
print('1 1')
for i in range(1,N-1):
    print(1, end = " ")
    for j in range(i):
        arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        print(arr[i][j], end = " ")
    print(1, end = " ")
    print()

