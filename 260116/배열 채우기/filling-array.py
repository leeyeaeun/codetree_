arr = list(map(int, input().split()))

num = 0

for elem in arr:
    if elem == 0:
        break
    else:
        num += 1



for elem in arr[num-1::-1]:
    print(elem, end=" ")
