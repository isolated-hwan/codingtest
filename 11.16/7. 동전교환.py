n = int(input())
a = list(map(int, input()))
m = int(input())

def DFS(l, sum):
    global min_cnt
    if l > min_cnt:
        return
    if sum > m:
        return
    if sum == m:
        if l < min_cnt:
            min_cnt = l
    else:
        for i in range(n):
            DFS(l+1, sum + a[i])


min_cnt = 2147000000
a.sort(reverse = True)
DFS(0, 0)
print(min_cnt)