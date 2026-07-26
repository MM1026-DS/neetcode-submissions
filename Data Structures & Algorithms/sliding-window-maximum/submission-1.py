from collections import deque
from typing import List 
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque() 
        result = []
        
        for index in range(len(nums)):

            while dq and dq[0]<=index-k:
                dq.popleft() 
            
            while dq and nums[dq[-1]]<=nums[index]:
                dq.pop() 

            
            dq.append(index)
            
            
            
            if index>=k-1:
                result.append(nums[dq[0]])

            
          
                
            
            
           
        
        return result 

        