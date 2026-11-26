class NumArray:

# Approach 2: In this design, every range sum query takes O(1) time
# Time complexity during initialization = O(n), as prefix sum array is also calculated
# Space complexity = O(n), to store the prefix sum array of length n
    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prefix_sums = []
        for i in range(len(nums)):
            if i==0:
                self.prefix_sums.append(nums[i])
                continue
            self.prefix_sums.append(self.prefix_sums[i-1] + nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return (self.prefix_sums[right] - self.prefix_sums[left] + self.nums[left])



# Approach 1: In this design, every range sum query will take O(n) time
    # def __init__(self, nums: list[int]):
    #     self.nums = nums

    # def sumRange(self, left: int, right: int) -> int:
    #     sums = 0
    #     for i in range(left, right+1):
    #         sums += self.nums[i]
    #     return sums


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Time complexity for worst case scenario = O(n) (need to sum the whole array)
# Space complexity = O(1), only 1 extra variable used