import pygame
from random import randint, randrange
import random as r
#Задаём начальне значения переменным
HEIGHT = 1920
WIDTH = 1000
SIZE = 100
reset=0
stop=0
gribi=0
flamethrower = 0
space=0
boshka="Normal"
idk=0
#sc=open("maxscore.txt","r+")
maxscore=0
pygame.init()
pygame.display.set_caption("Snakman")
pygame.display.set_icon(pygame.image.load("icon.png"))

#import images
RED = (200, 191, 231)
surface = pygame.display.set_mode([HEIGHT, WIDTH])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Impact', 40, bold=False)
font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_pause = pygame.font.SysFont('impact', 100, bold=False)
img = pygame.image.load('wall.jpg').convert()
img = pygame.transform.scale(img,(HEIGHT, WIDTH))
fon_menu = pygame.image.load('fonmenu2.png').convert()
fon_menu = pygame.transform.scale(fon_menu,(HEIGHT, WIDTH))
heador = pygame.image.load('head2.png').convert()
heador.set_colorkey(RED)
bodyor = pygame.image.load('body2.png').convert()
bodyor.set_colorkey(RED)
tailor = pygame.image.load('tail2.png').convert()
tailor.set_colorkey(RED)
yablokor = pygame.image.load('apple2.png').convert()
yablokor.set_colorkey(RED)
gribor = pygame.image.load('mushroom.png').convert()
gribor.set_colorkey(RED)
agribor = pygame.image.load('agrib3.png').convert()
agribor.set_colorkey(RED)
fireor = pygame.image.load('fire.png').convert()
fireor.set_colorkey(RED)
head_openor = pygame.image.load('head_open.png').convert()
head_openor.set_colorkey(RED)
gribor1 = pygame.image.load('mushroom1.png').convert()
gribor1.set_colorkey(RED)
gribor2 = pygame.image.load('mushroom2.png').convert()
gribor2.set_colorkey(RED)
asteror = pygame.image.load('meteor.png').convert()
asteror.set_colorkey(RED)
imgmenu = pygame.image.load('veva.png').convert()
imgmenu = pygame.transform.scale(imgmenu,(HEIGHT, WIDTH))
spaceheador = pygame.image.load('head.png').convert()
spaceheador.set_colorkey(RED)
spacebodyor = pygame.image.load('body.png').convert()
spacebodyor.set_colorkey(RED)
spacetailor = pygame.image.load('tail.png').convert()
spacetailor.set_colorkey(RED)
spaceyablokor = pygame.image.load('apple.png').convert()
spaceyablokor.set_colorkey(RED)
spacefon = pygame.image.load('veva.png').convert()
spacefon = pygame.transform.scale(spacefon,(HEIGHT, WIDTH))


astery = 0
asterx = 0
X1 = r.randint(0, WIDTH)
X2 = r.randint(0, WIDTH)

#exit
def close_game():
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           exit()



# objects spawn
x, y = randrange(SIZE, HEIGHT - SIZE, SIZE), randrange(SIZE, WIDTH - SIZE, SIZE)
apple = randrange(SIZE, HEIGHT - SIZE, SIZE), randrange(SIZE, WIDTH - SIZE, SIZE)
if x == apple and y == apple:
    apple = randrange(SIZE, HEIGHT - SIZE, SIZE), randrange(SIZE, WIDTH - SIZE, SIZE)
# значения переменным для новой игры
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 60
dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
score = 0
speed_count, snake_speed = 0, 10
status="menu"
mush=[0]
amush=[0]
grewup=0
agrewup=0
astery = 0
asterx = 0
X1 = r.randint(0, WIDTH)
X2 = r.randint(0, WIDTH)
metfall=500
metfall2=0
spacevav=0
#main game cycle
while True:
    #menu
    if status =="menu":
        surface.blit(fon_menu,(0,0))
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            status="game"
        if key[pygame.K_BACKSPACE]:
            exit()
        pygame.display.flip()
        close_game()

    #pause
    if status =="pause":
        Pause = font_pause.render(f'Paused', 1, pygame.Color('black'))
        if space == 1:
            Pause = font_pause.render(f'Paused', 1, pygame.Color('red'))
        surface.blit(Pause, (820, 97))
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            status="game"
        if key[pygame.K_BACKSPACE]:
            exit()
        pygame.display.flip()
        close_game()

    #game
    if status =="game":
        #drawing textures
        grib = pygame.transform.scale(gribor,(SIZE,SIZE))
        agrib = pygame.transform.scale(agribor,(SIZE,SIZE))
        grib1 = pygame.transform.scale(gribor1,(SIZE,SIZE))
        grib2 = pygame.transform.scale(gribor2,(SIZE,SIZE))
        head = pygame.transform.scale(heador,(SIZE,SIZE))
        body = pygame.transform.scale(bodyor,(SIZE,SIZE))
        tail = pygame.transform.scale(tailor,(SIZE,SIZE))
        fire = pygame.transform.scale(fireor,(SIZE,SIZE))
        head_open = pygame.transform.scale(head_openor,(SIZE,SIZE))
        aster = pygame.transform.scale(asteror,(SIZE,SIZE))
        spacehead = pygame.transform.scale(spaceheador,(SIZE,SIZE))
        spacebody = pygame.transform.scale(spacebodyor,(SIZE,SIZE))
        spacetail = pygame.transform.scale(spacetailor,(SIZE,SIZE))
        spaceapple = pygame.transform.scale(spaceyablokor,(SIZE,SIZE))

        if dx == 0 and dy == -1:#w
            tail = pygame.transform.rotate(tail, 90)
        if dx == 0 and dy == 1:#s
            tail = pygame.transform.rotate(tail, 270)
        if dx == -1 and dy == 0:#a
            tail =  pygame.transform.flip(tail, True, False)
        
        if dx == 0 and dy == -1:#w
             spacetail = pygame.transform.rotate( spacetail, 90)
        if dx == 0 and dy == 1:#s
             spacetail = pygame.transform.rotate( spacetail, 270)
        if dx == -1 and dy == 0:#a
             spacetail =  pygame.transform.flip( spacetail, True, False)
        
        if dx == 0 and dy == -1:#w
            fire = pygame.transform.rotate(fire, 90)
        if dx == 0 and dy == 1:#s
            fire = pygame.transform.rotate(fire, 270)
        if dx == -1 and dy == 0:#a
            fire =  pygame.transform.flip(fire, True, False)
        if dx == 0 and dy == -1:#w
            head_open = pygame.transform.rotate(head_open, 90)
        if dx == 0 and dy == 1:#s
            head_open = pygame.transform.rotate(head_open, 270)
        if dx == -1 and dy == 0:#a
            head_open = pygame.transform.flip(head_open, True, False)
        if dx == 0 and dy == -1:#w
            head = pygame.transform.rotate(head, 90)
        if dx == 0 and dy == 1:#s
            head = pygame.transform.rotate(head, 270)
        if dx == -1 and dy == 0:#a
            head = pygame.transform.flip(head, True, False)
        yabloko = pygame.transform.scale(yablokor,(SIZE,SIZE))
        grib = pygame.transform.scale(gribor,(SIZE,SIZE))
        surface.blit(img, (0, 0))
        # drawing snake
        [surface.blit(body, (i, j)) for i, j in snake[1:-1]]
        if length >1 and space == 0:
            surface.blit(tail,snake[0])
        if boshka == "Normal":
            surface.blit(head,snake[-1])
        if flamethrower == 1:
            surface.blit(fire,snake[0])
            surface.blit(head_open,snake[-1])
            boshka="0"
        if space ==1:
            surface.blit(spacefon, (0, 0))
            if length >1:
                surface.blit(spacetail,snake[0])
            [surface.blit(spacebody, (i, j)) for i, j in snake[1:-1]]
            surface.blit(spacehead,snake[-1])
            boshka="0"
            spacevav=1
        
        # drawinng apple
        #pygame.draw.rect(surface, pygame.Color('red'), (*apple, SIZE, SIZE))
        surface.blit(yabloko, apple)
        #show size
        render_score = font_score.render(f'Length: {length*SIZE}', 1, pygame.Color('red'))
        surface.blit(render_score, (1700, 5))
        #SPACE
        SPACE = pygame.font.SysFont('Imapct', 66, bold=False)
        SPACE1 = SPACE.render('Press SPACE to restart', 1, pygame.Color('red'))
        # show score
        render_score = font_score.render(f'Score: {score} Max: {maxscore}', 1, pygame.Color('red'))
        surface.blit(render_score, (5, 5))
        #metfall
        metfallrender = font_score.render(f'До метеоита: {metfall}', 1, pygame.Color('black'))
        surface.blit(metfallrender, (820, 10))
        if space == 1:
            metfallrender = font_score.render(f'До метеоита: {metfall}', 1, pygame.Color('red'))
            surface.blit(metfallrender, (820, 10))
        #metheorites
        # A = (X1, 0)
        # B = (X2, HEIGHT)
        # snake movement
        speed_count += 1
        if not speed_count % snake_speed:
            x += dx * SIZE
            y += dy * SIZE
            snake.append((x, y))
            snake = snake[-length:]
        # eating food
        # apples
        if (apple[0]<=snake[-1][0]<=apple[0]+SIZE) and (apple[1]<=snake[-1][1]<=apple[1]+SIZE) or (apple[0]<=snake[-1][0]+SIZE<=apple[0]+SIZE) and (apple[1]<=snake[-1][1]<=apple[1]+SIZE) or (apple[0]<=snake[-1][0]<=apple[0]+SIZE) and (apple[1]<=snake[-1][1]+SIZE<=apple[1]+SIZE) or (apple[0]<=snake[-1][0]+SIZE<=apple[0]+SIZE) and (apple[1]<=snake[-1][1]+SIZE<=apple[1]+SIZE) :
            apple = randrange(SIZE, HEIGHT - SIZE, SIZE), randrange(SIZE, WIDTH - SIZE, SIZE)
            length += 1
            score += 1
            if score == maxscore+1:
                maxscore+=1
                #sc.write(str(maxscore))
            snake_speed -= 1
            snake_speed = max(snake_speed, 3)
            metfall=400
            if SIZE >15:
                SIZE -=5
            spawn = r.randint(1,10)
            if spawn==1 and mush[0]==0:
                mushroom = randrange(SIZE, HEIGHT - SIZE, SIZE), randrange(SIZE, WIDTH - SIZE, SIZE)
                mush[0]=1
                grewup=300
            aspawn = r.randint(1,20)
            if aspawn==1 and amush[0]==0:
                amushroom = randrange(SIZE, HEIGHT - SIZE, SIZE), randrange(SIZE, WIDTH - SIZE, SIZE)
                amush[0]=1
                agrewup=1000
        grewup-=1
        agrewup-=1
        if mush[0]==1 and grewup>0:
            if grewup<=300 and grewup>200:
                surface.blit(grib, mushroom)
            if grewup<=200 and grewup>100:
                surface.blit(grib1, mushroom)
            if grewup<=100:
                surface.blit(grib2, mushroom)
            if(mushroom[0]<=snake[-1][0]<=mushroom[0]+SIZE) and (mushroom[1]<=snake[-1][1]<=mushroom[1]+SIZE) or (mushroom[0]<=snake[-1][0]+SIZE<=mushroom[0]+SIZE) and (mushroom[1]<=snake[-1][1]<=mushroom[1]+SIZE) or (mushroom[0]<=snake[-1][0]<=mushroom[0]+SIZE) and (mushroom[1]<=snake[-1][1]+SIZE<=mushroom[1]+SIZE) or (mushroom[0]<=snake[-1][0]+SIZE<=mushroom[0]+SIZE) and (mushroom[1]<=snake[-1][1]+SIZE<=mushroom[1]+SIZE) :
                if grewup<=300 and grewup>200:
                    length-=1
                    score+=10
                    snake_speed+=5
                    mush[0]=0
                elif grewup<=200 and grewup>100:
                    length-=1
                    score+=5
                    mush[0]=0
                elif grewup<=100:
                    score+=5
                    mush[0]=0
        if grewup <0:
            mush[0]=0
        if agrewup <0:
            amush[0]=0
        if amush[0]==1:
            surface.blit(agrib, amushroom)
            if(amushroom[0]<=snake[-1][0]<=amushroom[0]+SIZE) and (amushroom[1]<=snake[-1][1]<=amushroom[1]+SIZE) or (amushroom[0]<=snake[-1][0]+SIZE<=amushroom[0]+SIZE) and (amushroom[1]<=snake[-1][1]<=amushroom[1]+SIZE) or (amushroom[0]<=snake[-1][0]<=amushroom[0]+SIZE) and (amushroom[1]<=snake[-1][1]+SIZE<=amushroom[1]+SIZE) or (amushroom[0]<=snake[-1][0]+SIZE<=amushroom[0]+SIZE) and (amushroom[1]<=snake[-1][1]+SIZE<=amushroom[1]+SIZE) :
                if space == 0: 
                    space=1
                if spacevav == 1:
                    space=0
                    boshka="Normal"
                    spacevav=0
                amush[0]=0
                    


        if dx ==0 and dy == 0:
            metfall=400
        metfall-=1
        if metfall <=0:
            metfall=0
            metfall2=1
            if metfall2==1:
                b = (X1*HEIGHT)/(X1-X2)
                k = -HEIGHT/(X1-X2)
                astery+=10
                asterx = (astery - b) / k
                surface.blit(aster, (asterx,astery))
                if astery>960:
                    astery=0
                    X1 = r.randint(0, WIDTH)
                    X2 = r.randint(0, WIDTH)
                    metfall=400
                    metfall2=0
        # game over 
        if x < 0 or x > HEIGHT - SIZE or y < 0 or y > WIDTH - SIZE or len(snake) != len(set(snake)) or (asterx<=snake[-1][0]<=asterx+SIZE) and (astery<=snake[-1][1]<=astery+SIZE) or (asterx<=snake[-1][0]+SIZE<=asterx+SIZE) and (astery<=snake[-1][1]<=astery+SIZE) or (asterx<=snake[-1][0]<=asterx+SIZE) and (astery<=snake[-1][1]+SIZE<=astery+SIZE) or (asterx<=snake[-1][0]+SIZE<=asterx+SIZE) and (astery<=snake[-1][1]+SIZE<=astery+SIZE):
            status="game over"
        if status=="game over":
            while True:
                render_end = font_end.render('GAME OVER', 1, pygame.Color('orange'))
                surface.blit(SPACE1, (HEIGHT // 2 - 250, HEIGHT // 2))
                surface.blit(render_end, (HEIGHT // 2 - 200, HEIGHT // 3))
                #МЕГАХАРОШ
                idk+=1
                if idk >400:
                    idk=0
                if score <=20:
                    Streak = SPACE.render('Плох', 1, pygame.Color('red'))
                    surface.blit(Streak, (910,100))
                if score >=20 and score<=40:
                    Streak = SPACE.render('Харош', 1, pygame.Color('red'))
                    surface.blit(Streak, (910,100))
                if score >40 and score<=100:
                    Streak = SPACE.render('Мегахарош', 1, pygame.Color('red'))
                    surface.blit(Streak, (910,100))
                if score > 100:
                    if idk <= 100:
                        Streak = SPACE.render('УЛЬТРАСУПЕРМЕГАХАРОШ', 1, pygame.Color('yellow'))
                        surface.blit(Streak, (700,100))
                    if idk <= 200 and idk >100:
                        Streak = SPACE.render('УЛЬТРАСУПЕРМЕГАХАРОШ', 1, pygame.Color('Violet'))
                        surface.blit(Streak, (700,100))
                    if idk <= 300 and idk >200:
                        Streak = SPACE.render('УЛЬТРАСУПЕРМЕГАХАРОШ', 1, pygame.Color('green'))
                        surface.blit(Streak, (700,100))
                    if idk <= 400 and idk >300:
                        Streak = SPACE.render('УЛЬТРАСУПЕРМЕГАХАРОШ', 1, pygame.Color('red'))
                        surface.blit(Streak, (700,100))

                pygame.display.flip()
                close_game()
                #Restarts
                key = pygame.key.get_pressed()
                if key[pygame.K_SPACE]:
                    status="game"
                    # objects spawn
                    x, y = randrange(SIZE, HEIGHT - SIZE, SIZE), randrange(SIZE, WIDTH - SIZE, SIZE)
                    apple = randrange(SIZE, HEIGHT - SIZE, SIZE), randrange(SIZE, WIDTH - SIZE, SIZE)
                    # значения переменным для новой игры
                    SIZE=100
                    length = 1
                    snake = [(x, y)]
                    dx, dy = 0, 0
                    fps = 60
                    dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
                    score = 0
                    speed_count, snake_speed = 0, 10
                    mush=[0]
                    amush=[0]
                    grewup=0
                    agrewup=0
                    astery = 0
                    asterx = 0
                    X1 = r.randint(0, WIDTH)
                    X2 = r.randint(0, WIDTH)
                    metfall=1000
                    break
                elif key [pygame.K_ESCAPE]:
                    status="menu"
                    break
                    
                    
                    
        pygame.display.flip()
        clock.tick(fps)
        close_game()
        cheat=[]
        # controls
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            if dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
        elif key[pygame.K_s]:
            if dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
        elif key[pygame.K_a]:
            if dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
        elif key[pygame.K_d]:
            if dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True, }
        elif key[pygame.K_l]:
            fps=10     
        elif key[pygame.K_k]: 
            fps=60 
        elif key[pygame.K_f]:
            flamethrower=1
        elif key[pygame.K_v]:
            flamethrower=0
            boshka="Normal"
        elif key[pygame.K_UP]:
            if dirs['W']:
                dx, dy = 0, -1
                dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
        elif key[pygame.K_DOWN]:
            if dirs['S']:
                dx, dy = 0, 1
                dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
        elif key[pygame.K_LEFT]:
            if dirs['A']:
                dx, dy = -1, 0
                dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
        elif key[pygame.K_RIGHT]:
            if dirs['D']:
                dx, dy = 1, 0
                dirs = {'W': True, 'S': True, 'A': False, 'D': True, } 
        elif key[pygame.K_ESCAPE]:
            status="pause"