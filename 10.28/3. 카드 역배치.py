a = list(i for i in range(0, 21))
for _ in range(10):
    start, end = map(int, input().split())
    for i in range((end - start + 1)//2):
        a[start + i], a[end - i] = a[end - i], a[start + i]
a.pop(0)
for x in a:
    print(x, end = ' ')

