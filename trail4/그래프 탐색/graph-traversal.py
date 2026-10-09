def dfs(v):
    global count
    for curr in graph[v]:
        if not visited[curr]:
            visited[curr] = True
            count += 1
            dfs(curr)

n, m =  map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())

    graph[x-1].append(y-1)
    graph[y-1].append(x-1)

visited = [False] * n
visited[0] = True
count = 0
dfs(0)


print(count)