arr = list(map(int,input().split()))

cnt = [0]*11

for elem in arr:
    if elem == 0:
        break
    p = elem //10
    cnt[p] +=1

for i in range(10, 0, -1):
    print(f"{i*10} - {cnt[i]}")