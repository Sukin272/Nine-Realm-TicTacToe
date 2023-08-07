def makeGrid(pygame,screen,width, height, x, y, a):
    height=int(height)
    width=int(width)
    x=int(x)
    y=int(y)
    
    pygame.draw.line(screen, (0,0,a*255), (x+int(1/3*width),y+  0), (x+int(1/3*width),y+  height), int(width*0.02))
    pygame.draw.line(screen, (0,0,a*255), (x+int(2/3*width),y+  0), (x+int(2/3*width),y+  height), int(width*0.02))
    pygame.draw.line(screen, (0,0,a*255), (x+0,y+ int(1/3*height)), (x+width, y+ int(1/3*height)), int(height*0.02))
    pygame.draw.line(screen, (0,0,a*255), (x+0,y+  int(2/3*height)), (x+width, y+ int(2/3*height)), int(height*0.02))

def getClick(pygame,w,h):
    x,y = pygame.mouse.get_pos()
    X=int(9*x/w)
    Y=int(9*y/h)
    return X,Y

def makeBoard(self):
        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,0,0,1)
        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,1/3*self.width,0,1)
        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,2/3*self.width,0,1)

        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,1/3*self.width,1/3*self.height,1)
        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,0,1/3*self.height,1)
        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,2/3*self.width,1/3*self.height,1)

        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,0,2/3*self.height,1)
        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,1/3*self.width,2/3*self.height,1)
        makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,2/3*self.width,2/3*self.height,1)

        makeGrid(self.pygame,self.screen,self.width, self.height,0,0,0)

def mouseClicked(self):
    x,y=getClick(self.pygame,self.width,self.height)
    self.clickedRealm=(x//3)+3*(y//3)
    if self.curRealm==-1 or self.curRealm==self.clickedRealm:
        self.Board[x][y]=self.curTurn
        self.curTurn=self.curTurn ^ 1
        x=x%3
        y=y%3
        self.curRealm=3*y+x
        print(self.curRealm)