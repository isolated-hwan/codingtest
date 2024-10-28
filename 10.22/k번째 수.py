t = int(input())
for _ in range(t):
    n, s, e, k = map(int, input().split())
    answer = list(map(int, input().split()))
    answer = answer[s-1 : e]
    answer.sort()
    print(answer[k-1])
