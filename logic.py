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
    if self.BoardState[self.curRealm]!=-1:
        self.curRealm=-1
    if self.curRealm==-1 or self.curRealm==self.clickedRealm:
        if self.curRealm==-1 or self.BoardState[self.curRealm] == -1:
            self.Board[x][y]=self.curTurn
            self.curTurn=self.curTurn ^ 1
            x=x%3
            y=y%3
            self.curRealm=3*y+x
    for i in range(9):
        self.BoardState[i]=gridFilled(self, i)

def renderMoves(pygame):
    for i in range(pygame.rows):
        for j in range (pygame.cols):
            Xcoord=int((1/9)*i*pygame.width+1/180*pygame.width)
            Ycoord=int(1/9*j*pygame.height+1/180*pygame.height)
            if pygame.Board[i][j]==1:
                pygame.screen.blit(pygame.X_image, (Xcoord, Ycoord))
            if pygame.Board[i][j]==0:
                pygame.screen.blit(pygame.O_image, (Xcoord, Ycoord))

def gridFilled(pygame, boardNumber):
    grid=[[-1 for _ in range(3)] for _ in range (3)]
    for i in range (9):
        for j in range(9):
            if i//3+3*(j//3) == boardNumber:
                grid[i%3][j%3]=pygame.Board[i][j]
    for i in range (3):
        if grid[i][0]==grid[i][1] and grid[i][2]==grid[i][1]:
            return grid[i][0]
    for i in range (3):
        if grid[0][i]==grid[1][i] and grid[2][i]==grid[1][i]:
            return grid[0][i]
    if grid[0][0]==grid[1][1] and grid[2][2]==grid[1][1]:
        return grid[0][0]
    if grid[2][0]==grid[1][1] and grid[0][2]==grid[1][1]:
        return grid[1][1]
    return -1



              