R, C = map(int, input().split())
grid = [input().split() for _ in range(R)]

sol = 0

def dfs(x, y, jump_cnt):
    global sol

    # 정확히 3번 점프했을 때
    if jump_cnt == 3:
        if x == R - 1 and y == C - 1:
            sol += 1
        return

    curr = grid[x][y]

    # 현재 위치보다 오른쪽 + 아래쪽으로만 점프
    for nx in range(x + 1, R):
        for ny in range(y + 1, C):

            # 다른 색깔이어야 이동 가능
            if grid[nx][ny] != curr:
                dfs(nx, ny, jump_cnt + 1)


dfs(0, 0, 0)

print(sol)