def compare(x, y, z):
    if z == '<':
        if x > y:
            return False
    else:
        if x < y:
            return False
    return True

def DFS(l, num):
    if l == k+1:
        res.append(num)
        return
    for i in range(10):
        if ch[i] == 0:
            if l == 0 or compare(num[l-1], str(i), a[l-1]):
                ch[i] = 1
                DFS(l + 1, num + str(i))
                ch[i] = 0


k = int(input())
a = list(input().split())

ch = [0] * 10
res = []
DFS(0, '')

res.sort()
print(res[-1])
print(res[0])