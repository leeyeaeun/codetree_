a,b = map(int,input().split())

s = a+b
s=str(s)
ans = 0
for i in s:
    if i == '1':
        ans +=1 
print(ans)