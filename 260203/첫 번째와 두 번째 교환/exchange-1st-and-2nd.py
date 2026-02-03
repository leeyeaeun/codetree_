s = list(input())

a = s[0]
b = s[1]

s = [b if x == a else a if x == b else x for x in s]
print(*s, sep="")

