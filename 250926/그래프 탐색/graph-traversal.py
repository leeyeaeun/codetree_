n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
graph= [[] for _ in range(n+1)]

for x,y in edges:
    graph[x].append(y)
    graph[y].append(x)


visited = [False] * (n+1)
visited[1] = True
ans = 0

def dfs(root):
    visited[root] = True
    max_depth = 0
    for daugther in graph[root]:
        if visited[daugther] == False:
            depth = dfs(daugther)
            max_depth = max(max_depth, depth)

    return max_depth + 1


print(dfs(1)-1)
