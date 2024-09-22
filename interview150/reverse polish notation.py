def validate(tokens):
    stack = []
    for item in tokens:
        if item in ['+', '-', '*','/']:
            res = 0
            n1 = stack.pop()
            n2 = stack.pop()
            if item == '+':
                res = n1+n2
            elif item == '-':
                res = n1-n2
            elif item == '*':
                res = n1*n2
            elif item == '/':
                res = n2/n1
                
            stack.append(int(res))
        else:
            stack.append(int(item))
            
            
    print(stack)


class Solution(object):
    
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for item in tokens:
            if item in ['+', '-', '*', '/']:
                res = 0
                n1 = stack.pop()
                n2 = stack.pop()
                if item == '+':
                    res = n1 + n2
                elif item == '-':
                    res = n2 - n1
                elif item == '*':
                    res = n1 * n2
                elif item == '/':
                    res = int(n2 / n1)
                
                stack.append(int(res))
                print(stack)
            else:
                stack.append(int(item))
        
        print("--", stack)
        return stack[0]
#tokens = ["2","1","+","3","*"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#tokens = ["4","13","5","/","+"]

s = Solution()
s.evalRPN(tokens)