class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        target = -math.inf
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Now treat this as a Two Sum II problem (Sorted Array)
            # Target = -nums[i]
            # Use Two Pointers (L and R) here...
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while(l < r):
                if(nums[l] + nums[r] == target): # found a triplet
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1

                    # Move the left pointer until it's not the same element
                    while(nums[l] == nums[l - 1] and l < r):
                        l += 1
                elif(nums[l] + nums[r] > target):
                    r -= 1
                else:
                    l += 1
        return res

            

