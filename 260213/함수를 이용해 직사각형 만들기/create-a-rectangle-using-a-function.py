n, m = map(int, input().split())

# Please write your code here.
def print_rec(n, m):
    for _ in range(n):
        for _ in range(m):
            print('1',end="")
        print()

print_rec(n,m)
