from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:

    # Approach 1: Count+sort
        # count_dict = Counter(nums)
        # # sorted_dict = sorted(count_dict.items(), key=lambda kv: kv[1], reverse=True)
        # sorted_list = sorted(count_dict, key=lambda k: -count_dict[k])
        # return [i for i in sorted_list[:k]]
    # Time complexity = O(n) to count the frequency of every elemnt in the list + O(n log n) to sort the list by key-values = O(n log n)
    # Space complexity = O(n) at most to store the count of all elements in the list,
    # + O(n) to store at most n items in a sorted list = O(2n) = O(n)

    # Approach 2: Bucket sort approach
        count_dict = Counter(nums)
        n=len(nums)
        buckets = [[] for _ in range(n+1)]
        for key,value in count_dict.items():
            buckets[value].append(key)
        count=0
        result = []
        for i in range(n, 0, -1):
            if len(buckets[i])>0:
                for j in buckets[i]:
                    if count<k:
                        result.append(j)
                        count+=1   
            if count==k:
                break
        return result
        # Time complexity for approach 2: making the count_dict is O(n) + creating n buckets is O(n)
        # + filling the buckets with values is O(n) at most as it depends on the length of the dictionary
        # + walking backwards through the buckets is O(n*u), n=no. of buckets, u=no. of unique elements
        # While collecting k values from the bucket, outer loop runs n times for n buckets, but inner loop runs for u times where u=no. of unique elements
                



        