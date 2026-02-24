n = int(input())

# Please write your code here.
def star(n):
    if n == 0:
        return
    star(n-1)
    for _ in range(n):
        print('*', end="" )
    print()

star(n)