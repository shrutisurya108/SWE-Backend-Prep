class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        
        # Approach 1
        # richest = 0
        # for customer in accounts:
        #     if sum(customer)>richest:
        #         richest=sum(customer)
        # return richest
        # Time complexity for approach 1 = O(n^2)
        # Space complexity for approach 1 = O(1)


        # Approach 2
        # richest = 0
        # for customer in accounts:
        #     customer_tot = 0
        #     for money in customer:
        #         customer_tot+=money
        #     if customer_tot>richest:
        #         richest=customer_tot
        # return richest
        # Time complexity for approach 2 = O(n^2)
        # Space complexity for approach 2 = O(1)
        
        # Approach 3
        return max(sum(customer) for customer in accounts)