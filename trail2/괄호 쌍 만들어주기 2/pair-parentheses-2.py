A = input()

# Please write your code here.
length = len(A)
cnt = 0
for i in range( length-1 ):
    if A[i] == A[i+1] == '(' :
        for j in range( i+2, length-1 ):
            if A[j]==A[j+1]==')':
                cnt +=1

print(cnt)