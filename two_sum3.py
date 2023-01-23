class TwoSum:

    def __init__(self):
        self.arr = []

    def add(self, number: int) -> None:
        self.arr.append(number)

    def find(self, value: int) -> bool:
        hashmap = {}
        for i in range(len(self.arr)):
            complement = value - self.arr[i]
            if complement in hashmap:
                return True
            hashmap[self.arr[i]] = i
        return False

            