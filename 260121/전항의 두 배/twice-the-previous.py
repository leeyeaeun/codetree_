A1,A2 = map(int,input().split())

for _ in range(10):
    print(A1,end=" ")
    A1, A2 = A2, 2*A1 + A2
