class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = [ i for i in vec if i != []]

    def next(self) -> int:
        if len(self.vec[0]) > 1:
            return self.vec[0].pop(0)
        else:
            return self.vec.pop(0)[0]

    def hasNext(self) -> bool:
        return len(self.vec) > 0 