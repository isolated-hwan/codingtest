k, n = map(int, input().split())
a = []

def cal(len):
    cnt = 0
    for i in a:
        cnt += i // len
    return cnt

large = 0
for _ in range(k):
    tmp = int(input())
    a.append(tmp)
    large = max(large, tmp)

lt = 1
rt = large
res = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if cal(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)
