n, m = map(int, input().split())

graph = [[] for _ in range(n)]
reverse_graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1

    graph[a].append(b)
    reverse_graph[b].append(a)

S, T = map(int, input().split())
S -= 1
T -= 1


def dfs(start, graph, end_point=-1):
    visited = [False] * n

    # 목적지를 통과하지 못하게 처리
    if end_point != -1:
        visited[end_point] = True

    visited[start] = True
    stack = [start]

    while stack:
        x = stack.pop()

        for v in graph[x]:
            if visited[v]:
                continue

            visited[v] = True
            stack.append(v)

    return visited


# 1. S에서 출발 (T 통과 금지)
from_s = dfs(S, graph, T)

# 2. T에서 출발 (S 통과 금지)
from_t = dfs(T, graph, S)

# 3. T로 도착할 수 있는 정점
to_t = dfs(T, reverse_graph)

# 4. S로 도착할 수 있는 정점
to_s = dfs(S, reverse_graph)


answer = 0

for i in range(n):
    if i == S or i == T:
        continue

    if from_s[i] and from_t[i] and to_t[i] and to_s[i]:
        answer += 1

print(answer)