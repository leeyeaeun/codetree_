N = int(input())
arr = [input() for _ in range(N)]
p = input()

ans = 0
ans_len = 0

for elem in arr:
    if elem[0] == p:
        ans += 1
        ans_len += len(elem)

#print(ans)
print(ans, f'{ans_len/ans:0.2f}')