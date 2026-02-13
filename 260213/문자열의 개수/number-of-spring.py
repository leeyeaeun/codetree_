ans = 0
l = []
while(True):
    s = input()
    if s=='0':
        break
    else:
        ans +=1
        if ans % 2 == 1:
            l.append(s)

print(ans)
print(*l, sep="\n")