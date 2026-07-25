
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t)>len(s):
            return ""
        
        required_frequency = {}
        for chr in t:
            required_frequency[chr] = required_frequency.get(chr,0)+1 
        
        left = 0 
        window_frequency = {}
        formed = 0 
        required = len(required_frequency)
        min_length = float("inf")
        min_start = 0 
        for right in range(len(s)):
            right_chr = s[right]
            if right_chr in required_frequency:
                window_frequency[right_chr] = window_frequency.get(right_chr,0)+1 
            
                if window_frequency[right_chr]==required_frequency[right_chr]:
                    formed+=1 

            while formed == required: 
                current_length = right-left+1 
                if current_length<min_length:
                    min_length = current_length 
                    min_start = left 
                left_chr = s[left]
                if left_chr in required_frequency: 
                    if (window_frequency[left_chr]==required_frequency[left_chr]):
                        formed-=1 
                    window_frequency[left_chr]-=1
                left+=1
        if min_length == float('inf'):
            return ''
        return s[min_start:min_start+min_length]
    
        