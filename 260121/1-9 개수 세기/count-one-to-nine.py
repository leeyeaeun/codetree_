N = int(input())
cnt = [0]*10
arr = list(map(int,input().split()))
for  elem in arr:
    cnt[elem] +=1

print(*cnt[1:], sep='\n')