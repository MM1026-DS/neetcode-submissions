class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ## last 2 tokens whenever any  operators comes takes the last two number in stack do the openration and append to 
        ## the stack  
        ## edge 1: suppose there is no number in the stack is it possible ?? 
        ##  what will happen in that case 
        
        stack = []
        mapping_dict ={
            "+":self.add,
            "-":self.sub,
            '*':self.mul,
            '/':self.div
        }
        operator = ['+','-','*','/']

        for token in tokens:
            if token not in operator:
                stack.append(token)
            else:
                if len(stack)>=2:

                    b = int(stack.pop())
                    a = int(stack.pop())
                    value = mapping_dict[token](a,b)
                    stack.append(value)

        return int(stack.pop())


    
    def add(self,a,b):
        return a+b 
    def sub(self,a,b):
        return a - b 
    def mul(self,a,b):
        return a *b 
    def div(self,a,b):
        return a/b 
        
        