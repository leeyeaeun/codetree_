n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max = 0
i = 0
def f():
    global arr
    global i
    global max

    if i == n:
        return 
    if max < arr[i]:
        max = arr[i]
    
    i +=1
    return f()

f()
print(max)