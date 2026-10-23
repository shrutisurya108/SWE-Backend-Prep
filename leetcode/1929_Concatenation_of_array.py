class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        # # Approach 1
        # ans = [0]*len(nums)*2
        # for i in range(len(nums)):
        #     ans[i]=nums[i]
        #     ans[i+n]=nums[i]
        # return ans
        # Time complexity for approach 1: O(n)
        # Space complexity for approach 1: O(2n) = O(n)

        # Approach 2, trying a one-liner
        # ans = [nums[i] for i in range(len(nums))] * 2
        # return ans
        # Time complexity for approach 2: O(n)
        # Space complexity for approach 2: O(2n) = O(n)

        # Approach 3
        ans = nums*2
        return ans
        # Time complexity for approach 2: O(n)
        # Space complexity for approach 2: O(2n) = O(n)
        