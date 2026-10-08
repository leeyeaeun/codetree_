n, m = map(int, input().split())
t = []
c = []
import sys
INF = 10**9

# dp[x] = x원을 만드는 최소 동전 개수
dp = [INF] * (m + 1)
dp[0] = 0


for _ in range(n):
    coin_type, value = input().split()
    value = int(value)

    # B : 한 번만 사용 가능
    if coin_type == 'B':

        # 뒤에서부터
        for money in range(m, value - 1, -1):

            if dp[money - value] != INF:
                dp[money] = min(
                    dp[money],
                    dp[money - value] + 1
                )

    # 무제한 사용 가능
    else:

        # 앞에서부터
        for money in range(value, m + 1):

            if dp[money - value] != INF:
                dp[money] = min(
                    dp[money],
                    dp[money - value] + 1
                )


if dp[m] == INF:
    print(-1)
else:
    print(dp[m])