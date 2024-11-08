a = input()
b = input()

# from collections import Counter

# a = Counter(a)
# b = Counter(b)

# if a == b:
#     print("YES")
# else:
#     print("NO")

dic = {}
for i in a:
    dic[i] = dic.get(i, 0) + 1

for i in b:
    dic[i] = dic.get(i, 0) - 1 

for v in dic.values():
    if v > 0:
        print("NO")
        break
else:
    print("YES")


