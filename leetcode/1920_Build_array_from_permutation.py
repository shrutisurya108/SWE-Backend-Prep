class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        # Approach 1: Using list comprehension
        ans = [nums[nums[i]] for i in range(len(nums))]
        return ans
        # Time complexity: O(n)
        # Space complexity: O(n)

        # Tried to solve it with space complexity O(1), did with help of Claude hint
        n = len(nums)
        for i in range(n):
            nums[i] += n * (nums[nums[i]] % n)   # % n reads the ORIGINAL value even if it was already updated
            for i in range(n):
                nums[i] //= n                        # keep only the new value
        return nums
    # Time O(n) | Space O(1) extra