class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        freq = {}
        maxLen = 0 
        maxfrequency = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1
            maxfrequency = max(maxfrequency,freq[s[right]])
            windowlength = right - left +1 


            replacementneeded = windowlength - maxfrequency 
            
            if replacementneeded>k:
                freq[s[left]]-=1
                left+=1 
            else:
                maxLen = max(maxLen,windowlength)
        return maxLen 
        