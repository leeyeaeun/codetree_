n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
meter = [0]*n

for i in range(n):
    for j in range(n):
        meter[i] +=  A[j] * abs(i-j)

print(min(meter))