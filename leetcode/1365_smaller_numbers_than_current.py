class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:

        #Approach 1: Brute force approach
        # ans = [0]*len(nums)
        # count=0
        # for i in range(0, len(nums)):
        #     count=0
        #     for j in range(0, len(nums)):
        #         if i==j:
        #             continue
        #         if nums[j]<nums[i]:
        #             count+=1
        #     ans[i]=count
        # return ans
        # Time complexity for approach 1: O(n^2)
        # Space complexity for approach 2: O(n)

        #Approach 2: Optimizing on the Brute force approach
        # ans = [0]*len(nums)
        # sorted_nums = sorted(nums, reverse=True)
        # sorted_dict={}
        # for i in range(0, len(sorted_nums)):
        #     if sorted_nums[i] not in sorted_dict:
        #         sorted_dict[sorted_nums[i]]=len(sorted_nums)-i-1
        #     else:
        #         sorted_dict[sorted_nums[i]]-=1
        # for i in range(len(nums)):
        #     ans[i]=sorted_dict[nums[i]]
        # return ans
        # Time complexity for approach 2: O(n log n)
        # Space coplexity for approach 2: O(n) in worst case if every number in the list is unique

        # Approach 3: Another optimized approach
        sorted_nums = sorted(nums)
        first_index = {}
        for i, num in enumerate(sorted_nums):
            if num not in first_index:
                first_index[num]=i
        return [first_index[num] for num in nums]
        # Time complexity for approach 3: O(n)
        # Space complexity for approach 3: O(n)
