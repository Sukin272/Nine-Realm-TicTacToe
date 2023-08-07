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
            self.width = self.screen.get_width()
            self.height = self.screen.get_height()
            self.update()
            self.render()
    
    def update(self):
        
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.running = False
            if event.type == self.pygame.MOUSEBUTTONUP:
                logic.mouseClicked(self)
    
    def render(self):
        self.screen.fill((0,0,0))
        logic.makeBoard(self)
        
        x,y=logic.getClick(self.pygame,self.width,self.height)
        self.pygame.draw.circle(self.screen, (255,0,0), (self.width*x/9+self.width/18,self.height*y/9+self.height/18), 10)

        self.pygame.display.update()
    
    