class CardDeck:
    def __init__(self):
        self.length = 52
        self.index = 0
        self.__SUITS = ['Пик', 'Бубей', 'Червей', 'Крестей']
        self.__RANKS = [*range(2, 11), 'J', 'Q', 'K', 'A']


    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        else:
            suit = self.__SUITS[self.index // len(self.__RANKS)]
            rank = self.__RANKS[self.index % len(self.__RANKS)]
            self.index += 1
            return f'{rank} {suit}'

    def __iter__(self):
        return self


deck = CardDeck()
while True:
    print(next(deck))