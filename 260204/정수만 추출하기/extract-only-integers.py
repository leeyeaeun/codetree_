s= list(input().split())

ans = 0

for i in s:
    if i.isdigit():
        ans += int(i)
        continue
    for j in i:
        if j.isdigit() == False:
            ind = i.index(j)
            ans += int(i[:ind])
            #print(j, i, ind)
            break
print(ans)