class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0 

        n = len(nums)
        parent = list(range(n))
        size =[1]*n
        value_to_index ={}
        def find(x):
            if parent[x]!=x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x,y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return 
            parent[root_y] = root_x 
            size[root_x]+=size[root_y]
        

        for index,value in enumerate(nums):
            if value in value_to_index:
                continue 
            value_to_index[value] = index 

            if value-1 in value_to_index:
                union(index,value_to_index[value-1])

            if value+1 in value_to_index:
                union(index,value_to_index[value+1])

        return max(size)
