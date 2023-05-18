class Solution:
    # # my solution
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     substring = dict()
    #     length = 0
    #     res = ''
    #     i = 0
    #     while i <= len(s)-1: 
    #         l = s[i]      
    #         if l in substring:
    #             temp = ''.join(substring.keys())
    #             if len(temp) > length:
    #                 res = temp
    #                 length = len(temp)
    #             i = substring[l]
    #             substring = dict()
    #             if len(s) - i - 1 < length:
    #                 return max(length, len(''.join(substring)))
    #         else:
    #             substring[s[i]] = i
    #         i += 1
        
    #     return max(length, len(''.join(substring)))
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        start = 0
        l_pos = {}
        for j in range(n):
            l = s[j]
            if l in l_pos:
                start = max(l_pos[l], start)
            l_pos[l] = j+1
            ans = max(ans, j - start + 1)

        return ans
    # 

s = Solution()
print(s.lengthOfLongestSubstring("abba"))