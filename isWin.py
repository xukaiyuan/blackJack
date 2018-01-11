def isWin2(pointP, pointM):
    #pointP = countPoint(cardPlayer)
    #pointM = countPointM(cardMaker)
    #print(pointM)
    if(pointM > 21):
        print("you win1")
        return True
    elif(pointM == 21):
        print("you lose")
        return False
    else:
        if(pointP >= pointM):
            print("you win2")
            return True
        else:
            print("you lose1")
            return False
