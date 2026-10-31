class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        num_set = set(nums)
        n = len(num_set)
        longest = 0
        seq=1
        for i in num_set:
            if i-1 not in num_set:
                seq=1
                j=i
                while(seq<=n):
                    if j+1 in num_set:
                        seq+=1
                        j+=1
                    else:
                        longest = max(longest, seq)
                        break
        return longest

# Time complexity:
# O(n) to make a set from the list
# The outer for-loop execution is n times, so another O(n)
# The inner while loop executes a total of n-times (for all while loops that will be called)
# The inner while loop touches each number at most once in the program, so O(n) for inner while loop
# Total time complexity = O(n)
# Space complexity = O(n) to store the set created from the list