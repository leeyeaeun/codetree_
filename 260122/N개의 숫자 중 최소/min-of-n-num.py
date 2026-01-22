n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
min_val = a[0]

for elem in a[1:]:
    if elem < min_val:
        min_val = elem

num = 0
for elem in a:
    if elem == min_val:
        num+=1 

print(min_val, num)