class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            num_set = set(nums)
            ans_dict = {}
            for num in num_set:
                if num - 1 not in num_set:
                    ans_dict[num] = [num]
                    current_num = num
                    while current_num + 1 in num_set:
                        current_num += 1
                        ans_dict[num].append(current_num)
                        
            return max((len(lst) for lst in ans_dict.values()), default=0)
   
            
