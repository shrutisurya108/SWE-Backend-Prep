class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:

        # Approach 3: Tried latest
        # Time complexity
        # n runs first to make prefix array
        # n runs again to make the final array
        # total = n+n = 2n = O(n) time complexity
        # Space complexity = O(1)
        # The leetcode question explicitly mentioned that the result array will not be counted as extra space complexity, hence not including the result array as extra space

        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        result = [0 for _ in range(len(nums))]

        prod = 1
        for i, num in enumerate(nums):
            if i==0:
                result[i]=1
            else:
                prod *= nums[i-1]
                result[i] = prod
        prod=1
        for i in range(len(nums)-1, -1, -1):
            if i==len(nums)-1:
                continue
            else:
                prod *= nums[i+1]
                result[i] *= prod
        return result

        # Approach 1:
        # Time complexity = O(n), one loop n times for creating suffix and prefix product arrays,
        # then one loop n times to calculate product of suffix and prefix products of an element
        # total = O(2n) = O(n)
        # Space complexity = O(n), 2 extra arrays to store prefix and suffix products

        # prefix = [0 for _ in range(len(nums))]
        # suffix = [0 for _ in range(len(nums))]
        # preprod = 1
        # suffprod=1
        # for i in range(len(nums)):
        #     j=len(nums)-1-i
        #     if i==0:
        #         prefix[i]=1
        #         suffix[j]=1
        #     else:
        #         preprod *= nums[i-1]
        #         prefix[i]=preprod
        #         suffprod *= nums[j+1]
        #         suffix[j] = suffprod
        #     j-=1
        # return [suffix[i]*prefix[i] for i in range(len(nums))] # creates a new array

        # Approach 2: Brute force, Cannot be accepted since we need an answer in O(n)
        # Time complexity = O(n^2)
        # Space complexity = O(n)
        # prod_list = []
        # for i in range(len(nums)):
        #     prod = 1
        #     for j in range(len(nums)):
        #         if j!=i:
        #             prod*= nums[j]
        #     prod_list.append(prod)
        # return prod_list