n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.
import sys
INT_MAX = sys.maxsize
sol = INT_MAX

for i in range(n):
# i 번째 방부터 시작
    dist = 0
    for j in range(n):
        #j번째 방에왓음
        if j > i : # 순방향
            dist += abs(i-j)*a[j]
            

        if i > j: # 역방향, j= 1, i=2
            dist += abs( n - (i-j))*a[j]
        #print(dist)
    sol = min(dist,sol)

print(sol)