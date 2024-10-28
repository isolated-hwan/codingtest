n, m = map(int, input().split())

cnt_list = [0] * (n + m + 3)
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt_list[i + j] += 1

max = 0
for i in range(len(cnt_list)):    
    if max < cnt_list[i]:
        max = cnt_list[i]
for i in range(len(cnt_list)):
    if max == cnt_list[i]:
        print(i, end= ' ') 