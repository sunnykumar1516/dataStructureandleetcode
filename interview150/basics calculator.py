# question number 224

def solve(s):
    stack = []
    number = 0
    result = 0
    sign = 1
    for item in s:
        if item in ['+','-']:
            if item =='+':
                result = result+ (sign*number)
                number = 0
                sign = 1
            if item == '-':
                result = result + (sign * number)
                number = 0
                sign = -1
        elif item in ['(',')']:
            if item == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                number = 0
                sign = 1
            if item ==')':
                result = result+ number*sign
                sign = stack.pop()
                number = stack.pop()
                result = number + result*sign
                number = 0
                sign = 1
        elif item.isdigit():
            number=number*10 + int(item)
                
    return result
            

s = "20+20-(100+30+30)"
s = "(1+(4+5+2)-3)+(6+8)"

x=  solve(s)
print(x)