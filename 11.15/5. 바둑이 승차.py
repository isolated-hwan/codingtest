def DFS(l , sum, tsum):
    global answer
    if sum + (total - tsum) < answer:
        return
    if sum > c:
        return 
    if l == n:
        if sum > answer:
            answer = sum
    else:
        DFS(l + 1, sum + a[l], tsum+a[l])
        print(sum, tsum)
        DFS(l + 1, sum, tsum+a[l])



c, n = map(int, input().split())
a = [0] * n
answer = -2147000000
for i in range(n):
    a[i] = (int(input()))
total = sum(a)
DFS(0, 0, 0)
print(answer)
 
