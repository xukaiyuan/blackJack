import random
from random import randrange, choice # generate and place new tile

cardType = ("草花", "黑桃", "红桃", "方块");
cardNum = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K");
def generator():
    card = []
    numCard = []
    for x in range(0,4):
        for i in cardType:
            for j in cardNum:
                card.append((i, j))
    random.shuffle(card)
    random.shuffle(card)
    
    return card