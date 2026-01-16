arr = list(map(int,input().split()))

total = 0
num = 0
for elem in arr:
    if elem >=250:
        break;
    else:
        num +=1
        total += elem
  
print(total, f"{total/(num):.1f}")
