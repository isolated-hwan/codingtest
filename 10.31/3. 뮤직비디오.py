n, m = map(int, input().split())

a = list(map(int, input().split()))

def cnt(len):
    cnt = 1
    sum = 0
    for i in a:
        if sum + i > len:
            cnt += 1
            sum = i
        else:
            sum += i
    return cnt

maxx = max(a)
lt = 1
rt = sum(a)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if maxx <= mid and cnt(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)