n = int(input())
dic = {}

for i in range(n):
    a = input()
    dic[a] = 0

for i in range(n-1):
    a = input()
    dic[a] = 1

for k, v in dic.items():
    if v == 0:
        print(k)
        break