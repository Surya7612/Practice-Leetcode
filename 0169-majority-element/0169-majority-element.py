class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = -1
        for i in range(len(nums)):
            if nums[i] == res:
                count += 1
            elif count == 0:
                res = nums[i]
                count = 1
            else:
                count -= 1
        return res