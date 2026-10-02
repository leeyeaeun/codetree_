n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

def not_carry(a,b,c):
    while a or b or c:
        num = a%10 + b%10 + c%10
        if num >=10:
            return False

        a = a//10
        b = b//10
        c = c//10

    return True

ans = -1
for i in range(n):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if not_carry(arr[i],arr[j],arr[k]):
                ans = max(ans, arr[i]+arr[j]+arr[k])

print(ans)
