s = input()
command = list(input().rstrip())

for i in range(len(command)):
    c = command[i]
    #print(c)
    if c == 'L':
        s = s[1:] + s[0]
    else:
        s = s[-1] + s[:-1]

print(s)