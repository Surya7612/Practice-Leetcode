class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    #counter class approach
        # s = Counter(nums).most_common()
        # return s[0][0]

    #sorting approach
        # nums.sort()
        # n = len(nums)
        # return nums[n//2]

    #Boyer Moore's Voting Algo. approach
        count = 0
        maj_el = -1

        for num in nums:
            if count == 0:
                maj_el = num
            if num == maj_el:
                count += 1
            else:
                count -= 1
        
        return maj_el
