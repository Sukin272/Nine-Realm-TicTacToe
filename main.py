import pygame
import time

rows = 9
cols = 9
Board = [[-1 for _ in range(cols)] for _ in range(rows)]

curTurn=0
curRealm=-1

def makeGrid(width, height, x, y, a):
    height=int(height)
    width=int(width)
    x=int(x)
    y=int(y)
    

    #Big grid
    pygame.draw.line(screen, (0,0,a*255), (x+int(1/3*width),y+  0), (x+int(1/3*width),y+  height), int(width*0.02))
    pygame.draw.line(screen, (0,0,a*255), (x+int(2/3*width),y+  0), (x+int(2/3*width),y+  height), int(width*0.02))
    pygame.draw.line(screen, (0,0,a*255), (x+0,y+ int(1/3*height)), (x+width, y+ int(1/3*height)), int(height*0.02))
    pygame.draw.line(screen, (0,0,a*255), (x+0,y+  int(2/3*height)), (x+width, y+ int(2/3*height)), int(height*0.02))

    # if a==0:
    #     # Border
    #     pygame.draw.line(screen, (100,0,0), (x+0, y+0), (x+width,y+ 0), int(height*0.03))
    #     pygame.draw.line(screen, (100,0,0), (x+0, y+height), (x+width, y+height), int(height*0.03))
    #     pygame.draw.line(screen, (100,0,0), (x+0, y+0), (x+0, y+height), int(width*0.03))
    #     pygame.draw.line(screen, (100,0,0), (x+width,y+ 0), (x+width, y+height), int(width*0.03))


def getClick(w,h):
    x,y = pygame.mouse.get_pos()
    X=int(9*x/w)
    Y=int(9*y/h)
    return X,Y



pygame.init()

screen = pygame.display.set_mode((1000, 1000),pygame.RESIZABLE)
pygame.display.set_caption("9 Realm TIc Tac Toe")

running = True
while running:
    width = screen.get_width()
    height = screen.get_height()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            x,y=getClick(width,height)
            clickedRealm=(x//3)+3*(y//3)
            if curRealm==-1 or curRealm==clickedRealm:
                Board[x][y]=curTurn
                curTurn=curTurn ^ 1
                x=x%3
                y=y%3
                curRealm=3*y+x
                print(curRealm)
            


    
    screen.fill((0,0,0))


    makeGrid(1/3*width, 1/3*height,0,0,1)
    makeGrid(1/3*width, 1/3*height,1/3*width,0,1)
    makeGrid(1/3*width, 1/3*height,2/3*width,0,1)

    makeGrid(1/3*width, 1/3*height,0,1/3*height,1)
    makeGrid(1/3*width, 1/3*height,1/3*width,1/3*height,1)
    makeGrid(1/3*width, 1/3*height,2/3*width,1/3*height,1)

    makeGrid(1/3*width, 1/3*height,0,2/3*height,1)
    makeGrid(1/3*width, 1/3*height,1/3*width,2/3*height,1)
    makeGrid(1/3*width, 1/3*height,2/3*width,2/3*height,1)

    makeGrid(width, height,0,0,0)
    
    x,y=getClick(width,height)
    pygame.draw.circle(screen, (255,0,0), (width*x/9+width/18,height*y/9+height/18), 10)



    pygame.display.update()