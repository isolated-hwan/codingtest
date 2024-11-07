from collections import deque
r = input()
n = int(input())

# for _ in range(n):
#     tmp = []
#     a = input()
#     a = deque(a)
#     while a:
#         a1 = a.popleft()
#         if a1 in r:
#             tmp.append(a1)
#     print(tmp)
#     if ''.join(tmp) == r:
#         print("YES")
#     else:
#         print("NO")
        
for i in range(n):
    plan = input()
    dq = deque(r)
    for x in plan:
        if x in dq:
            if x != dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq) == 0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))



