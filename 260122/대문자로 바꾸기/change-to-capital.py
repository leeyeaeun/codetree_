arr = [
    list(input().upper().split())
    for _ in range(5)
]

for row in arr:
    print(*row)