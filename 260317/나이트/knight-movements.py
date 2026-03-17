n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
dxs,dys = [-2,-1,+1,+2, -2,-1,1,2 ],[-1,-2,-2,-1, 1,2,2,1]
from collections import deque
q = deque()

step = [[-1]* n for _ in range(n)]
step[r1-1][c1-1] = 0


def bfs(sx, sy):
    q.append((sx,sy))

    visited = [[False]*n for _ in range(n)]
    visited[sx][sy] = True

    while q:

        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = x+dx,y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] +1

    return step



bfs(r1-1,c1-1)
#print(step)
print(step[r2-1][c2-1])