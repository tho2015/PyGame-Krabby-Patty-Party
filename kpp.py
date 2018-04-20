#Krabby Patty Party
#Mery,Lingxiao,Tszching
#press left or right arrow key to move spongebob
#catch the krabby patty to move on to the next level
from gamelib import*#imports the game library of classes and functions
game = Game (800,600,"Krabby patty party",30)#game object
bk = Image("bk8.jpg",game)#image object
bk.resizeTo(800,600)

sb = Image("spongebob.png",game)
sb.resizeBy(-45)
sb.moveTo(400,540)
bomb = Image("bomb.png",game)
bomb.resizeBy(-85)
bomb.moveTo(100,50)
clock = Image("clock.gif",game)                                                                                                                                                                                                                                                                          
clock.resizeBy(-60)
clock.moveTo(100,100)
bk1=Image("levelclear3.jpg",game)
bk1.resizeTo(800,600)
st=Image("bk7.jpg",game)
st.resizeTo(800,600)
pt=Image("patrick.png",game)
lose=Image("lose.jpg",game)
lose.resizeTo(800,600)
bkm=Sound("bkmusic.wav",1)
levelup=Sound("levelup.wav",2)
final=Image("final.jpg",game)
final.resizeTo(800,600)

kp = []
for index in range(30):
    kp.append( Image( "krabbypatty1.png",game))
    
for index in range(30):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(4,8)
    kp[index].resizeBy(-85)
    kp[index].moveTo(x, -y)
    kp[index].setSpeed(s,180)

bomb = []
for index in range(20):
    bomb.append( Image( "bomb.png",game))
    
for index in range(20):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(2,6)
    bomb[index].resizeBy(-85)
    bomb[index].moveTo(x, -y)
    bomb[index].setSpeed(s,180)

clock = []
for index in range(12):
    clock.append( Image( "clock.gif",game))
    
for index in range(12):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(4,7)
    clock[index].resizeBy(-60)
    clock[index].moveTo(x, -y)
    clock[index].setSpeed(s,180)

seashell = []
for index in range(10):
    seashell.append( Image( "seashell.gif",game))
    
for index in range(10):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(7,8)
    seashell[index].resizeBy(-65)
    seashell[index].moveTo(x, -y)
    seashell[index].setSpeed(s,180)

kpPassed = 0
kpcount = 0
bombPassed = 0
bombcount = 0
seashellPassed = 0
seashellcount = 0
clockPassed = 0
clockcount = 0
ptPassed = 0
ptcount = 0
#Title Screen
game.over = False
while not game.over:
    game.processInput()
    st.draw()
    bkm.play()
    if keys.Pressed[K_SPACE]:
          game.over = True

    game.update(30)
#Level1
game.over = False    
while not game.over:#while loops runs until game is over
    game.processInput()#process Input
    bk.draw()
    sb.draw()
    bkm.play()
    game.drawText("LEVEL ONE",250,5)
    for index in range(30):
        kp[index].move()
        if kp[index].collidedWith(sb):
            game.score+= 1
            kp[index].visible = False
        if kp[index].isOffScreen("bottom") and kp[index].visible:
            kpPassed += 1
            kp[index].visible = False

    for index in range(20):
        bomb[index].move()
        if bomb[index].collidedWith(sb):
             game.score-=3
             bomb[index].visible = False
        if bomb[index].isOffScreen("bottom") and bomb[index].visible:
            bombPassed += 1
            bomb[index].visible = False

    for index in range(10):
        seashell[index].move()
        if seashell[index].collidedWith(sb):
            kp[index].speed-=1
            seashell[index].visible = False
        if seashell[index].isOffScreen("bottom") and seashell[index].visible:
            seashellPassed += 1
            seashell[index].visible = False           


    for index in range(12):
        clock[index].move()
        if clock[index].collidedWith(sb):
            game.time+= 5
            clock[index].visible = False
        if clock[index].isOffScreen("bottom") and clock[index].visible:
            clockPassed += 1
            clock[index].visible = False    
 

   
    if keys.Pressed[K_RIGHT]:
        sb.x += 8
    if keys.Pressed[K_LEFT]:
        sb.x -= 8

    if game.score>=8:
        game.over = True
     
        
    if game.score<0 or game.time<1 :
        game.over = True
        lose.draw()
        
    game.displayScore()
    game.displayTime(100,5)

     
    game.update(30)

#Level Clear
game.over = False
while not game.over and game.score>=8:
    game.processInput()
    bk1.draw()
    levelup.play()

    if keys.Pressed[K_SPACE]:
        game.over=True

    game.update(30)

#lose
game.over = False
while not game.over and game.score<0 or game.time<1 :
    game.processInput()
    lose.draw()
   

    if keys.Pressed[K_SPACE]:
        game.over=True
        game.quit()
        
    game.update(30)
    game.over=False
#Level2
kp = []
for index in range(30):
    kp.append( Image( "krabbypatty1.png",game))
    
for index in range(30):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(4,8)
    kp[index].resizeBy(-85)
    kp[index].moveTo(x, -y)
    kp[index].setSpeed(s,180)

bomb = []
for index in range(25):
    bomb.append( Image( "bomb.png",game))
    
for index in range(25):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(2,6)
    bomb[index].resizeBy(-85)
    bomb[index].moveTo(x, -y)
    bomb[index].setSpeed(s,180)

clock = []
for index in range(10):
    clock.append( Image( "clock.gif",game))
    
for index in range(10):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(4,7)
    clock[index].resizeBy(-60)
    clock[index].moveTo(x, -y)
    clock[index].setSpeed(s,180)

seashell = []
for index in range(12):
    seashell.append( Image( "seashell.gif",game))
    
for index in range(12):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(7,8)
    seashell[index].resizeBy(-65)
    seashell[index].moveTo(x, -y)
    seashell[index].setSpeed(s,180)

pt = []
for index in range(10):
    pt.append( Image( "patrick.png",game))
    
for index in range(10):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(7,8)
    pt[index].resizeBy(-55)
    pt[index].moveTo(x, -y)
    pt[index].setSpeed(s,180)
#level2 game loop    
#game.over = False    
while not game.over and game.score>7:#while loops runs until game is over
    game.processInput()#process Input
    bk.draw()
    sb.draw()
    game.drawText("LEVEL TWO - Catch 4 more Krabby Patties to move on to next level",250,5)
    for index in range(30):
        kp[index].move()
        if kp[index].collidedWith(sb):
            game.score+= 1
            kp[index].visible = False
        if kp[index].isOffScreen("bottom") and kp[index].visible:
            kpPassed += 1
            kp[index].visible = False

    for index in range(25):
        bomb[index].move()
        if bomb[index].collidedWith(sb):
             game.score-=3
             bomb[index].visible = False
        if bomb[index].isOffScreen("bottom") and bomb[index].visible:
            bombPassed += 1
            bomb[index].visible = False

    for index in range(12):
        seashell[index].move()
        if seashell[index].collidedWith(sb):
            kp[index].speed-=1
            seashell[index].visible = False
        if seashell[index].isOffScreen("bottom") and seashell[index].visible:
            seashellPassed += 1
            seashell[index].visible = False           

    for index in range(10):
        clock[index].move()
        if clock[index].collidedWith(sb):
            game.time+= 5
            clock[index].visible = False
        if clock[index].isOffScreen("bottom") and clock[index].visible:
            clockPassed += 1
            clock[index].visible = False    
 
    for index in range(10):
        pt[index].move()
        if pt[index].collidedWith(sb):
            game.score-=10  
            pt[index].visible = False
        if pt[index].isOffScreen("bottom") and pt[index].visible:
            ptPassed += 1
            pt[index].visible = False  
   
    if keys.Pressed[K_RIGHT]:
        sb.x += 8
    if keys.Pressed[K_LEFT]:
        sb.x -= 8

    if game.score>=12:
        game.over = True
     
        
    '''if game.score<8:
        game.over = True'''

    if game.time<1 and game.score<12:
        game.over = True
        
    game.displayScore()
    game.displayTime(100,5)

     
    game.update(30)

#lose
game.over = False
while not game.over and game.score<=8 or game.time<1 :
    game.processInput()
    lose.draw()

    if keys.Pressed[K_SPACE]:
        game.over=True
        game.quit()
        
    game.update(30)


#Level Clear

game.over = False
while not game.over and game.score>11:
    game.processInput()
    bk1.draw()
    levelup.play()

    if keys.Pressed[K_SPACE]:
        game.over=True

    game.update(30)
game.over=False

#level3
kp = []
for index in range(30):
    kp.append( Image( "krabbypatty1.png",game))
    
for index in range(30):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(4,8)
    kp[index].resizeBy(-85)
    kp[index].moveTo(x, -y)
    kp[index].setSpeed(s,180)

bomb = []
for index in range(25):
    bomb.append( Image( "bomb.png",game))
    
for index in range(25):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(2,6)
    bomb[index].resizeBy(-85)
    bomb[index].moveTo(x, -y)
    bomb[index].setSpeed(s,180)

clock = []
for index in range(10):
    clock.append( Image( "clock.gif",game))
    
for index in range(10):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(4,7)
    clock[index].resizeBy(-60)
    clock[index].moveTo(x, -y)
    clock[index].setSpeed(s,180)

seashell = []
for index in range(12):
    seashell.append( Image( "seashell.gif",game))
    
for index in range(12):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(7,8)
    seashell[index].resizeBy(-65)
    seashell[index].moveTo(x, -y)
    seashell[index].setSpeed(s,180)

pt = []
for index in range(15):
    pt.append( Image( "patrick.png",game))
    
for index in range(15):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(8,9)
    pt[index].resizeBy(-55)
    pt[index].moveTo(x, -y)
    pt[index].setSpeed(s,180)
#level 3 game loop    
#game.over = False    
while not game.over and game.score>=12 :#while loops runs until game is over
    game.processInput()#process Input
    bk.draw()
    sb.draw()
    game.drawText("CATCH 8 MORE KRABBY PATTY  TO PASS THIS LEVEL!!",100,20)

    for index in range(30):
        kp[index].move()
        if kp[index].collidedWith(sb):
            game.score+= 1
            kp[index].visible = False
        if kp[index].isOffScreen("bottom") and kp[index].visible:
            kpPassed += 1
            kp[index].visible = False

    for index in range(25):
        bomb[index].move()
        if bomb[index].collidedWith(sb):
             game.score-=3
             bomb[index].visible = False
        if bomb[index].isOffScreen("bottom") and bomb[index].visible:
            bombPassed += 1
            bomb[index].visible = False

    for index in range(12):
        seashell[index].move()
        if seashell[index].collidedWith(sb):
            kp[index].speed-=1
            seashell[index].visible = False
        if seashell[index].isOffScreen("bottom") and seashell[index].visible:
            seashellPassed += 1
            seashell[index].visible = False           


    for index in range(10):
        clock[index].move()
        if clock[index].collidedWith(sb):
            game.time+= 5
            clock[index].visible = False
        if clock[index].isOffScreen("bottom") and clock[index].visible:
            clockPassed += 1
            clock[index].visible = False    
 
    for index in range(15):
        pt[index].move()
        if pt[index].collidedWith(sb):
            game.score-=10  
            pt[index].visible = False
        if pt[index].isOffScreen("bottom") and pt[index].visible:
            ptPassed += 1
            pt[index].visible = False  
   
    if keys.Pressed[K_RIGHT]:
        sb.x += 8
    if keys.Pressed[K_LEFT]:
        sb.x -= 8

    

    if game.score>=20:
        game.over = True
     
        
    if game.score<12:
        game.over = True
        lose.draw()
    if game.time<1:
        game.over = True
        lose.draw()        
    game.displayScore()
    game.displayTime(100,5)

     
    game.update(30)

#lose
game.over = False
while not game.over and game.score<=12 or game.time<1 :
    game.processInput()
    lose.draw()

    if keys.Pressed[K_SPACE]:
        game.over=True

    game.update(30)


#Level Clear

game.over = False
while not game.over and game.score>=20:
    game.processInput()
    final.draw()
    levelup.play()

    if keys.Pressed[K_SPACE]:
        game.over=True

    game.update(30)

game.quit()
