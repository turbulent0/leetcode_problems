class Solution:
    # bad solution, depends on range that can be up to 10**9
    def findMissingRanges(self, nums: list[int], lower: int, upper: int) -> list[str]:
        res = []
        # left = 0
        # right = 0
        # start_range = False
        # for i in range(lower, upper + 2):
        #     if i in nums and not start_range:
        #         start_range = False
        #     if i not in nums and not start_range:
        #         left = i
        #         right = i
        #         start_range = True
        #     elif i not in nums and start_range and i != upper + 1:
        #         right += 1
        #     elif i in nums and start_range:
        #         start_range = False
        #         if left != right:
        #             res.append(f"{left}->{right}")
        #         else:
        #             res.append(f"{left}")
        #     elif i == upper + 1 and i not in nums and start_range:
        #         if left != right:
        #             res.append(f"{left}->{right}")
        #         else:
        #             res.append(f"{left}")
        # return res

        ## optimal but bounds not effective
        # res = []
        # def formatRange(upper, lower):
        #     if lower != upper:
        #         return f"{lower}->{upper}"
        #     return f"{lower}"

        # if not nums:
        #     if lower != upper:
        #         res.append(f"{lower}->{upper}")
        #     else:
        #         res.append(f"{lower}") 
        #     return res            
        # if lower not in nums:
        #     nums.insert(0, lower-1)
        # if upper != lower:
        #     nums.append(upper+1)
        # for i in range(len(nums)-1):
        #     l = nums[i]
        #     if nums[i+1] != nums[i]+1 and i != len(nums) - 1:
        #         left = nums[i] + 1
        #         right = nums[i+1] - 1
        #         if left != right:
        #             res.append(f"{left}->{right}")
        #         else:
        #             res.append(f"{left}")               
        # return res

        def formatRange(lower, upper):
            if lower != upper:
                return f"{lower}->{upper}"
            return f"{lower}"
        prev = lower - 1
        for i in range(len(nums) + 1):
            curr = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= curr - 1:
                res.append(formatRange(prev + 1, curr - 1))  
            prev = curr
        return res       

s = Solution()
print(s.findMissingRanges(nums = [2, 7], lower = 1, upper = 99))