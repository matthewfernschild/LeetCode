class Solution:
    # take a list then CREATE nested lists. OHHHH
    # can there be repeat strings?
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = {}
        for i in strs:
            sorted_i = "".join(sorted(i))
            if sorted_i not in str_dict:
                str_dict[sorted_i] = []
                str_dict[sorted_i].append(i) # initialize the new dict entry & add the value
            elif sorted_i in str_dict:
                str_dict[sorted_i].append(i) # add value to existing dict entry
        return list(str_dict.values())
        
            
