a = input()
x = a[1]
y = a[0]
a = [y if i ==x else i for i in a]
print(*a, sep="")