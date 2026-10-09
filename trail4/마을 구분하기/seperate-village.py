n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
dx , dy = [1,-1,0,0],[0,0,1,-1]

def dfs(x,y):
    global count
    global visited

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0<=nx<n and 0<=ny<n):
            continue
        
        if visited[nx][ny]:
            continue

        if grid[nx][ny] == 0:
            continue

        visited[nx][ny] = True
        count +=1
        dfs(nx, ny)

village_list = []

visited = [[False]* n for _ in range(n)]

for i in range(n):
    for j in range(n):

        if grid[i][j] == 1 and not visited[i][j]:
            count  = 1 
            visited[i][j] = True
            dfs(i,j)
            village_list.append(count)

village_list.sort()
print(len(village_list))
for i in village_list:
    print(i)