from collections import deque

n, m, k = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

start_points = list(map(lambda x: int(x) - 1, input().split()))
 
max_dist = [0] * (n)
reachable = [0] * (n)

for start in start_points: 
    q = deque([start])

    dist = [-1] * (n)
    dist[start] = 0

    while q:
        cur = q.popleft()
        
        for nxt in graph[cur]:

            if dist[nxt] != -1:
                continue
            
            dist[nxt] = dist[cur] + 1
            q.append(nxt)

    for v in range(n):
        if dist[v] == -1:
            continue
        
        reachable[v] +=1
        max_dist[v] = max(max_dist[v], dist[v])

answer = -1
import sys
INF = sys.maxsize
best = INF

for v in range(n):
    if reachable[v] != k:
        continue

    if max_dist[v] < best:
        best = max_dist[v]
        answer = best

# print(max_dist)
# print(reachable)
print( answer )