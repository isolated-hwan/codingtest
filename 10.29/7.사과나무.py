n = int(input())

a = [list(map(int, input().split()))for _ in range(n)]

answer = 0

start, end = n//2
for i in range(n):
    for j in range(start, end + 1):
        answer += a[i][j]
    if i < n//2:
        start -=1
        end += 1
    else:
        start += 1
        end -= 1

print(answer)