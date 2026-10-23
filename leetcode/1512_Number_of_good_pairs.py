class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        
        # Approach 1: Brute force
        num_good_pairs=0
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j]:
                    num_good_pairs+=1
        return num_good_pairs
        # Time complexity for approach 1: O(n^2)
        # Space complexity for approach 1: O(1)

        # Approach 2: Optimizing on brute force
        count_dict={}
        num_good_pairs=0
        for i in nums:
            if i in count_dict:
                count_dict[i]+=1
            else:
                count_dict[i]=1
        for items in count_dict:
            if count_dict[items]>1:
                num_good_pairs+=(count_dict[items]-1)
        return num_good_pairs
        # Time complexity for approach 2: O(n)
        # Space complexity for approach 2: O(n) (worst case if no matching pairs exist)
