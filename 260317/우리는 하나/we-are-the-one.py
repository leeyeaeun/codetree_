n, k, u, d = map(int, input().split()) # 두 도시간 높이의 차가 U 이상 D 이하
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

dxs,dys = [0,1,0,-1],[1,0,-1,0]
from collections import deque
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy)) # 최대 갯수니까 최대 갯수를 어.... 넣어야하나? 
    # 중복되면 안되는데.. 흠..
    
    
    visited[sx][sy] = True

    ans = 1
    while q:
        x,y = q.popleft()

        for dx,dy in zip(dxs,dys):
            nx,ny = x +dx,y+dy
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if u<= abs(grid[nx][ny] - grid[x][y]) <=d:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    ans +=1
                
    return ans
# 해당 위치에서 갈 수 있는 최대 도시의 수와, 그 위치들이 나옴..
# 근데 이걸.. k 개를 뽑아야해. 흠..
# 중복이 없어야하니까..  map으로 가능한 도시 좌표를 다 저장해둘까?
# 그래도 n2정도로 나올거같은데.. 시간이 너무 오래걸려보이는데 흠..

visited = [[False] * n for _ in range(n) ]
components_list = []

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            ans = bfs(i,j)
            components_list.append(ans)

components_list = sorted(components_list)

answer = sum(components_list[ -k :  ])

print(answer)
