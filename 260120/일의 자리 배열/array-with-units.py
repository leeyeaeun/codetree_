a,b = map(int,input().split())
print(a,b, end = " ")
for _ in range(8):
    a,b = b, a+b
    print(b%10 ,end=" ")