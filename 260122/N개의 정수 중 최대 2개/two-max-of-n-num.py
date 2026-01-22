n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
max_val = a[0]
idx = -1
for i, elem in enumerate(a[1:]):
    if elem > max_val:
        max_val = elem
        idx = i

print(max_val,end=" ")

a.pop(idx+1)

max_val = a[0]

for elem in a[1:]:
    if elem> max_val:
        max_val = elem

print(max_val,end=" ")