n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

count = 0

for i in range(n):
    for j in range(i+1,n):
        if price[j]-price[i] > count:
            count = price[j]-price[i]

print(count)