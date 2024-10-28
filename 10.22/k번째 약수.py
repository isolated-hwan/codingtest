n, k = map(int, input().split())

answer = []

for i in range(n, 0, -1):
    if n % i == 0:
        answer.append(i)
answer.sort()

if len(answer) < k:
    print(-1)
else:       
    print(answer[k-1])