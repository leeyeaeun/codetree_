n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dxs,dys = [0,1,0,-1],[1,0,-1,0]
from collections import deque
q = deque()
ans = [[-2]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            ans[i][j] = -1
        elif grid[i][j] == 2:
            ans[i][j]= 0
            q.append((i,j))

def bfs():
    썩을귤리스트=[]
    visited = [[False]*n for _ in range(n)]
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    썩을귤리스트.append((nx,ny))
                    visited[nx][ny] = True
    return 썩을귤리스트

time = 0 
while True:
    time +=1
    썩을귤리스트 = bfs()
    
    if not 썩을귤리스트:
        break

    for x,y in 썩을귤리스트:
        grid[x][y] = 2
        ans[x][y] = time
        q.append((x,y))

for elem in ans:
    print(*elem, sep=" ") 

