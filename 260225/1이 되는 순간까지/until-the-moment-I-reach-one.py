N = int(input())

# Please write your code here.

def f(n):
    num = 0
    if n == 1:
        return 0

    if n %2 == 0:
        return 1 + f(n//2)
    else:
        return 1 + f(n//3)

print(f(N))
