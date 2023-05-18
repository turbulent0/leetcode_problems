
if __name__== '__main__':
    # class Solution:
    #     def twoSum(self, nums: list[int], target: int) -> list[int]:
    #         for i_ind, i in enumerate(nums):
    #             for j_ind, j in enumerate(nums[i_ind+1:]):
    #                 if (i + j) == target:
    #                     return [i_ind, j_ind+i_ind+1]
    #2.5 s
    class Solution:
        def twoSum2(self, nums: List[int], target: int) -> List[int]:
            for i_ind, i in enumerate(nums):
                remaining = target - i
                if remaining in nums:
                    return [i_ind, nums.index(remaining)]
    
    # 70 ms
    class Solution:
        def twoSum(self, nums: list[int], target: int) -> list[int]:
            hashmap = {}
            for i in range(len(nums)):
                complement = target - nums[i]
                if complement in hashmap:
                    return [i, hashmap[complement]]
                hashmap[nums[i]] = i

    print(Solution().twoSum([2,7,9], 9))