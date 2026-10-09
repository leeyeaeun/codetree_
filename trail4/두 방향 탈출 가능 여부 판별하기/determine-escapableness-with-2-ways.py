n, m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

dx,dy = [1,0],[0,1]

answer = 0
def dfs(x,y):
    global answer

    if x == n-1 and y ==m-1:
        answer = 1
        return

    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]

        if not ((0<=nx<n) and (0<=ny<m)):
            continue
        
        if visited[nx][ny]:
            continue

        if grid[nx][ny] == 0: # 뱀이 있는 경우
            continue

        visited[nx][ny] =True
        dfs(nx,ny)

visited = [[False]* m for _ in range(n)]
visited[0][0] = True
dfs(0,0)
print(answer)