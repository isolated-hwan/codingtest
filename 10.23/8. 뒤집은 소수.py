n = int(input())
a = list(map(int, input().split()))
def reverse(x):
    x = str(x)
    x = int(x[::-1])
    return x
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True

for i in a:
    tmp = reverse(i)
    if isPrime(tmp):
        print(tmp, end= ' ')

