a = input()
b = input()
ans = 0
while True:
    if a == b:
        print(ans)
        break
    else:
        ans +=1
        a = a[-1] + a[:-1]
        if ans >= len(a):
            print(-1)
            break
        
