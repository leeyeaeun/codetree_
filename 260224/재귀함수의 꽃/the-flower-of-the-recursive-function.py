N = int(input())

# Please write your code here.

def A(N):
    if N == 0:
        return
    print(N, end= " ")
    A(N-1)
    print(N, end=" ")

A(N)