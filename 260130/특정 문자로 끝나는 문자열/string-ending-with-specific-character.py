arr= [input() for _ in range(10)]

p = input()

ans = 0
for elem in arr:
    if elem[-1] == p:
        print(elem)
        ans +=1

if ans == 0:
    print('None')
