def DFS(l, sum):
    global res
    if l == n+1:
        if sum < res:
            res = sum
    else:
        if l + t[l] <= n+1:
            DFS(l + t[l], sum + p[l])
        DFS(l + 1, sum)

n = int(input())
t = []
p = []
for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
res = -2147000000
t.insert(0,0)
p.inser(0,0)
DFS(1, 0)