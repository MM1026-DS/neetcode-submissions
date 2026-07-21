class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pointer1 = 0 
        pointer2 = len(numbers)-1

        while pointer1<pointer2:
            sum_val = numbers[pointer1]+numbers[pointer2]
            if sum_val>target:
                pointer2-=1
            elif sum_val<target:
                pointer1+=1
            else:
                return [pointer1+1,pointer2+1]
        return []

        
        