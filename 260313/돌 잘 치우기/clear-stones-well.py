n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

r = []
c = []
for _ in range(k):
    ri, ci = map(int, input().split())
    r.append(ri - 1)
    c.append(ci - 1)

# Please write your code here.
from collections import deque

stones = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            stones.append((i, j))


dxs,dys = [0,1,0,-1],[1,0,-1,0]

def bfs(grid):
    visited = [[False] * n for _ in range(n)] 
    q= deque()
    for sx, sy in zip(r, c):
        visited[sx][sy] = True
        q.append((sx, sy))

    while q:
        #print(q)
        x, y= q.popleft()
        

        for dx,dy in zip(dxs, dys):
            nx, ny = x+dx, y+ dy

            if (0 <= nx < n and 0 <= ny < n):
                if grid[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny))

    reachable = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                reachable += 1
    return reachable

answer = 0

from itertools import combinations

for comb in combinations(stones, m):
    board = [row[:] for row in grid]

    for x, y in comb:
        board[x][y] = 0

    answer = max(answer, bfs(board))

print(answer)
