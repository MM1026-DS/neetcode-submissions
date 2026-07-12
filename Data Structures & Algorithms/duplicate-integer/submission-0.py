class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        previous_len = len(nums)
        deduplicate_nums = list(set(nums))
        current_len = len(deduplicate_nums)
        if current_len<previous_len:
            return True 
        return False
        