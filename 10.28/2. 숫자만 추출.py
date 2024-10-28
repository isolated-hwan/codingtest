a = input()
answer = []
for i in a:
    if i.isdigit():
        answer.append(i)
str = ''.join(answer)
str = int(str)
print(str)
cnt = 0
for i in range(1, str + 1):
    if str % i == 0:
        cnt += 1
print(cnt)