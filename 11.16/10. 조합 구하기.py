def DFS(l, s):
    global cnt
    if l == m:
        for j in range(m):
            print(res[j], end = ' ')
        cnt +=1     
        print()
    else:
        for i in range(s, n+1):
            res[l] = i
            DFS(l+1, i+1) 

n, m = map(int, input().split())
cnt = 0
res = [0] * (n+1)
DFS(0, 1)
print(cnt)