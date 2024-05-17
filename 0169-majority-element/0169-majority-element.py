class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        s = Counter(nums).most_common()

        return s[0][0]