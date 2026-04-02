class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_set = set(nums)
        if len(test_set) != len(nums):
            return True
        else:
            return False