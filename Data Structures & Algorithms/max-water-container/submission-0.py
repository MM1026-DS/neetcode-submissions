class Solution:
    def maxArea(self, heights: List[int]) -> int:
        pointer1 = 0 
        pointer2 = len(heights)-1 
        maxArea = 0 

        while pointer1<=pointer2: 

            if heights[pointer1]<=heights[pointer2]:
                area = heights[pointer1]*(pointer2 - pointer1)
                maxArea = max(maxArea,area)
                pointer1+=1 
            else:
                area = heights[pointer2]*(pointer2 - pointer1)
                maxArea = max(maxArea,area)
                pointer2-=1 

        return maxArea 

        