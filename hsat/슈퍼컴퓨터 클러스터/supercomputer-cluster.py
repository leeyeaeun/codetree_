import sys
from math import isqrt

N, B = map(int, input().split())
a = list(map(int, input().split()))
# d만큼 향상시키는데 d^2원
a.sort()

# 모든 컴퓨터를 mid 이상으로 만들 수 있는지
def check(mid):
    cost = 0

    for x in a:
        if x < mid:
            cost += (mid - x) ** 2

        if cost > B:
            return False

    return True


left = min(a)
right = min(a) + isqrt(B) # 상한 정하는게 포인트

answer = left

while left <= right:
    mid = (left + right) // 2

    if check(mid):
        answer = mid
        left = mid + 1

    else:
        right = mid - 1

print(answer)
