import random
from random import randrange, choice # generate and place new tile

cardType = ("黑桃", "草花", "方块", "红心");
cardNum = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K");
def generator():
    card = []
    numCard = []
    for i in cardType:
        for j in cardNum:
            card.append((i, j))
    random.shuffle(card)
    random.shuffle(card)
    return card