import pygame as pg

pg.init() #초기화?

CAPTION="minetaker" #창 제목
ICON = pg.image.load("realmine.png")

WIDTH = 640
HEIGHT = 360
FPS = 60

WINDOW = pg.display #창을 가리키는 객체
WINDOW.set_caption(CAPTION) #set_caption 이나 icon, mode 는 내장된거임
WINDOW.set_icon(ICON)
SCREEN = WINDOW.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0,100,255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255,150, 0)

RUNNING = True

while RUNNING: #반복문이 필요함 없으면 나중에 바로 꺼질수도 있음.
    pg.time.Clock().tick(FPS)

    #Your code here
    SCREEN.fill(RED)
    #pg.draw.rect(SCREEN, BLUE, [180,140,300,100]) #왼쪽 변으로부터 얼마나 떨어졌나, 오른쪽 변으로 부터 얼마떨어졌나, 넓이?

    pg.draw.circle(SCREEN, WHITE, (200, 240),100, 100) #몸통

    pg.draw.ellipse(SCREEN, BLUE,[85,110,230,100], 32) #머플러
    pg.draw.ellipse(SCREEN, BLACK,[85,110,230,100], 2) #머플러 테두리

    pg.draw.ellipse(SCREEN, BLUE,[85,80,230,100], 32) #머플러
    pg.draw.ellipse(SCREEN, BLACK,[85,80,230,100], 2) #머플러 테두리


    pg.draw.circle(SCREEN, WHITE, (200, 80),60, 60) #얼굴

    pg.draw.line(SCREEN, ORANGE, (190,100), (200,115),5) #코 왼쪽
    pg.draw.line(SCREEN, ORANGE, (210,100), (200,115),5) #코 오른쪽

    pg.draw.circle(SCREEN, BLACK, (180, 80), 10, 10) #눈 왼쪽
    pg.draw.circle(SCREEN, BLACK, (220, 80), 10, 10) #눈 오른쪽

    #양쪽 팔
    pg.draw.line(SCREEN, BLACK, (110,210), (70,210),5)
    pg.draw.line(SCREEN, BLACK, (290,210), (340,210),5)
    pg.draw.circle(SCREEN, WHITE, (70, 210),20, 20)
    pg.draw.circle(SCREEN, WHITE, (340, 210),20, 20)


    pg.display.update() # 화면을 갱신 시켜줌

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
            RUNNING = False
