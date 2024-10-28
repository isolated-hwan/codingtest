n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
# answer = a + b
# answer.sort()
# for i in answer:
#     print(i, end= ' ')

p1 = p2 = 0
c = []
while p1<n and p2<m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p1])
        p2+=1
if p1 < n:
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]
print(c)