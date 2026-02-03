a = list(input())
while(len(a)>1):
    p = int(input())
    if p >= len(a):
        a.pop(-1)
        print(*a, sep="")
        continue
    a.pop(p)
    print(*a, sep="")

    