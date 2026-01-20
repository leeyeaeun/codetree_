arr = list(map(int,input().split()))
total = 0
n = 0
for elem in arr:
    if elem == 0:
        break
    total += elem
    n +=1

print(total, f"{total/n:.1f}")