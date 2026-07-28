class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        left_max = 0 
        right_max = 0 
        total_water_trap = 0 
        while left<right: 
            

            
            if height[left]<=height[right]:
                if left_max<height[left]:
                    left_max = height[left]

                else:
                   
                    total_water_trap+=(left_max - height[left]) ## 2
                left+=1
            else:
                # right-=1
                if right_max<height[right]:
                    right_max = height[right]

                else:
                    
                    total_water_trap+=(right_max - height[right])
                right-=1

        return total_water_trap 
        