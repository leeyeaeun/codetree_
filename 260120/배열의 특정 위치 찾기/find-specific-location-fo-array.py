arr = list(map(int,input().split()))

arr_2 = sum(arr[1::2])
arr_3 = sum(arr[2::3]) /3

print(arr_2,f"{arr_3:.1f}")

