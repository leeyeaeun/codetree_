n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

pq = []

for elem in arr:
    heapq.heappush(pq,-elem)

for _ in range(m):
    nbignum = heapq.heappop(pq)
    bignum = - nbignum
    bignum -= 1
    heapq.heappush(pq, -bignum)
