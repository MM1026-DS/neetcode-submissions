from collections import deque 
class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        self.previousmin = []
        

    def push(self, val: int) -> None:
        if val<=self.min:
            self.previousmin.append(self.min)
            self.min = val
            
        self.stack.append(val)
        

    def pop(self) -> None:
        ele = self.stack.pop()
        if ele == self.min:
            # self.previousmin.pop() 
            if len(self.previousmin)>0:
                self.min = self.previousmin.pop() 
            else:
                self.min = float('inf')


        
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min
        
