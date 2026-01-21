arr = [0] * 4 #(A,B,C,D,E)
i = 0
while(True):
    try:
        status , temp = input().split()
        status = str(status)
        temp = int(temp)
        i +=1
        if status == "N":
            if temp >= 37:
                arr[1] += 1
            else:
                arr[3] += 1
        else:
            if temp >=37:
                arr[0] += 1
            else:
                arr[2] += 1
        if (i == 3 and arr[0] >= 2 ):
            arr.append('E')
        
    except EOFError:
        break



print(*arr, sep= " ")