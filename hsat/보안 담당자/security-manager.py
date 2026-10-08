N = int(input())
S = input()

if N % 2 != 0:
    print('No')
    exit()

cnt0 = S.count(')') #나간사람갯수

# 나간사람이랑 들어온 사람 둘다 갯수가 N/2 여야함
need0 = N//2 - cnt0 # 물음표중에.. 나간 기록이어야 하는 수
check =  0 # 들어온 직원수 - 나간 직원수 차이 기록

# 뒤에서부터 검사.

for i in range(N-1, -1, -1):
    if S[i] == '(': # 들어오다
        check +=1 

    elif S[i] == ')': # 나가다
        check -= 1
    
    else:
        if need0 > 0:
            check -=1
            need0 -=1
        else:
            check +=1

    if check > 0: # 뒤에서부터 검사를 하는데 들어온 직원수가 더 많아..
        print("No")
        exit()

    
if check == 0:
    print("Yes")
else:
    print("No")