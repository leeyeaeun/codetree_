n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_coin = 0
for i in range(n):
    for j in range(n-2):
        max_coin = max(max_coin, grid[i][j] + grid[i][j+1]+grid[i][j+2] )
        
print(max_coin)