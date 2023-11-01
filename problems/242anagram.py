from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) == len(t):
        #     freq_t = defaultdict(int)
        #     freq_s  = defaultdict(int)
        #     for letter in s:
        #         freq_s[letter] += 1
        #     for letter in t:
        #         freq_t[letter] += 1
        #     for k in freq_s.keys():
        #         if freq_s[k] != freq_t[k]:
        #             return False
        #     return True
        # else:
        #     return False
        return Counter(t) == Counter(s)