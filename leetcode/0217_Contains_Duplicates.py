# Tried both the approach 1 by 1 on leetcode, all testcases pass for both the approach
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # Approach 1, using seen-before technique.
        # Time complexity = time to traverse the list once = O(n)
        # Space complexity = O(n) (worst case, all items distinct)
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False

        # Approach 2:
        # Time complexity = time to convert list to set = O(n)
        # Space complexity = O(n) (worst case, all items distinct)
        # nums_set = set(nums)
        # return False if len(nums_set) == len(nums) else True

        # Approach 2 will exit earlier