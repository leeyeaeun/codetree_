n = int(input())
a = list(map(int, input().split()))

# Please write your code here.
index = n-1
while(index != 0):
    print(a.index(max(a))+1, end=" ")
    index = a.index(max(a))
    a= a[:index]

