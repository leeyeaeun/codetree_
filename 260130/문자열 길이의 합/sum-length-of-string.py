N = int(input())

ans = 0
ans_a = 0
for _ in range(N):
    p = input()
    ans += len(p)
    if p[0] =='a':
        ans_a+=1

print(ans,ans_a)