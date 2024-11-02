n = int(input())
a = list(map(int , input().split()))

res = ''
lt = 0
rt = n-1
rv = 0
tmp = []

while lt <= rt:
    if a[lt] > rv:
        tmp.append((a[lt], 'L'))
    if a[rt] > rv:
        tmp.append((a[rt], 'R'))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res += tmp[0][1]
        rv = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1 
        tmp.clear()
print(res)