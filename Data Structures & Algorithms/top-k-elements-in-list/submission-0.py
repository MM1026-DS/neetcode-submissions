import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_counter = {}
        output = [] 

        for val in nums:
            dict_counter[val] = dict_counter.get(val,0)+1 

       
        counterheapq =[]
        for key,value in dict_counter.items():
            heapq.heappush(counterheapq,(-value,key))

        for _ in range(k):
            # print(heapq.heappop(counterheapq))
            output.append(heapq.heappop(counterheapq)[1])

        return output


        
        

        