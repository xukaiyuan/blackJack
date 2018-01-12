
# coding: utf-8


# In[20]:


import random
import curses
from random import randrange, choice # generate and place new tile
from collections import defaultdict

from generator import generator
from countPoint import countPointM
from isWin import isWin2
from isGameOver import isGameOver
from ifContinue import ifContinue
from showHand import showHandM 
from showHand import showHandP


card = []

numCardM = []
numCardP = []
i = 0
x = 'z'

chip = 100
flag = 0




def dispatch(card, i):
    
    return card[i]

def countPoint(card):
    global x
    points = 0
    for i, j in card:
        if (j == 'J' or j == 'Q' or j == 'K'):
            points = points + 10
        elif (j == 'A'):
            if(points <= 10):
                while (x != 'y' and x != 'n'):
                    x = input("want 11?(y/n):")
                if(x == 'y'):
                    points = points + 11
                else:
                    points = points + 1
            else:
                points = points + 1
        else:
            points = points + int(j)
    return points

def showPoint(cardPlayer):
    print('当前点数：')
    point = countPoint(cardPlayer)
    print(point)

def showPointM(cardMaker):
    print('庄家点数：')
    point = countPointM(cardMaker)
    print(point)

def isWin1(pointP):
    #pointP = countPoint(cardPlayer)
    global flag
    if(pointP > 21):
        print("you lose")
        return False
    elif(pointP == 21):
        flag = 1
        print("you win")
        return True
    else:
        return True


def judge(pointP, pointM, cardMaker):
    global chip
    showHandM(cardMaker)
    showPointM(cardMaker)
    if(isWin2(pointP, pointM)):
        chip = chip + 1
    else:
        chip = chip - 2

    
def start():
    #
    #不应该每次洗牌
    global card
    global i
    global screen
    if(i == 51 or i == 0):
        card = generator()
    cardMaker = []
    cardPlayer = []

    cardPlayer.append(dispatch(card, i))
    cardPlayer.append(dispatch(card, i + 1))
    cardMaker.append(dispatch(card, i + 2))
    cardMaker.append(dispatch(card, i + 3))
    i = i + 4

    global chip
    global flag
    global x
    

    showHandP(cardPlayer)
    showPoint(cardPlayer)

    pointP = countPoint(cardPlayer)
    pointM = countPointM(cardMaker)

    
    print('庄家第一张手牌：')
    print
    print(cardMaker[0])
    
    while(ifContinue()):
        cardPlayer.append(dispatch(card, i))
        showHandP(cardPlayer)
        showPoint(cardPlayer)
        i = i + 1
        pointP = countPoint(cardPlayer)
        if(countPoint(cardPlayer) > 21):
            break

    if(isWin1(pointP)):
        #print('player')
        #print(pointP)
        if(flag == 1):
            chip = chip + 1
            print('强啊')
        else:   
             while(countPointM(cardMaker) <= 17):
                cardMaker.append(dispatch(card, i))
                i = i + 1
                pointM = countPointM(cardMaker)
                if(countPointM(cardMaker) > 21):
                    break
             
             #print('Maker')
             #print(pointM)
             judge(pointP, pointM, cardMaker)
    else:
        chip = chip - 2

    flag = 0
    x = 'z'
    #tmpA = 1
        #showHandM(cardMaker)
      
        


letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']  
actions = ['yes', 'no', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))

def show_text(surface_handle, pos, text, color, font_bold = False, font_size = 13, font_italic = False):   
    ''''' 
    Function:文字处理函数 
    Input：surface_handle：surface句柄 
           pos：文字显示位置 
           color:文字颜色 
           font_bold:是否加粗 
           font_size:字体大小 
           font_italic:是否斜体 
    Output: NONE 
    author: socrates 
    blog:http://blog.csdn.net/dyx1024 
    date:2012-04-15 
    '''         
    #获取系统字体，并设置文字大小  
    cur_font = pygame.font.SysFont("宋体", font_size)  
      
    #设置是否加粗属性  
    cur_font.set_bold(font_bold)  
      
    #设置是否斜体属性  
    cur_font.set_italic(font_italic)  
      
    #设置文字内容  
    text_fmt = cur_font.render(text, 1, color)  
      
    #绘制文字  
    surface_handle.blit(text_fmt, pos)   



if __name__=="__main__":

    def init():
        #重置牌组
        card = generator() 
        return 'Game'

    def not_game(state):
        #画出 GameOver 或者 Win 的界面
        #读取用户输入得到action，判断是重启游戏还是结束游戏
        #action = get_user_action(stdscr)
        responses = defaultdict(lambda: state) #默认是当前状态，没有行为就会一直在当前界面循环
        responses['Restart'], responses['Exit'] = 'Init', 'Exit' #对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        #开始游戏
        #读取用户输入得到action

        start()
        #action = get_user_action(stdscr)
        print("现在筹码数量：")
        print(chip)
        action = input("continue or quit or refresh?(c/q/r)")


        if action == 'c':
            return 'Game'
        if action == 'r':
            return 'Init'
        if action == 'q':
            return 'Exit'
        #if 成功移动了一步:
            if (isWin1(pointP, flag) and isWin2(pointP, pointM)):
                return 'Win'
            if isGameOver():
                return 'Gameover'
        return 'Game'


    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
        }

    state = 'Init'


#pygame

        
#pygame

    
    #状态机开始循环
    while state != 'Exit':
        
        
    #background = pygame.image.load(background_image_filename).convert()
        state = state_actions[state]()


        
    




#for i in range(50):
#   dispatch(card, i)

