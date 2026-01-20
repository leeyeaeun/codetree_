arr = list(map(int, input().split()))

total =0
n = 0
for elem in arr:
    if elem == 0:
        break
    if elem %2 == 0:
        total += elem
        n+=1

print(n, total)