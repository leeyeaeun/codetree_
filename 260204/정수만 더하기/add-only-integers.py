s =input()

a = list( x for x in s if x.isdigit())

a = [int(x) for x in a]

print(sum(a))