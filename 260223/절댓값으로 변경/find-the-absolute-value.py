n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def makeAbs(n,arr):
    for i in range(n):
        if arr[i] < 0:
            arr[i] = abs(arr[i])
    
makeAbs(n,arr)
print(*arr, end=" ", sep=" ")