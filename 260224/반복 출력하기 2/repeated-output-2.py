n = int(input())

# Please write your code here.

def reHello(n):
    if n == 0:
        return
    print('HelloWorld')
    reHello(n-1)
    
reHello(n)