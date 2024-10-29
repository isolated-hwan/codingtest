n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for _ in range(m):
    r, t, c = map(int, input().split())
    if t == 0:
        for _ in range(c):
            a[r-1].append(a[r-1].pop(0))
    else:
        for _ in range(c):
            a[r-1].insert(0, a[r-1].pop())

start = 0
end = n-1
answer = 0 
for i in range(n):
    for j in range(start, end +1):
        answer += a[i][j]
    if i < n//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(answer)