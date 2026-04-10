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
        dx, dy = Ls[(idx + 1)%4]

    elif command == 'R':
        idx = Rs.index((dx,dy))
        #print(idx)
        dx, dy = Rs[(idx + 1)%4]
        #print(ndx,ndy)

    else:
        nx = x + dx
        ny = y + dy
        if 0<=nx<N and 0<=ny<N :
            x = nx
            y = ny
            ans += board[x][y]
        else:
            continue            
        
        #print(board[nx][ny])


print(ans)