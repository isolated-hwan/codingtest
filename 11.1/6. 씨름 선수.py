n = int(input())

a = []

for _ in range(n):
    h, w = map(int, input().split())
    a.append((h, w))

a.sort(reverse=True)

cnt  = 0
large_w = 0
for h, w in a:
    if w > large_w:
        large_w = w
        cnt+=1

print(cnt)
