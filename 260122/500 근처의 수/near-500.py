arr = list(map(int, input().split()))

arr_b = [elem for elem in arr if elem < 500]
arr_c = [elem for elem in arr if elem > 500]


print(max(arr_b), min(arr_c))