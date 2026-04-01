class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if(r - l > k): # window size is invalid(too big), remove leftmost
                window.remove(nums[l])
                l += 1
            
            if(nums[r] in window):
                return True
            else:
                window.add(nums[r])
                r += 1

        return False