n = int(input())

def DFS(n):
    if n > 0:
        DFS(n//2)
        print(n % 2, end = '')




DFS(n)