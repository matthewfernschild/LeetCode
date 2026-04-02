class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1,2,3,45,65,23,4,23
        # indice + indice = target

        # brute force would be to say okay 0+1, 0+2, etc.
        # what would be more efficient
        
        t = 0
        
        for index, num in enumerate(nums):
            i = index+1
            while i < len(nums):

                if (num + nums[i]) == target: return [index,i]

                i += 1
            
            print("test")