N1,N2 = map(int,input().split())

arr1 = list(map(int,input().split())) 
arr2 = list(map(int,input().split())) 

cnt = None

for i in range(N1-N2+1):
    if arr1[i] == arr2[0]:
        if arr1[i:i+N2] == arr2:
            cnt = 'Yes'
            break
    cnt = 'No'
print(cnt)
