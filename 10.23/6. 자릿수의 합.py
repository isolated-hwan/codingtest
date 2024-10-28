n = int(input())

def digit_sum(x):
    x = str(x)
    sum = 0
    for i in range(len(x)):
        sum += int(x[i])
    return sum 

a = list(map(int, input().split()))
print(a)
result = 0
for i in a:
    tot = digit_sum(i)
    if tot > result:
        result = tot
        res = i
print(res)
