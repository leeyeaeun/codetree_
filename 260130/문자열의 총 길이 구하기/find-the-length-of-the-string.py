arr = input().split()

ans = 0
for elem in arr:
    ans += len(elem)

print(ans)