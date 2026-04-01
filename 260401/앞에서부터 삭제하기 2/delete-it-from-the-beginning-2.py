n  = int(input()) 
arr = list(map(int, input().split()))


# Please write your code here.
meanlist = []
import heapq 
for i in range(n -2):
    remain = arr[i+1:]
    pq = []
    for elem in remain:
        heapq.heappush(pq,elem)
    heapq.heappop(pq)
    mean = sum(pq)/ len(pq)
    heapq.heappush(meanlist, -mean)

print(f"{-meanlist[0]:.2f}")

    