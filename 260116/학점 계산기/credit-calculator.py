n = int(input())
arr =list(map(float,input().split()))

total = sum(arr)/ len(arr)
print(f"{total:.1f}")
if total >=4:
    print('Perfect')
elif total >= 3.0:
    print('Good')
else:
    print('Poor')