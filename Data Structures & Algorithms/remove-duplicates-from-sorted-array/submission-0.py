class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        num_list = []

        for num in nums[:]:
            if num in num_list:
                nums.remove(num)
            if num not in num_list:
                num_list.append(num)
        
        return len(num_list)
