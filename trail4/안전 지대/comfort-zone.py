n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

max_k = grid[0][0]
for i in grid:
    max_k = max(max_k, *i)


safe_list = [-1] * (max_k+1)

dx, dy = [1,-1,0,0],[0,0,1,-1]

def dfs(x,y,k):
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if not (0<=nx<n and 0<=ny<m):
                continue
            if visited[nx][ny]:
                continue
            if grid[nx][ny] <= k:
                continue
            visited[nx][ny] = True
            stack.append((nx, ny))

for k in range(1, max_k + 1):
    visited = [[False]*m for _ in range(n)]
    count  = 0
    for i in range(n):
        for j in range(m):
            
            if not visited[i][j] and grid[i][j] > k :
                count  += 1    
                visited[i][j] = True
                dfs(i,j,k) 
    
    safe_list[k] = count                 

ans = max(safe_list[1:])

print(safe_list.index(ans), ans)