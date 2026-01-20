N = int(input())
arr = list(map(int, input().split()))

new_arr=[]

for elem in arr[::-1]:
    if elem %2 == 0:
       print(elem, end=" ")

