a = input()
stack = []
for i in a:
    if i.isdecimal():
        stack.append(int(i))
    else:
        if i == '+':
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a2 + a1)
        elif i == '-':
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a2 - a1)
        elif i == '*':
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a2 * a1)
        elif i == '/':
            a1 = stack.pop()
            a2 = stack.pop()
            stack.append(a2 / a1)
print(stack[0])
        