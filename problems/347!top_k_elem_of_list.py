class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #build dict of frequencies
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            print(times)
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]