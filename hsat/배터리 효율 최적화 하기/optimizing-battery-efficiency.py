n, m = map(int, input().split())

board = [
    list(map(int, input().split()))
    for _ in range(n)
]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def get_neighbors(x, y):
    neighbors = []

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<= nx < n and 0 <= ny < m:
            neighbors.append((nx,ny))

    return neighbors 

modules = set() #5칸짜리 모듈들

def backtrack(chosen, candidates):

    if len(chosen) == 5:
        modules.add(tuple(sorted(chosen)))
        return
    
    for cell in list(candidates):
        new_chosen = set(chosen)
        new_chosen.add(cell)

        new_candidates = set(candidates)
        new_candidates.remove(cell)

        x,y = cell

        for nx, ny in get_neighbors(x,y):
            if (nx,ny) not in new_chosen:
                new_candidates.add((nx,ny))

        backtrack(new_chosen, new_candidates)

for i in range(n):
    for j in range(m):

        start = (i,j)

        chosen = {start}
        candidates = set(get_neighbors(i, j)) 

        backtrack(chosen, candidates)


modules = [set(module) for module in modules]

scores = []

for module in modules:
    score = 0

    for x,y in module:
        score += board[x][y]

    scores.append(score)

ans = -10**18

for i in range(len(modules)):
    for j in range(i+1, len(modules)):

        overlap = modules[i] & modules[j]

        if len(overlap) ==2:
            ans = max(ans, scores[i]+ scores[j])

print(ans)