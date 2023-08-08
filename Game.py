import pygame,logic

class Game:
        
    def __init__(self):
        self.pygame=pygame
        self.pygame.init()
        self.rows = 9
        self.cols = 9
        self.Board = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        self.width=self.height=1000
        self.clock = pygame.time.Clock()
        self.BoardState=[-1 for _ in range (9)]

        self.curTurn=1
        self.curRealm=-1
        self.screen = pygame.display.set_mode((1000, 1000),pygame.RESIZABLE)
        self.pygame.display.set_caption("9 Realm TIc Tac Toe")
        self.running = True

    def run(self):
        while self.running:
            self.width = self.screen.get_width()
            self.height = self.screen.get_height()
            self.X_image=pygame.image.load("pictures/X.xcf")
            self.X_image=pygame.transform.scale(self.X_image, (1/10*self.width, 1/10*self.height))
            self.O_image=pygame.image.load("pictures/O.xcf")
            self.O_image=pygame.transform.scale(self.O_image, (1/10*self.width, 1/10*self.height))
            self.update()
            self.render()
    
    def update(self):
        
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.running = False
            if event.type == self.pygame.MOUSEBUTTONUP:
                logic.mouseClicked(self)
                # print(logic.gridFilled(self,1))
        self.clock.tick(60)

    
    def render(self):
        self.screen.fill((0,0,0))

        logic.makeBoard(self)

        x,y=logic.getClick(self.pygame,self.width,self.height)
        self.pygame.draw.circle(self.screen, (255,0,0), (self.width*x/9+self.width/18,self.height*y/9+self.height/18), 10)

        logic.renderMoves(self)

        logic.highlight(self) 

        logic.renderBigWins(self)

        logic.makeGrid(self.pygame,self.screen,self.width, self.height,0,0,0)

        oimg=pygame.image.load("pictures/O.xcf")
        oimg=pygame.transform.scale(oimg, (self.width,self.height))
        ximg=pygame.image.load("pictures/X.xcf")
        ximg=pygame.transform.scale(ximg, (self.width,self.height))
        tie=pygame.image.load("pictures/Tie.jpg")
        tie=pygame.transform.scale(tie, (self.width,self.height))
        end = logic.gameEnd(self)
        if end==1:
            self.screen.blit(ximg, (0, 0))
        if end==0:
            self.screen.blit(oimg, (0, 0))
        if end==2:
            self.screen.blit(tie, (0, 0))            
            
        self.pygame.display.update()
    
    