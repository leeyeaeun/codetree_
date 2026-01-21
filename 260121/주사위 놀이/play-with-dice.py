arr= list(map(int, input().split()))
cnt = [0]*7
for elem in arr:
    cnt[elem] +=1

for i in range(1,7):
    print(f"{i} - {cnt[i]}")