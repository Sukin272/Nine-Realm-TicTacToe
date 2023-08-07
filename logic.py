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