#question number 20

def solve(s):
    stack = []
    for i in range(len(s)):
        item =  s[i]
        if item == '(' or item == '{' or item == '[':
            stack.append(item)
            continue
        elif item == ')':
            head = stack.pop()
        elif item == '}':
            head = stack.pop()
        elif item == ']':
            head = stack.pop()

                
    if len(stack) ==0:return True
    else: return False


s = "([])"
s = "()[]{"
s = "(]"
x = solve(s)
print(x)
        
        
