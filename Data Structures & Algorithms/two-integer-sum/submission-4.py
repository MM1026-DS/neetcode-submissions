class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for pointer1 in range(len(nums)-1):
            for pointer2 in range(pointer1+1,len(nums)):
                if nums[pointer1]+nums[pointer2]== target:
                    return [pointer1,pointer2]


      
        