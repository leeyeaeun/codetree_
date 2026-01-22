n = int(input())
nums = list(map(int, input().split()))

count = [0] * (1001)

for elem in nums:
    count[elem] +=1

max_val = -1
for i, elem in enumerate(count):
    if elem == 1:
        if max_val < i :
            max_val = i 
print(max_val)