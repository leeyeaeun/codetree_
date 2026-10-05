S = input()

K,M = map(int, input().split())

cnt = {}

p = 0
for i in range(K):
    p = p*2 + (ord(S[i]) - ord('0'))


cnt[p] = 1

for i in range(K,len(S)):

    old_bit = int(S[i-K]) # 맨 앞에있는 비트
    new_bit = int(S[i])

    p = p * 2
    p = p - old_bit * (2 ** K)
    p = p + new_bit

    if p in cnt:
        cnt[p] +=1
    else:
        cnt[p] = 1

flag = False

for value in cnt.values():
    if value >=M:
        flag = True
        break

print(int(flag))