n = int(input())
num = 1

arr = [
    [0] * n for _ in range(n)
]
for i in range(n):
    for j in range(n):
        arr[j][i] = num
        num +=1
        
for row in arr:
    for elem in row:
        print(elem,end=" ")
    print()
    