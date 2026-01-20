N = int(input())

arr = [elem for elem in list(map(int,input().split())) if elem %2 == 0]

print(*arr, sep=" ")