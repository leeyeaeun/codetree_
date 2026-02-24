n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def doit():
    global a1,b1,arr
    ans = 0
    ans = sum(arr[a1-1:b1])
    print(ans)

for i in range(m):
    a1, b1 = queries[i]    
    doit()

