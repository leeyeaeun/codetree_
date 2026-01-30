a,b = input().split()
ans = a
if len(b)>len(a):
    ans = b
else:
    ans = False
if ans:
    print(ans, len(ans))
else:
    print('same')