n,m = map(int,input().split())

arr1 = [
    list(map(int,input().split()))
    for _ in range(n)
]

arr2 = []
for i in range(n):
    row = list(map(int, input().split()))
    arr2.append([
        0 if row[j] == arr1[i][j] else 1
        for j in range(m)
    ])


for row in arr2:
    for elem in row:
        print(elem, end=" ")
    print()