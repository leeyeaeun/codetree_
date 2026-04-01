n  = int(input()) 
arr = list(map(int, input().split()))


# Please write your code here.
ans = 0
import heapq 
pq = []
suffix_sum = 0

for start in range(n -1 , 0, -1):
    x = arr[start]
    heapq.heappush(pq, x)
    suffix_sum += x

    # 원소가 2개 이상 있어야 최솟값 하나 빼고 평균 가능
    if len(pq) >= 2:
        mean = (suffix_sum - pq[0]) / (len(pq) - 1)
        if mean > ans:
            ans = mean

print(f"{ans:.2f}")

    