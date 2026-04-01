from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)
        
        # Count everything - O(n)
        for n in nums:
            freq_dict[n] += 1

        # bucket sort
        # bucket[2] = the list of numbers that occurred twice 
        # create buckets using for comprehension
        buckets = [[] for i in range(len(nums) + 1)]

        # fill the buckets
        for num, count in freq_dict.items():
            buckets[count].append(num)

        # collect the elements until k is the length of the result
        result = []
        for i in range(len(buckets) - 1, 0 , -1):
            # collect
            for n in buckets[i]:
                result.append(n)
                if len(result) == k: 
                    return result