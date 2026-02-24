N = int(input())

# Please write your code here.
def summ(N):
    if N == 1:
        return 1
    return N + summ(N-1)
print(summ(N))