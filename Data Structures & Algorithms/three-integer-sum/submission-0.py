class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = [] 
        nums.sort()

        for index in range(len(nums)-1):
            first_num = nums[index]
            pointer1 = index+1 
            pointer2 = len(nums)-1

            while pointer1<pointer2:
                # print(first_num, nums[pointer1] ,nums[pointer2])
                sum_val = first_num + nums[pointer1] + nums[pointer2]
                # print(sum_val)
                if sum_val>0:
                    pointer2-=1
                elif sum_val<0:
                    pointer1+=1 
                else:
                    threesum_arr = [first_num,nums[pointer1],nums[pointer2]]
                    pointer1+=1
                    pointer2-=1
                    
                    threesum_arr.sort() 
                    if threesum_arr not in output:
                    
                        output.append(threesum_arr)

        return output 


        


        