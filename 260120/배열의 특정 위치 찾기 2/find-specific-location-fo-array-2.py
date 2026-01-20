arr = list(map(int,input().split()))

print(abs(sum(arr[::2]) - sum(arr[1::2])))