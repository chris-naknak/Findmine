from re import X
import pygame as pg
import random
import tkinter.messagebox
import sys
import os



pg.init() 

# 우리가 이미지의 경로를 절대경로로 변환해주는 함수
# def resource_path(relative_path: str) -> str:
#     try:
#         base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
#     except:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

def resource_path(relative_path: str) -> str:
    try:
        base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)    

CAPTION="MINETAKER" #창 제목
ICON = pg.image.load(resource_path("realmine.png")) 
SCREEN_WIDTH = 320
SCREEN_HEIGHT = 400
FPS = 60
FONT = pg.font.SysFont("unpilgi",32,True,True)
CONTENT_FONT = pg.font.SysFont("system",25,True,True)
WINDOW = pg.display

#화면 타이틀 설정
WINDOW.set_caption(CAPTION)
WINDOW.set_icon(ICON)

#화면 크기 설정
SCREEN = WINDOW.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#색깔
RED = (255, 0, 0)
BLUE = (0,100,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255,150, 0)
GRAY = (150,150,150)
PINK = (255,51,255)
GREEN = (0,153,0)
PUPPLE = (102,51,153)
BROWN = (153,102,0)
SKYBLUE = (153,204,255)

# 사진
image = pg.image.load(resource_path("realmine.png"))
image_flag = pg.image.load(resource_path("flag.png"))

# TEXT
left_mine_text = FONT.render(" ",True,BLACK)
Failed = FONT.render(" ",True,RED)  

# 지뢰 최대 갯수
max_mine = 40


class Board:
    def __init__(self,number):
        self.Cellmaster = []
        self.Minemaster = []
        for i in range(1,17):
            Cellnumber = 1 + 16*(i-1)
            for j in range(1,17):
                self.Cellmaster.append(Cell(self,j,i,(j-1)*20 + 1, j*20 - 1,(i-1)*20+80 + 1, i*20+80 - 1,Cellnumber))
                #append는 list 끝에 요소 한개를 추가하는 함수
                Cellnumber += Cellnumber
        self.left_mine = number


    def mine_text(self):
        left_mine_text = FONT.render("Mine : {}".format(self.left_mine),True,BLACK)
        SCREEN.blit(left_mine_text,(10,10))

    def render_cell(self):
        for i in self.Cellmaster:
            if i.opened == False:
                pg.draw.rect(SCREEN,BLACK,(i.x_1, i.y_1, 18, 18))
            elif i.opened == True:
                pg.draw.rect(SCREEN,BLACK,(i.x_1, i.y_1, 18, 18),1)

    def render_flag(self):
        for i in self.Cellmaster:
            if i.flaged == True:
                SCREEN.blit(image_flag,[i.x_1,i.y_1]) 

    # content 색깔부여하고, 숫자를 그리는 코드
    def render_content(self):
        for i in self.Cellmaster:
            if i.opened == True:
                if i.content == 0:
                    content_text = CONTENT_FONT.render(None,False,BLUE)
                elif i.content == 1:
                    content_text = CONTENT_FONT.render("{}".format(i.content),False,RED)
                elif i.content == 2:
                    content_text = CONTENT_FONT.render("{}".format(i.content),False,GREEN)
                elif i.content == 3:
                    content_text = CONTENT_FONT.render("{}".format(i.content),False,ORANGE)
                elif i.content == 4:
                    content_text = CONTENT_FONT.render("{}".format(i.content),False,PINK)
                elif i.content == 5:
                    content_text = CONTENT_FONT.render("{}".format(i.content),False,PUPPLE)                
                elif i.content == 6:
                    content_text = CONTENT_FONT.render("{}".format(i.content),False,SKYBLUE)
                elif i.content == 7:
                    content_text = CONTENT_FONT.render("{}".format(i.content),False,BROWN)
                elif i.content == 8:
                    content_text = CONTENT_FONT.render("{}".format(i.content),False,BLACK)
                SCREEN.blit(content_text,(4+i.x_1,2+i.y_1))


    def render_gameover(self):
        if gameover == True:
            print("fail")    
            Failed = FONT.render("OPPPPPPPPPPPPS!!!!",True,RED)
            SCREEN.blit(Failed,(40,60))

            for i in self.Minemaster:
                SCREEN.blit(image,[self.Cellmaster[i-1].x_1, self.Cellmaster[i-1].y_1])

            # self.warn()
            msg_box = tkinter.messagebox.askretrycancel("패배","LOLOLOLOLOL \n Do you try again?")
            if msg_box == True:
                restart()
            print("fuck")

    def warn(self):
        msg_box = tkinter.messagebox.askretrycancel("패배","LOLOLOLOLOL \n Do you try again?")
        if msg_box == True:
            restart()

        # else:
        #     pg.display.quit()
        #     RUNNING = False




    # 지뢰 랜덤생성
    def mine_generate(self):
        self.Minemaster = []
        while True:
            minecell = random.randrange(1,257)
            if minecell not in self.Minemaster:
                self.Cellmaster[minecell-1].set_mine()  # hasmine = True 랑 같은말 
                self.Minemaster.append(minecell)
    
            if len(self.Minemaster) == 40:
                break
    
    # open 되있으면서 content = 0 이면, 주변 8개를 open 시켜라
    def open_with(self):
        for c in self.Cellmaster:
            if c.opened == True and c.content == 0:
                x = c.x
                y = c.y
                X = [x-1, x, x+1]
                Y = [y-1, y, y+1]

                if x-1 == 0:
                    X.remove(x-1)
                if x+1 == 17:
                    X.remove(x+1)
                if y-1 == 0:
                    Y.remove(y-1)
                if y+1 == 17:
                    Y.remove(y+1)
                for i in Y:
                    for j in X:
                        self.Cellmaster[j + (i-1)*16 -1].open()




    # 주먹구구식 content 부여하는 코드
    def has_content(self):
        for c in self.Cellmaster:
            x = c.x
            y = c.y
            X = [x-1, x, x+1]
            Y = [y-1, y, y+1]

            if c.hasmine == True:
                c.content = None
                pass
            else:
                c.content = 0
                if x-1 == 0:
                    X.remove(x-1)
                if x+1 == 17:
                    X.remove(x+1)
                if y-1 == 0:
                    Y.remove(y-1)
                if y+1 == 17:
                    Y.remove(y+1)
                for i in Y:
                    for j in X:
                        if self.Cellmaster[j + (i-1)*16 - 1].hasmine == True:
                            c.content = c.content + 1


class Cell:

    def __init__(self,board1,x,y,x_1,x_2,y_1,y_2,num):
        self.boss = board1
        self.x = x #cell의 x좌표
        self.y = y #cell의 y좌표
        self.x_1 = x_1 #없어도 됨
        self.x_2 = x_2
        self.y_1 = y_1
        self.y_2 = y_2
        self.Cellnumber = num
        self.hasmine = False
        self.opened = False
        self.flaged = False
        self.content = None


    def set_mine(self):
        self.hasmine = True

    def open(self):
        self.opened = True 

    def unopen(self):
        self.opened = False

    def flag(self):
        self.boss.left_mine = self.boss.left_mine - 1 
        self.flaged = True

    def unflag(self):
        self.boss.left_mine = self.boss.left_mine + 1 
        self.flaged = False


# 재시작 함수
def restart():
    global gameover, board1

    gameover = False
    board1 = Board(max_mine)
    for i in board1.Cellmaster:
        i.opened = False
        i.flaged = False
        i.content = None
        i.hasmine = False
    board1.mine_generate()
    print(board1.Minemaster)

# 마우스 커서
def mouse_position():
    return pg.mouse.get_pos()

# 마우스 커서가 있는 cell의 좌표
def what_cell():
    mp_x, mp_y = mouse_position()
    if mp_x % 20 == 0:
        return None
    elif mp_y % 20 == 0:
        return None
    elif mp_y <= 80 :
        return None
    else:    
        a = mp_x // 20 + 1
        b = (mp_y - 80) // 20 + 1
        return a + (b-1)*16  #Cellnumber  구하는 방법


gameover = False
board1 = Board(max_mine)
board1.mine_generate()
print(board1.Minemaster)


RUNNING = True
while RUNNING:

    pg.time.Clock().tick(FPS)

    # for event in pg.event.get():
    #     if event.type == pg.QUIT:
    #         pg.display.quit()
    #         RUNNING = False

    #대충 틀
    SCREEN.fill(GRAY)
    SCREEN.blit(Failed,(40,60))
    board1.mine_text()
    board1.render_cell()
    board1.render_flag()
    board1.render_gameover()
    board1.has_content()
    board1.render_content()
    board1.open_with()

    pg.display.update() # 화면을 갱신 시켜줌

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.display.quit()
            RUNNING = False

        # 좌클릭
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1 :
            current_button_num = what_cell()
            # 찍은 곳이 이상하면 pass
            if current_button_num == None:
                pass
            
            else:
                current_button = board1.Cellmaster[current_button_num-1]
                if current_button.opened == False and current_button.flaged == False:
                    if current_button.hasmine == False:
                        current_button.open()
                    elif current_button.flaged == False and current_button.hasmine == True:
                        gameover = True


        # 우클릭
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 3 :
            current_button_num = what_cell()
            # 찍은 곳이 이상하면 pass
            if current_button_num == None:
                pass

            else:
                current_button = board1.Cellmaster[current_button_num-1]
                if current_button.opened == False and current_button.flaged == False:
                    current_button.flag()
                    # current_.open()
                elif current_button.flaged == True:
                    current_button.unflag()
                    # current_button.unopen()











    

    

