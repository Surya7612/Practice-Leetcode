class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using two-pointer iteration approach
        sorted_nums = sorted(enumerate(nums), key= lambda x:x[1])
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = sorted_nums[left][1] + sorted_nums[right][1]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return [sorted_nums[left][0], sorted_nums[right][0]]
        return []