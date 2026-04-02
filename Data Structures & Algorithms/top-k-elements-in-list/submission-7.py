class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        # we are given a list of integers, then we have to make a list in order of frequency
        # THEN, we print out the top k most frequent
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n,0)

        freq = [[] for _ in range(len(nums) + 1)]

        for n, c in count.items():
            freq[c].append(n)

        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
