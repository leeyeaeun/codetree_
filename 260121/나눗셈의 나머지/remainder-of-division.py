A,B = map(int,input().split())

cnt = [0] * 10
p = 0
while(A>1):
    
    A , p = A//B, A%B
    cnt[p] +=1

#print(cnt)
total = 0
for i in range(10):
    total += cnt[i] ** 2
 
print(total)