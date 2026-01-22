n = int(input())

arr = list(map(int,input().split()))

min_val = arr[-1]
for i in range(n-2):
    if min_val> arr[i+1] - arr[i]:
        min_val = arr[i+1] - arr[i]

print(min_val)