class Solution:
    def findMin(self, nums: List[int]) -> int:

        def helper(subarr: List[int]) -> int:
            print(subarr)
            if len(subarr) == 1:
                return subarr[0]
            if len(subarr) == 2:
                print(subarr)
                if(subarr[0] < subarr[1]):
                    return subarr[0]
                return subarr[1]
            nums_size = len(subarr)
            mid = -1

            mid = len(subarr) // 2
            if(subarr[mid] > subarr[-1]):
                return helper(subarr[mid:])
            return helper(subarr[:mid+1])
        return helper(nums)