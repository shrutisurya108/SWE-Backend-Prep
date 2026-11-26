class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        sums = 0
        for i in range(left, right+1):
            sums += self.nums[i]
        return sums


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# Time complexity for worst case scenario = O(n) (need to sum the whole array)
# Space complexity = O(1), only 1 extra variable used