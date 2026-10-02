a = input()

# Please write your code here.

a2 = int(a,2)

maxi = 0

for i in range(len(a)):
    if a[i] == '0':
        a_new = a[:i] + '1' + a[i+1:]
    else:
        a_new = a[:i] + '0'+ a[i+1:]
    
    a_new_10 = int(a_new,2)
    #print(maxi)
    maxi = max(maxi, a_new_10)
    #print(i , a_new, a_new_10)

print(maxi)