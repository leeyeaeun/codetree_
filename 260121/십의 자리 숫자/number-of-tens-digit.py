arr= list(map(int,input().split()))
cnt = [0]* 10
for elem in arr:
    if elem == 0:
        break
    p = elem // 10
    cnt[p] +=1

for i in range(1,10):
    print(f"{i} - {cnt[i]}")