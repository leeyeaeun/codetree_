n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque


q = deque()
 # 0,0 부터.. 이어진. 1 을 찾는거야..
dxs,dys = [0,1,0,-1],[1,0,-1,0] # 오른쪽, 아래, 왼쪽, 위 순서로

def bfs():
    visited = [[False]*m for _ in range(n)]
    melt = []
    q.append((0,0))
    visited[0][0] = True
    while q:
        x,y = q.popleft()
        for dx,dy in zip(dxs,dys):
            nx,ny = x + dx, y+dy
            if 0 <= nx < n and 0<= ny< m and not visited[nx][ny]:
                if a[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                else:
                    visited[nx][ny] = True
                    melt.append((nx,ny))

    return melt

time = 0 
melt_list = []

while True:
    melt = bfs()
    melt_list.append(len(melt))

    if not melt:
        break

    if melt:
        for x,y in melt:
            a[x][y] = 0
    time += 1 

print(time, melt_list[-2])
