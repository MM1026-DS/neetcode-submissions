class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals,key = lambda x:x[0])
        pointer1 =0 
        n = len(sorted_intervals)

        while pointer1<n-1:
            # print(sorted_intervals)
            next_pointer = pointer1+1 
            interval1 = sorted_intervals[pointer1]
            interval2 = sorted_intervals[next_pointer]

            ## ==================
            if interval1[1]>=interval2[0]:
                new_inerval = [interval1[0],max(interval1[1],interval2[1])]
                
                sorted_intervals.pop(pointer1)
            
                sorted_intervals.pop(pointer1)
                
                sorted_intervals.insert(pointer1, new_inerval )
                n-=1
            else:
                pointer1+=1
        
        return sorted_intervals 
        