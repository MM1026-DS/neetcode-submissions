
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ## nums = [9,1,4,2,3,3,7]
        # for 9 either I will select 1 or reject 1  both test  ## [1,2,3,4]
        # if select 1 is it greater than 9 return 0 

        dp = {}

        def dfs(index,prev_index):

            if index == len(nums):
                return 0 

            if (index, prev_index) in dp:
                return dp[(index, prev_index)]

            skip = dfs(index+1,prev_index)
            
            take = 0 
            if prev_index==-1 or nums[index]>nums[prev_index]:
                take   =  1+dfs(index+1,index)

            dp[(index,prev_index)] = max(take,skip)

            return dp[(index,prev_index)] 

        dfs(0,-1)
        return max(dp.values())



                

        