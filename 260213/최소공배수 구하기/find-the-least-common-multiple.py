n, m = map(int, input().split())

# Please write your code here.
def min_common(n,m):
    i = 1
    j=1
    while(True):
        if n * i == m * j:
            print(n*i)
            break
        if n * i > m* j:
            j+=1
        else:
            i+=1
min_common(n,m)