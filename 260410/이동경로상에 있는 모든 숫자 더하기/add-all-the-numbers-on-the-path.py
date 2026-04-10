N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.

x, y = N//2, N//2
(dx, dy) = (-1, 0)

Rs = [(-1,0), (0,1), (1,0), (0,-1)]
Ls = [(-1,0), (0,-1), (1,0), (0,1)]
ans = board[x][y]

for command in str:
    
    if command == 'L':
        idx = Ls.index((dx,dy))
        ndx,ndy = Ls[(idx + 1)%4]
        nx = x + ndx
        ny = y + ndy
        if 0<=nx<N and 0<=ny<N :
            ans += board[nx][ny]
            
            x = nx
            y = ny
            dx,dy = ndx, ndy
        else:
            continue
    elif command == 'R':
        idx = Rs.index((dx,dy))

        ndx,ndy = Rs[(idx + 1)%4]

        nx = x + ndx
        ny = y + ndy
        if 0<=nx<N and 0<=ny<N :
            ans += board[nx][ny]

            x = nx
            y = ny
            dx,dy = ndx, ndy
        else:
            continue

    else:
        nx = x + dx
        ny = y + dy

        if 0<=nx<N and 0<=ny<N :
            x = nx
            y = ny
        else:
            continue


print(ans)