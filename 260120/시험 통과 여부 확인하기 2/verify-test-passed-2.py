N = int(input())
arr = [sum(list(map(int, input().split())))/4 for _ in range(N)]
n =0
#print(arr)
for elem in arr:
    if elem > 60:
        print('pass')
        n+=1
    else:
        print('fail')
print(n)