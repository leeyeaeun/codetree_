A = input()

# Please write your code here.

result= []
cnt = 1

ans = 0
for i in range(1,len(A)):
    if A[i] == A[i-1]:
        cnt +=1
        
    else:
        result.append( A[i-1] + str(cnt))
        ans += len(str(cnt)) + 1
        cnt = 1

result.append(A[-1] + str(cnt))
ans += len(str(cnt)) + 1
print(ans)
print(*result, sep ="")