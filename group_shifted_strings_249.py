from collections import defaultdict
class Solution:
    def groupStrings(self, strings: list[str]) -> list[list[str]]:
        gr_diffs = defaultdict(list)
        for word in strings:
            chars = list(map(ord, word))
            diffs = '_'.join([str((ch2 - ch1)%26) for ch1, ch2 in zip(chars, chars[1:])])
            gr_diffs[diffs].append(word)
        return list(gr_diffs.values())