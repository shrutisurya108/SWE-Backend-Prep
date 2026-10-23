class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        # Approach 1: Using list comprehension
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans
        # Time complexity: O(n)
        # Space complexity: O(n)

        # Tried to solve it with space complexity O(1), but could not do so