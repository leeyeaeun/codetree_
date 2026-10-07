n, k = map(int, input().split())
arr = list(map(int, input().split()))

ans = -(1e9)
# Please write your code here.

for i in range(n-k+1):
    cand = sum(arr[i:i + k])
    ans = max(ans,cand)

print(ans)