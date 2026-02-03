input_str = input()
target_str = input()

# Please write your code here.
if target_str in input_str:
    print(input_str.find(target_str))
else:
    print(-1)