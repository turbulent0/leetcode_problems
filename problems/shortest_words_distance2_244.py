words = ["practice", "makes", "perfect", "coding", "makes", 'son', 'coding', 'makes']
    
from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: list[str]):
        self.locations = defaultdict(list)
        
        for i, word in enumerate(wordsDict):
            self.locations[word].append(i)

    
    def shortest(self, word1, word2):
        locs1 = self.locations[word1]
        locs2 = self.locations[word2]
        loc1, loc2 = 0, 0
        dist = abs(locs1[0] - locs2[0])
        while loc1 < len(locs1) and loc2 < len(locs2):
            dist = min(dist, abs(locs1[loc1] - locs2[loc2]))
            if locs1[loc1] < locs2[loc2]:
                loc1 += 1
            elif locs1[loc1] > locs2[loc2]:
                loc2 += 1
            else:
                return 0
        return dist

obj = WordDistance(words)

print(obj.shortest('makes', 'coding'))