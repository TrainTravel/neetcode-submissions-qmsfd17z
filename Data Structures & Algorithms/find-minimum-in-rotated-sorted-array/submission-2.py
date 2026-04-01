class Solution:
    def findMin(self, nums: List[int]) -> int:
        left_ptr, right_ptr = 0, len(nums) - 1

        def helper(l: int, r: int) -> int:
            subarr_size = r - l + 1
            if(subarr_size) == 1:
                return nums[l]
            if(subarr_size) == 2:
                if(nums[l] < nums[r]):
                    return nums[l]
                return nums[r]

            mid = (l + r) // 2
            if(nums[mid] > nums[r]):
                return helper(mid, r)
            return helper(l, mid)
        return helper(left_ptr, right_ptr)