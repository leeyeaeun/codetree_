a = [i for i in input() if i.isdigit()]
b = [i for i in input() if i.isdigit()]

s=""
sb =""
for i in a:
    s += i

for i in b:
    sb += i 
s = int(s)
sb = int(sb)   
print(s+sb)