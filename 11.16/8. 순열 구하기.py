def DFS(l):
    global cnt
    if l == m:
        for j in range(l):
            print(res[j], end= ' ')
        print()
        cnt+=1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i
                DFS(l+1)
                ch[i] = 0

n, m = map(int, input().split())
res = [0] * n
ch = [0] * (n+1)
cnt = 0

DFS(0)
print(cnt)