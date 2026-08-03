from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        left = 0 
        for right in range(len(s1),len(s2)+1):
            if Counter(s2[left:right])==Counter(s1):
                return True 
            else:
                left+=1
        return False