class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_product  = 1 
        right_product = 1 
        left_product_arr = [] 
        right_product_arr = [] 
        product_arr = [] 

        for num in nums:
            left_product_arr.append(left_product)
            left_product*=num 

        for num in reversed(nums):
            right_product_arr.append(right_product)
            right_product*=num 
        
        for l,r in zip(left_product_arr,right_product_arr[::-1]):
            product = l*r 
            product_arr.append(product)
        
        return product_arr 