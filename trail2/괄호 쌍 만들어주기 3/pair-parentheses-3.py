A = input()

# Please write your code here.
ans = 0

for i in range(len(A)):
    if A[i] == '(':
        for j in range(i+1, len(A)):
            if A[j] == ')':
                ans +=1

print(ans)
