N, a = input().split()
N = int(N)

ans = 0
for _ in range(N):
    s = input()
    if s== a:
        ans +=1
print(ans)