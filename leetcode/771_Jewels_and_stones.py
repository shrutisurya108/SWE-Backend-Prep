class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # Approach 1: Brute Force
        # count=0
        # for jewel in jewels:
        #     for stone in stones:
        #         if jewel == stone:
        #             count+=1
        # return count
        # Time complexity for approach 1: O(n*m), n=len(stones), m=len(jewels)
        # Space complexity for approch 1: O(1)

        # Approach 2: Brute Force with in keyword
        # count=0
        # for stone in stones:
        #     if stone in jewels:
        #         count+=1
        # return count
        # Time complexity for approach 2: O(n.m), n=len(stones), m=len(jewels)
        # Space complexity for approach 2: O(1)

        # Approach 3: Optimizing on brute force solutions
        jwl = set(jewels)
        count = sum(stone in jwl for stone in stones)
        return count

