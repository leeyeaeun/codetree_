A = list(input())
B = list(input())

# Please write your code here.
while True:
    found = False
    for i in range(len(A)- len(B) +1 ):
        #print(i,A,B)
        if A[i : i+len(B)] == B:
            del A[i:i+len(B)]
            found = True
            break
    if not found:
        break

print(*A, sep="")
    # 인덱스 찾기..
    # A 에서 그 인덱스.. 빼버림
