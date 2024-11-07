from collections import deque
n, m = map(int, input().split())
a = [(i , val) for i, val in enumerate (list(map(int, input().split())))]

a = deque(a)
cnt = 0
while True:
    first = a.popleft()
    if any(first[1] < i[1] for i in a):
        a.append(first)
    else:
        cnt += 1
        if first[0] == m:
            print(cnt)
            break



        


