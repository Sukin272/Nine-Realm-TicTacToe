import pygame,logic

class Game:
        
    def __init__(self):
        self.pygame=pygame
        self.pygame.init()
        rows = 9
        cols = 9
        self.Board = [[-1 for _ in range(cols)] for _ in range(rows)]

        self.curTurn=0
        self.curRealm=-1
        self.screen = pygame.display.set_mode((1000, 1000),pygame.RESIZABLE)
        self.pygame.display.set_caption("9 Realm TIc Tac Toe")
        self.running = True

    def run(self):
        while self.running:
            self.update()
            self.render()
    
    def update(self):
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.running = False
            if event.type == self.pygame.MOUSEBUTTONUP:
                x,y=logic.getClick(self.pygame,self.width,self.height)
                self.clickedRealm=(x//3)+3*(y//3)
                if self.curRealm==-1 or self.curRealm==self.clickedRealm:
                    self.Board[x][y]=self.curTurn
                    self.curTurn=self.curTurn ^ 1
                    x=x%3
                    y=y%3
                    self.curRealm=3*y+x
                    print(self.curRealm)
    
    def render(self):
        self.screen.fill((0,0,0))


        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,0,0,1)
        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,1/3*self.width,0,1)
        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,2/3*self.width,0,1)

        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,1/3*self.width,1/3*self.height,1)
        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,0,1/3*self.height,1)
        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,2/3*self.width,1/3*self.height,1)

        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,0,2/3*self.height,1)
        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,1/3*self.width,2/3*self.height,1)
        logic.makeGrid(self.pygame,self.screen,1/3*self.width, 1/3*self.height,2/3*self.width,2/3*self.height,1)

        logic.makeGrid(self.pygame,self.screen,self.width, self.height,0,0,0)
        
        x,y=logic.getClick(self.pygame,self.width,self.height)
        self.pygame.draw.circle(self.screen, (255,0,0), (self.width*x/9+self.width/18,self.height*y/9+self.height/18), 10)

        self.pygame.display.update()