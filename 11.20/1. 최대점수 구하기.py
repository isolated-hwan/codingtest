def DFS(l, vsum , tsum):
    global res
    if tsum > m:
        return
    if l == n:
        if vsum > res:
            res = vsum
    else:
        DFS(l+1, vsum + v[l], tsum + t[l])
        DFS(l+1, vsum, tsum) 

n, m = map(int, input().split())


v = []
t = []
for i in range(n):
    a, b = map(int, input().split())
    v.append(a)
    t.append(b)

res = -2147000000
DFS(0, 0 ,0)
print(res)