n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
import sys
INT_MIN = -1 * sys.maxsize
sol = INT_MIN

for i in range(n):
    for j in range(i+2,n):
        cand = numbers[i] + numbers[j]
        sol = max(sol, cand)

print(sol)