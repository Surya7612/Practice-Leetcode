#Brute Force algorithm 

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        #here, the time complexity is O(n^2) and space complexity is O(1)


# Optimized way is: use the two pointer approach
''' we start by considering two pointers, one at the left most point and one at the right most point. On each iteration, we will move one of the pointers. This is done by comparing the elements where the current pointers are at and seeing if they sum up to the target. But this only works when the array is sorted. After initializing the left and right most points. The main part of the algorithm starts, where it is iterating through the array with these two points. In each iteration, the sum of the elements pointed by the two points are summed and compared to the target. If the sum equals the target, the indices(or values) of these elements are the required output. If the sum is less than the target, the left pointer is moved one step closer to the right(to increase the sum). If the sum is greater than the target, the right pointer is moved one step closer to the left(to decrease the sum). The process is repeated until the two pointers meet or the target sum is found. 
Time Complexity:
Sorting: The initial sorting of the array has a time complexity of O(n log n), where n is the number of elements in the array.
Two-Pointer Iteration: After sorting, the algorithm iterates through the array once with the two pointers. This iteration is O(n), as each element is looked at most once.
Combining these steps, the overall time complexity of the two-pointer approach to the Two Sum problem is O(n log n) due to the sorting step.
Space Complexity:
Sorting: The space complexity for sorting can vary based on the algorithm used. For example, if an in-place sorting algorithm like Heapsort is used, the space complexity can be O(1). However, for algorithms like Mergesort, it could be O(n).
Pointers: The two pointers themselves use constant space, O(1).
In scenarios where in-place sorting is used, the space complexity is O(1). Otherwise, it could be O(n) due to the space required for sorting.'''
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         sorted_nums = sorted(enumerate(nums), key = lambda x: x[1])
#         '''sorted_nums = sorted(enumerate(nums), key = lambda x: x[1]) enumerate(nums)  pairs each number in nums with its index. sorted(..., key = lambda x: x[1]) sorts these pairs based on the numbers, not the indices.'''
#         left, right = 0, len(nums) - 1
#         while left < right:
#             current_sum = sorted_nums[left][1] + sorted_nums[right][1]
#             if current_sum < target:
#                 left += 1
#             elif current_sum > target:
#                 right -=1
#             else:
#                 return [sorted_nums[left][0], sorted_nums[right][0]]
#         return []

#Another Optimal way: Two pass Hash Table:

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums_Map = {}
#         n = len(nums)

#         #Hash Table
#         for i in range(n):
#             nums_Map[nums[i]] = i

#         #Find the complement:
#         for i in range(n):
#             complement = target - nums[i]
#             if complement in nums_Map and nums_Map[complement] != i:
#                 return [i, nums_Map[complement]]

#         return [] 
#Time complexity: O(n)

#Now, One Pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target:int) -> List[int]:
        nums_Map = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in nums_Map:
                return [nums_Map[complement], i]
            nums_Map[nums[i]] = i

        return []