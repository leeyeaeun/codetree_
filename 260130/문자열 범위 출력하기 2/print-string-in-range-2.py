arr = input()
N = int(input())

for elem in arr[len(arr): len(arr)-N -1:-1]:
    print(elem, end="")