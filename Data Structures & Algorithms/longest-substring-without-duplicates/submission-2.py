class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## I can create set  I will loop from the index 0 
        ##  there is a pointer at index +1 which will move untill repeating char will come 
        ## and compare that length with maxLength if len > maxLen so it will replace it 

        ## e.g. 
        ## xyzyzx 
        ## X   yzyzx     yzyzx     yzyzx   -- max len 3 and time complexity is O(n**2) O(1)
        ## |   |          |          |   
        if len(s)==0:
            return 0
        if len(set(s))==1:
            return 1
        maxLen = float('-inf')
        for startindex in range(len(s)):
            nextpointer = startindex+1 
            length = 1 
            visited = set() 
            visited.add(s[startindex])
            while nextpointer<=len(s)-1 and s[nextpointer] not in visited: 
                visited.add(s[nextpointer])
                length+=1
                nextpointer+=1
            maxLen = max(maxLen,length)
        return maxLen 

        