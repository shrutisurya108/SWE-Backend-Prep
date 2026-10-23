class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        # Approach 1: Brute force
        # num_good_pairs=0
        # for i in range(0,len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]==nums[j]:
        #             num_good_pairs+=1
        # return num_good_pairs
        # Time complexity for approach 1: O(n^2)
        # Space complexity for approach 1: O(1)

        # Approach 2, optimizing on brute force to make time complexity O(n)
        count=0
        seen={}
        for i in nums:
            count = count+seen.get(i, 0)
            seen[i]=seen.get(i,0)+1
        return count