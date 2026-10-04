n = int(input())
xs = []
dir = []

arr = [0] * (3000)
OFFSET =  1000
start = 1500

for _ in range(n):
    xi, di = input().split()
    xs.append(int(xi))
    dir.append(di)


for i in range(n):
    if dir[i] == 'R':
        arr[start : start+xs[i]] = [x + 1 for x in arr[start:start+xs[i]]]
        start  = start + xs[i]
    else:
        arr[start-xs[i]:start] = [x + 1 for x in arr[start-xs[i]:start]]
        start =  start - xs[i] 

ans = 0

for i in arr:
    if i >= 2:
        #print(i)
        ans +=1
print(ans)
# Please write your code here.