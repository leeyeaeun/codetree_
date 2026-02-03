s = input()
print(s)
for _ in range(len(s)):
    s = s[-1] + s[:-1]
    print(s)