def showHandP(cardPlayer):
    print('你的手牌：')
    print
    for i in range(0, len(cardPlayer)):
        print(cardPlayer[i])
    print
    
def showHandM(cardMaker):
    print('庄家手牌：')
    print
    for i in range(0, len(cardMaker)):
        print(cardMaker[i])
    print