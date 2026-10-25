from collections import Counter
# Both approach tried and tested on leetcode, all cases passed.
class Solution:
    def getCharCountDict(self,str):
        char_count_dict = {}
        for ch in str:
            char_count_dict[ch] = char_count_dict.get(ch, 0)+1
        return char_count_dict

    def isAnagram(self, s: str, t: str) -> bool:
        # Before diving into making character counts dict, we can check and reject if the 2 strings are of unequal length
        # Time complexity of len() is O(1)
        if len(s) != len(t): return False 
        # Approach 1, using a dict to keep a count of all chars in the string
        # Time complexity = O(n+m), n=length of s, m=length of t
        # Space complexity = O(n+m), n=length of s, m=length of t (worst case, if all chars in both strings are distinct)
        return self.getCharCountDict(s) == self.getCharCountDict(t)

        # Approach 2, using Counter class
        # Time complexity = O(n+m), n=length of s, m=length of t
        # Space complexity = O(n+m), n=length of s, m=length of t (worst case, if all chars in both strings are distinct)
        # return True if Counter(s) == Counter(t) else False

        # Approach 2 is similar in logic to Approach 1, the only difference is the 
        # Counter class which has an efficient function to get the dict of char counts
        # and I wrote a similar function by myself getCharCountDict()
        # Since approach 2 uses an inbuilt Python class which has the most efficient function,
        #I think it would exit earlier.
