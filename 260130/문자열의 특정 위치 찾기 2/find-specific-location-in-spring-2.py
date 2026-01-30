arr = ['apple','banana','grape','blueberry','orange']

p=input()
ans =[]
for elem in arr:
    if p == elem[2] or p== elem[3]:
        ans.append(elem)
        continue

for elem in ans:
    print(elem)
print(len(ans))