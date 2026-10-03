board = [list(map(int, input().split())) for _ in range(19)]

# Please write your code here.


some_win = False
for i in range(19):
        for j in range(15):
            if board[i][j] !=0:
                if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4]:

                    print(board[i][j])
                    print(i+1,j+3)
                    some_win = True
                    break

                if i<=14 : 
                    if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] :
                        
                        print(board[i][j])
                        print(i+3,j+1)
                        some_win = True
                        break

                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4]:
                        print(board[i+2][j+2])
                        print(i+3,j+3)
                        some_win = True
                        break
                
                if i >=4: 
                    if board[i][j] == board[i-1][j+1] == board[i-2][j+2] == board[i-3][j+3] == board[i-4][j+4]:
                        print(board[i-2][j+2])
                        print(i-1,j+3)
                        some_win = True
                        break
                


if not some_win: 
    print(0)