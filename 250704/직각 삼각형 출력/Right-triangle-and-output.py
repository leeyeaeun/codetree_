N = int(input())

for i in range(N):
    for j in range(2*(i+1)-1):
        print("*",end="")
    print()