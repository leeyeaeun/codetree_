n, m = map(int, input().split())

# Please write your code here.
def max_divide(n,m):
    i = 1
    max_i = 1
    for i in range(1, min(n,m)+1):
        if n % i == 0 and m % i == 0:
            max_i = i

    print(max_i)

max_divide(n,m)
    