class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        
        # Approach 4: using maths formula
        # Time complexity = O(n), space complexity = O(1)
        n=len(nums)
        expect_nums_sum = n * (n+1) // 2
        actual_nums_sum = 0
        for i in nums:
            actual_nums_sum += i
        return expect_nums_sum - actual_nums_sum
        
        # Approach 3: using sort(), time complexity = O(n log n), space complexity = O(1)
        # nums.sort()
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return nums[i] - 1
        # return len(nums)
        
        # Approach 2: Using set, Time complexity = O(n), space complexity = O(n)
        # n=len(nums)
        # num_set = set(nums)
        # for i in range(n+1):
        #     if i not in num_set:
        #         return i

        # Approach 1: Brute Force, time complexity = O(n^2), Space complexity = O(1)
        # n = len(nums)
        # for i in range(n+1):
        #     if i not in nums:
        #         return i