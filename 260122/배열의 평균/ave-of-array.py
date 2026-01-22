arr = [
    list(map(int,input().split()))
    for _ in range(2)
]


a_t = 0
b_t = 0
total = 0
for i in range(2):
    a_t = 0
    for j in range(4):
        #print(i,j)
        a_t += arr[i][j]
    print(f"{a_t/4:0.1f}", end =" ") ## 가로 합.... 이고

print()
for i in range(4):
    b_t = 0
    for j in range(2):
        #print(j, i)
        b_t += arr[j][i]
        total += arr[j][i]
    print(f"{b_t/2:0.1f}", end =" ") ## 세로 합.... 이고

print()
print(f"{total/8:0.1f}", end =" ")