n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# Please write your code here.

order = {}
for i, elem in enumerate(a):
    order[elem] = i + 1

for _ in range(q):
    x = int(input())
    if x in order:
        cur = order[x]
        print((cur-1)*(n-cur))
    else:
        print(0)