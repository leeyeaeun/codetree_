
arr = [
    list(map(int,input().split()))
    for _ in range(4)
]
total = 0
for i in range(4):
    for j in range(i,4):
        #print(arr[j][i])
        total += arr[j][i]

print(total)