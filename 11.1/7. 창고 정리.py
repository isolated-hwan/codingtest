n = int(input())
a = list(map(int, input().split()))
m = int(input())
a.sort()
for _ in range(m):
    a[0] += 1
    a[-1] -= 1
    a.sort()
print(a[-1] - a[0])

