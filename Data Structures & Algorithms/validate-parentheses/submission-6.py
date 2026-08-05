from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        mapping_para = {'(':')','{':'}','[':']'}
        stack = []
        stack2 = deque([])

        if len(s)==1:
            return False

        arr_paraenthesis = ["(","{","["]

        for chr in s:
            if chr in arr_paraenthesis:
                stack.append(chr)
            else:
                if len(stack)>0:

                    ls_chr = stack.pop() 
                    if mapping_para[ls_chr]!=chr:
                        return False 

                else:
                    stack2.append(chr)
                    
        return True if len(stack)==0 and len(stack2)==0 else False
