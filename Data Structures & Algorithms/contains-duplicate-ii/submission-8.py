class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0: return False
        window = set()

        L = 0
        for R in range(len(nums)):
            # 1. Maintain: If window size exceeds k, slide the left boundary
            # We do this BEFORE checking nums[R]
            # print(f"current window: {window}")
            if(R - L) > k:
                window.remove(nums[L])
                L += 1

            # 2. Check: Is the current number a duplicate within distance k?
            if nums[R] in window:
                return True
            
            window.add(nums[R])
        return False


            
            