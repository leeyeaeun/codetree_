n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

points = []
for _ in range(m):
    x, y = map(int, input().split())
    points.append((x - 1, y - 1))

# Please write your code here.

visited = [[False] * n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

answer = 0

def dfs(x,y,idx):
    global answer

    if (x,y) == points[idx]:
        
        if idx == m-1:
            answer +=1
            return

        idx +=1


    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0<=nx<n and 0<=ny<n):
            continue

        if grid[nx][ny] == 1:
            continue

        if visited[nx][ny]:
            continue

        visited[nx][ny] = True

        dfs(nx,ny,idx)

        visited[nx][ny] = False


sx,sy = points[0]

visited[sx][sy] = True

dfs(sx,sy,1)

print(answer)
