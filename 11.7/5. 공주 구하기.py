from collections import deque
n, k = map(int, input().split())
a = [i for i in range(1, n+1)]

a = deque(a)

while a:
    for _ in range(k-1):
        a1 = a.popleft()
        a.append(a1)
    a.popleft()
    print(a)
    if len(a) == 1:
        print(a[0])
        a.popleft()

