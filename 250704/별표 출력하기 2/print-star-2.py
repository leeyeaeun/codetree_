N = int(input())

for i in range(N):
    #print(f"i :{i}",)
    for j in range(0, N - i):
        print("*" , end=" ")
    print()