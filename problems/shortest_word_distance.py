class Solution:
    def shortestDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        diff = float('inf')
        pos1, pos2 = None, None
        for i, word in enumerate(wordsDict):
            if word == word1:
                pos1 = i
            if word == word2:
                pos2 = i
            if (pos1 is not None) and (pos2 is not None):
                diff = min(diff, abs(pos2 - pos1))
                if diff == 1:
                    return diff
        return diff