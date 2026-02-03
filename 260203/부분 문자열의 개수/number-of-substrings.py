string = input()
target = input()

s= string
num = 0
while (s):
    if target in s:
        location = s.find(target)
        s = s[location+1:]
        num +=1
    else:
        break

print(num)