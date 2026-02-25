N = int(input())

# Please write your code here.
def f(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    if  n %2 == 1:
        return n + f(n-2)
    else:
        return n + f(n-2)

print(f(N))