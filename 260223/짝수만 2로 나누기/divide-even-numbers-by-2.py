n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def divide_only_even(n, arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] //=2

divide_only_even(n, arr)
print(*arr, sep=" ", end=" ")
