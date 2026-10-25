# Both approaches tried and tested on leetcode, both passed
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Approach 1: Brute Force
        # Time complexity = O(n^2) (The i-loop runs for n times and j-loop runs n-1 times)
        # Space complexity = O(n) (worst case, if all elements are included in the final result list)

        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             result.append(i)
        #             result.append(j)
        # return result
        
        # Approach 2: Trying to optimize on brute force
        # Time complexity = O(n)
        # Space complexity = O(n) (worst case, if all elements have to be added in seen)
        seen = {}
        for i, num in enumerate(nums):
            needed = target-num
            if needed in seen:
                return [seen[needed], i]
            seen[num]=i
