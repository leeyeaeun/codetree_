n = int(input())

# Please write your code here.

def sum_num(N):
    ans = 0
    for i in range(N+1): 
        ans += i 
    return ans // 10
print(sum_num(n))