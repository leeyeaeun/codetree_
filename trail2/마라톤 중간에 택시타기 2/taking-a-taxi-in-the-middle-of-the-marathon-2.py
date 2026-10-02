n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

xs = [p[0] for p in points]
ys = [p[1] for p in points]

# Please write your code here.
total = 0

def dist(i, j):
    return abs(xs[i] - xs[j])+ abs(ys[i] - ys[j])

for i in range(n-1):
    total += dist(i,i+1)

min_meter = total

for i in range(1,n-1):
    new_meter = total

    new_meter -= dist(i-1,i)
    new_meter -= dist(i,i+1)
    new_meter += dist(i-1,i+1)

    min_meter = min(new_meter,min_meter)

print(min_meter)