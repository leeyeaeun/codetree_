N = int(input())

arr = input().split()
ans =""
for elem in arr:
    ans += elem
#print(ans)

for i in range(0, len(ans), 5):
    print(ans[i:i+5])