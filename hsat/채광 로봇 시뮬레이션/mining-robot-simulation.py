MAX_N = 1005       
MIN_VALUE = -int(1e9)


def  calculate_mx(i,j,x,y,passed_time, profit):
#  모든 칸 A에 대해

#    A가 "t초 전 위치"였다고 가정한다.

#    A에서 오른쪽/아래로 정확히 t초 동안
#    갈 수 있는 모든 경로를 확인한다.

#    t초 후 끝점에서 시간역행해서 A로 돌아온다고 했을 때
#    얻는 추가 점수의 최댓값을 mx[A]에 저장한다.


    if passed_time == t:
        mx[i][j] = max(mx[i][j], profit)
        return
        
    if x+1 <= n:
        calculate_mx(i, j, x+1, y, passed_time+1, profit + a[x+1][y])
    
    if y+1 <= n:
        calculate_mx(i, j, x, y+1, passed_time+1, profit + a[x][y+1])

n, t = map(int,input().split())
a = [[0] * (MAX_N) for _ in range(MAX_N)]
mx = [[MIN_VALUE]*(MAX_N) for _ in range(MAX_N)]
dp = [[[MIN_VALUE] * 2 for _ in range(MAX_N)] for _ in range(MAX_N)] # dp [i][j][0] 이랑.. dp[i][j][1]

for i in range(1, n+1):
    a[i][1:] = list(map(int,input().split()))


for i in range(1,n+1):
    for j in range(1,n+1):
        mx[i][j] = MIN_VALUE
        dp[i][j][0] = dp[i][j][1] = MIN_VALUE

for i in range(1,n+1):
    for j in range(1,n+1):
        calculate_mx(i,j,i,j,0,a[i][j])

#   상태 0 = 시간역행 아직 안 씀
#   상태 1 = 시간역행 이미 씀
dp[1][1][0] = a[1][1]

for i in range(1, n+1):
    for j in range(1,n+1):
        # (i,j)를 t초 전 위치로 하여
        # 시간역행을 지금 한 번 사용하는 경우
        dp[i][j][1] = max(dp[i][j][1], dp[i][j][0] + mx[i][j])

        if i+1<=n:
            dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j][0] + a[i+1][j])
            dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][1] + a[i+1][j])

        if j+1<=n:
            dp[i][j+1][0] = max(dp[i][j+1][0], dp[i][j][0] + a[i][j+1])
            dp[i][j+1][1] = max(dp[i][j+1][1], dp[i][j][1] + a[i][j+1])

print(max(dp[n][n][0], dp[n][n][1]))