n = int(input())

# a = []
# for _ in range(n):
#     a.append(list(map(int, input().split())))

# max_r = 0
# for i in range(n):
#     r_sum = 0
#     for j in range(n):
#         r_sum += a[i][j]
#     if r_sum > max_r:
#         max_r = r_sum
# a.append(max_r)

# max_c = 0
# for i in range(n):
#     l_sum = 0
#     for j in range(n):
#         l_sum += a[j][i]
#     if l_sum > max_c:
#         max_c = l_sum
# a.append(l_sum)

a = [list(map(int, input().split())) for _ in range(n)]
large = 0
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > large:
        large = sum1
    if sum2 > large:
        large = sum2
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > large:
    large = sum1
if sum2 > large:
    large = sum2
print(large)

