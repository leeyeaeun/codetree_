s= list(input().split())

ans = 0
for i in s:
    for j in i:
        if j.isdigit() == False:
            ind = i.index(j)
            ans += int(i[:ind])
            #print(j, i, ind)
            break
print(ans)