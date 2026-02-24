n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def util():
    global n, m, A
    ans = 0
    while(m>=1):
        ans += A[m-1]
        if m == 1:
            break

        if m%2 == 1:
            m -= 1
        else:
            m //=2

    print(ans)

util()