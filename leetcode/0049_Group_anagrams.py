# from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Approach 1: Group all anagrams using a canonica key (sorted(word))
        # out = defaultdict(list)
        # out={}
        # result = []
        # for word in strs:
        #     canonical_key = "".join(sorted(word))
        #     out.setdefault(canonical_key, []).append(word)
        #     # out[canonical_key].append(word)
        # return list(out.values())
        # Time complexity for approach 1: 
        # sorting for n words = O(n log k) (assuming n words, each of avg length k)
        # In the same loop, dict operations also happen
        # total time complexity = O(n log k)
        # Space compexity = O(n) (worst case, if every word needs a separate key-value pair in the dict)

        # Approach 2, using a 26-alphabet tuple for every word as key
        # result = {}
        # alpha_dict = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11,
        # 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23,
        # 'y':24, 'z':25}

        # for word in strs:
        #     word_list = [0]*26
        #     for ch in word:
        #         word_list[alpha_dict[ch]] += 1
        #     result.setdefault(tuple(word_list), []).append(word)
        #     # result[tuple(word_list)].append(word)
        
        # return list(result.values())

        # Time complexity for approach 2:
        # there are n words, each word of avg length k
        # the loop runs for n*k times, so time complexity = O(nk)
        # Space complexity= n tuples of 26 values = 26n, and a dict of n words/keys at max
        # Space complecity = O(27n) in worst case = O(n)

        # Approach 3, using the same logic as approach, only the way of building the tuple of 26 length for each word changes
        result = {}

        for word in strs:
            word_list = [0]*26
            for ch in word:
                idx_to_be_changed = ord(ch)-ord('a')
                word_list[idx_to_be_changed] += 1
            result.setdefault(tuple(word_list), []).append(word)
            # result[tuple(word_list)].append(word)
        
        return list(result.values())

        # Time complexity for approach 3:
        # there are n words, each word of avg length k
        # the loop runs for n*k times, so time complexity = O(nk)
        # Space complexity= n tuples of 26 values = 26n, and a dict of n words/keys at max
        # Space complecity = O(27n) in worst case = O(n)



        
