n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
max_val = -1
for elem in nums:
    if max_val == elem:
        max_val = -1
        continue
    if max_val < elem :
        max_val = elem
    
print(max_val)