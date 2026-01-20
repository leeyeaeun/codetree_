arr = list(map(int,input().split()))
temp = None
num = 0
for i in range(len(arr)):
    if arr[i]==0:
        num = i
        break


new_arr = [
    elem + 3 if elem % 2 == 1 else elem // 2
    for elem in arr[:i]
]
print(*new_arr, sep=" ")

