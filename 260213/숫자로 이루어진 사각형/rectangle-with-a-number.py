n = int(input())

# Please write your code here.
def square(N):
    i = 1
    for _ in range(N):
        for _ in range(N):
            if i == 10:
                i = 1
            print(i,  end =" ")
            i+=1
        print()
square(n)