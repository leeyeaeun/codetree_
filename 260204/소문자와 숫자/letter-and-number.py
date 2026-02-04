s = input()

for i in s:
    if i.isdigit():    
        print(i,end="")
    elif i.isalpha():
        print(i.lower(),end="")
    else:
        continue