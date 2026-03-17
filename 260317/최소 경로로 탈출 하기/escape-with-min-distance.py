n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
# 뱀이 없는 경우 1, 뱀이 있는 경우 0
# Please write your code here.

from collections import deque
q = deque()
q.append((0,0))
visited = [[False] * m for _ in range(n)]
step= [[-1]*m for _ in range(n)]
step[0][0] = 0

def bfs():
    ans = 0
    dxs,dys = [0,1,0,-1],[1,0,-1,0]
    
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs, dys):
            nx, ny = x + dx, y+dy
            if 0<= nx < n and 0<=ny<m and not visited[nx][ny]:
                if a[nx][ny] ==1:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    step[nx][ny] = step[x][y] + 1
bfs()
print(step[n-1][m-1])