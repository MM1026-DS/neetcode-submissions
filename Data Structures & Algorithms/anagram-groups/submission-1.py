from collections import defaultdict, Counter 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        groupanagram_list = [] 
        for str_val in strs:
            key = tuple(sorted(Counter(str_val).items()))
            group_dict[key].append(str_val)

        for value in group_dict.values():
            groupanagram_list.append(value)
        
        return groupanagram_list

        
            

        