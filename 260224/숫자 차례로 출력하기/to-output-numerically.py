n = int(input())

# Please write your code here.

def printA(n):
    if n== 0:
        return
    print(n, end =" ")
    printA(n-1)

def printB(n):
    if n== 0:
        return
    printB(n-1)
    print(n, end=" ")

printB(n)
print()
printA(n)
