def ifContinue():
    x = input("hit or not(y/n):")
    while (x != "y" and x != "n"):
        x = input("hit or not(y/n):")
    if(x == 'y'):
        return True
    else:
        return False