s = input()

if len(s) % 2  == 0:
    print(s[-1:0:-2])
else:
    print(s[-2:0:-2])
