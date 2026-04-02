class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:        
        # we are given a list of integers, then we have to make a list in order of frequency
        # THEN, we print out the top k most frequent
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        # now i have number: frequency and I need to sort it
        freq_list = []

        while k > 0:
            max_key = max(num_dict, key=num_dict.get)
            highest = num_dict.pop(max_key)
            freq_list.append(max_key)
            k -= 1

        return freq_list