n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
# Please write your code here.
def dfs(x,y):
    global count

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0<=nx<n and 0<=ny<n):
            continue

        if visited[nx][ny]:
            continue
        
        if not grid[x][y] == grid[nx][ny]:
            continue
        visited[nx][ny] = True
        count +=1
        dfs(nx,ny)
ans_list = []
ans = 0
visited = [[False]* n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            visited[i][j] = True
            count = 1
            dfs(i,j)
            ans_list.append(count)
            if count >= 4:
                ans +=1


print(ans, max(ans_list))