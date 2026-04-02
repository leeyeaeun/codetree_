t = int(input())
import heapq
for _ in range(t):
    m = int(input())
    arr = list(map(int, input().split()))

    # Please write your code here.
    pq = [] # 작은애들 저장 
    npq = [] # 큰애들 저장
    # 크기가 둘이 다르면 pop
    for elem in arr:
        if not npq or -npq[0] >= elem:
            heapq.heappush(npq, -elem)
        else:
            heapq.heappush(pq,elem)

        if len(npq) > len(pq) + 1:
            heapq.heappush(pq, -heapq.heappop(npq))
        elif len(pq)  > len(npq):
            heapq.heappush(npq, -heapq.heappop(pq))
        ###print(pq, npq)

        if (len(pq) +len(npq)) % 2 == 1:
            print(-npq[0], end = " ")
    print()