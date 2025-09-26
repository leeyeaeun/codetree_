n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

order = 1
answer = [[0]*(n) for _ in range(n)]
visited = [[False]*(n) for _ in range(n)]
def dfs(x,y):
    global order
    dxs, dys = [0,1],[1,0]

    visited[x][y] = 1
    order +=1
    answer[x][y] = order

    
    for dx,dy in zip(dxs,dys):
        new_x, new_y = x + dx, y + dy

        if can_go(new_x,new_y):
            dfs(new_x, new_y)

def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y] == True or grid[x][y] == 0:
        return False
    return True


def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n


dfs(0,0)
print(1 if answer[n-1][n-1] != 0 else 0)