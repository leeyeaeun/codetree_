N = int(input())

m = 0
printing = N

while(m < 2):
    if printing % 5 == 0 and printing != 0:
        m +=1
    print(printing, end = " ")
    printing += N
    
