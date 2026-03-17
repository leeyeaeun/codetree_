N = int(input())

# Please write your code here.
grid = [0] * (N+1) 
from collections import deque
q = deque()
q.append((N))
visited = [-1] * (N+1)
visited[N] = 0


def bfs():

    while q:
        x = q.popleft()        
        nxs = [x+1,x-1]
        if x %2 == 0:
            nxs.append(x//2)
        if x%3 ==0:
            nxs.append(x//3)
        #print(nxs)

        for nx in nxs:
            #print(nx)
            if 0<= nx <N and visited[nx] == -1:
        
                #print('True :', nx)
                visited[nx] = visited[x] + 1
                q.append(nx)

bfs()
#print(visited)
print(visited[1])

