n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
for i in range(1, n):
    for j in range(0, i):  # 앞의 숫자
        if a[i] < a[j]:
            dp[i] = max(dp[j] + 1, dp[i])
print(n - max(dp))
