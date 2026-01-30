a =input()
b =input()
c =input()

ab = abs(len(a)-len(b))
bc = abs(len(c)-len(b))
ca = abs(len(a)-len(c))

ans = ab
if ans < bc:
    ans= bc
if ans < ca:
    ans = ca

print(ans)