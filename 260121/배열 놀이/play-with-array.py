N,Q= map(int,input().split())

arr = list(map(int,input().split()))

while(True):
    try:
        commands = list(map(int,input().split()))
        if commands[0] == 1:
            print(arr[commands[1]-1])
        elif commands[0] == 2:
            if (commands[1]) in arr:
                print(arr.index(commands[1])+1)
            else:
                print(0)
        else:
            s,e =commands[1], commands[2]
            print(*arr[s-1:e])


    except EOFError:
        break