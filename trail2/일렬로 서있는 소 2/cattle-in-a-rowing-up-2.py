N = int(input())
A = list(map(int, input().split()))

ans = 0
# Please write your code here.
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if A[i] <= A[j] and A[j] <= A[k]:
                ans +=1

print(ans)