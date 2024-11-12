def DFS(v):
    if v > 7:
        return
    else:
        # print(v, end = " ") # 전위 순회
        DFS(v*2)
        # print(v, end = " ") # 중위 순회
        DFS(v*2 + 1 )
        # print(v, end = " ") # 후위 순회

DFS(1) 