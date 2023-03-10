T = input()
ans = ''
stack = [] # 연산자 관리용

for t in T :
    if t.isalpha() :
        ans += t
    else :
        if t == '(' :
            stack.append(t)
        elif t == '*' or t == '/' :
            while stack and (stack[-1] == '*' or stack[-1] == '/') :
                ans += stack.pop()
            stack.append(t)
        elif t == '+' or t == '-' :
            while stack and stack[-1] != '(' :
                ans += stack.pop()
            stack.append(t)
        elif t == ')' :
            while stack and stack[-1] != '(' :
                ans += stack.pop()
            stack.pop() # '('를 빼는 작업

while stack :
    ans += stack.pop()

print(ans)