N = int(input())

arr = [1,N]

while(True):
    a,b = arr[-1],arr[-2]
    arr.append(a+b)
    if a+b > 100:
        break
print(*arr, sep=" ")