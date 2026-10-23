class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        
        # Approach 1: Creating a new array that stores the array
        # runsum=[]
        # curr_sum=0
        # for i in nums:
        #     curr_sum+=i
        #     runsum.append(curr_sum)
        #     # curr_sum=runsum[-1]
        # return runsum
        # Time complexity for approach 1: O(n)
        # Space complexity for approach 1: O(n)
        
        # Approach 2: Modifying the array in place
        for i in range(len(nums)):
            if i>0:
                nums[i]+=nums[i-1]
        return nums
        # Time complexity for approach 2: O(n)
        # Space complexity for approach 2: O(1)