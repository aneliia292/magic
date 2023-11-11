import time
import random


class Card:
    numList = ['Joker', '2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'Valet', 'Dama', 'King', 'Toose']
    mastList = ['Пик', "Крестей", "Червей", "Бубей"]

    def __init__(self, i, j):
        self.mastB = self.mastList[i - 1]
        self.numB = self.numList[j - 1]


class DeckOfCard:
    def __init__(self):
        self.deck = [None] * 56
        k = 0
        for i in range(1, 5):
            for j in range(1, 15):
                self.deck[k] = Card(i, j)
                k += 1

    def shuffle(self):
        random.shuffle(self.deck)

    def get(self, i):
        if 0 <= i <= 55:
            answer = f'{self.deck[i].numB} {self.deck[i].mastB}'

        else:
            answer = f'Такой карты нет'

        return answer


deck = DeckOfCard()
deck.shuffle()
n = int(input('Выерите карту:   '))
if 0 <= n <= 55:
    print(f'Вы взяли {deck.get(n)}')
else:
    print('Такой карты нет')