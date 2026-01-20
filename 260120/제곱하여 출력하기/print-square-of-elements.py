N = int(input())

arr = [elem**2 for elem in list(map(int,input().split())) ]
print(*arr, sep=" ")

