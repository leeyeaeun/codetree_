N = int(input())
ans = 0

for _ in range(N):
    ans += int(input())

ans = str(ans)
print(ans[1:] + ans[0])