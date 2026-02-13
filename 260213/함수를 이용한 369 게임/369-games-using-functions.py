a, b = map(int, input().split())
ans = 0
def is369(n):
    n = str(n)
    for i in n:
        if i== '3' or i == '6' or i == '9':
            return True
        else:
            continue 
# Please write your code here.
for i in range(a+1, b+1):
    if i % 3 == 0 or is369(i) == True:
        ans +=1
print(ans)

