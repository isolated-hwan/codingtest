def DFS(l):
    global cnt
    if l == n:
        cnt+=1
    else:
        for i in range(1, n+1):
            if v[l][i] == 1 and ch[i] == 0:
                ch[i] = 1
                DFS(i)
                ch[i] = 0



n, m = map(int, input().split())

v = [[0] * (n+1) for _ in range(n+1)]
ch = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    v[a][b] = 1

cnt = 0
ch[1] = 1
DFS(1)
print(cnt)