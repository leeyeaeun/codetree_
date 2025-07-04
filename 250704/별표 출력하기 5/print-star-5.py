N = int(input())

for i in range(N):
    for j in range(0,N-i):
        print("*"*(N-i), end=" ")
    print()