n = int(input())
a = list(map(int, input().split()))
answer = 0
n = 0
for i in a:
    if i == 1:
        n += 1
        answer += n
    else: 
        n = 0
        answer += n
print(answer)