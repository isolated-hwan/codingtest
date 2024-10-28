n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000
for idx, i in enumerate(a):
    tmp = abs(ave - i)
    if min > tmp:
        min = tmp
        score = i
        res = idx + 1
    elif tmp == min:
        if i > score:
            score = i
            res = idx + 1
print(ave, res)
