N = int(input())

arr= [[1]*(N+1) for _ in range(N+1)]
print('1')
#print('1 1')
for i in range(N-1):
    print(1, end = " ")
    for j in range(i):
        arr[i+1][j+1] = arr[i][j] + arr[i][j+1]
        print(arr[i+1][j+1], end = " ")
    print(1, end = " ")
    print()

