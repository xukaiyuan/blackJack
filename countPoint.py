def countPointM(card):
    pointM = 0
    for i, j in card:
        if (j == 'J' or j == 'Q' or j == 'K'):
            pointM = pointM + 10
        elif(j == 'A'):
            if(pointM <= 10):
                pointM = pointM + 11
            else:
                pointM = pointM + 1
        else:
            pointM = pointM + int(j)
    return pointM