N = int(input())

for i in range(N):
    for j in range(i+1):
        print("*", end = "")
    print("\n")

for i in range(N-2,-1,-1):
    for j in range(i+1):
        print("*", end = "")
    print("\n")