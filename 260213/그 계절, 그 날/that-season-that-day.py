Y, M, D = map(int, input().split())

# Please write your code here.

def is_lunar_year(Y,M,D):
    if Y % 4 == 0:
        if Y %100 ==0:
            if Y % 400 == 0:
                return True
            return False
        else:
            return True
    else:
        return False
#print(is_lunar_year(1900,2,29))

def is_real_day(Y,M,D):
        if M in [1,3,5,7,8,10,12]:
            if D>=1 and D <=31:
                return True
            else:
                return False
        else:
            if D>=1 and D <=30 and M != 2:
                return True
            else:
                if M == 2 and D == 29:
                    if is_lunar_year(Y,M,D):
                        return True
                    else:
                        return False
                return False

if is_real_day(Y,M,D):
    if M>=3 and M<=5:
        print('Spring')
    elif M>=6 and M<=8:
        print('Summer')
    elif M>=9 and M<=11:
        print('Fall')
    else:
        print('Winter')
else:
    print('-1')
