import pygame, sys

from pygame.locals import *
from random import randint
pygame.init()

FPS = 10 
fpsClock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (255, 20, 255)
silver = (192, 192, 192)

gameDisplay = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('LUDO GAME')

def drawingboard():
         
        gameDisplay.fill(black) 
        pygame.draw.rect(gameDisplay, red, [750, 0, 250, 250])
        pygame.draw.rect(gameDisplay, green,[300, 0, 250, 250])   
        pygame.draw.rect(gameDisplay, yellow, [300, 450, 250, 250])
        pygame.draw.rect(gameDisplay, blue, [750, 450, 250, 250])    
        pygame.draw.rect(gameDisplay, white, [618, 0, 62, 700])
        pygame.draw.rect(gameDisplay, white, [552, 0, 64, 700])
        pygame.draw.rect(gameDisplay, white, [682, 0, 66, 700])
        pygame.draw.rect(gameDisplay, white, [300, 318, 700, 62])
        pygame.draw.rect(gameDisplay, white, [300, 252, 700, 64])
        pygame.draw.rect(gameDisplay, white, [300, 382, 700, 66])
        pygame.draw.rect(gameDisplay, green, [341, 318, 250, 62])
        pygame.draw.rect(gameDisplay, green, [341, 252, 40, 64])
        pygame.draw.rect(gameDisplay, blue, [750, 318, 211, 62])
        pygame.draw.rect(gameDisplay, blue, [917, 382, 44, 66])
        pygame.draw.rect(gameDisplay, red, [618, 41, 62, 210])
        pygame.draw.rect(gameDisplay, red, [682, 41, 66, 37])
        pygame.draw.rect(gameDisplay, yellow, [618, 450, 62, 211])
        pygame.draw.rect(gameDisplay, yellow, [552, 618, 64, 44])
        pygame.draw.rect(gameDisplay, black, [422, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [339, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [378, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [461, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [502, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [872, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [789, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [828, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [916, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [961, 250, 2, 200])
        pygame.draw.rect(gameDisplay, black, [550, 250, 200, 200])
        pygame.draw.rect(gameDisplay, black, [550, 122, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 39, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 78, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 161, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 208, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 572, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 489, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 528, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 616, 200, 2])
        pygame.draw.rect(gameDisplay, black, [550, 661, 200, 2])
        pygame.draw.rect(gameDisplay, white, [552, 252, 196, 196])
        pygame.draw.polygon(gameDisplay, red, ((552, 252), (748, 252), (650, 350)))
        pygame.draw.polygon(gameDisplay, green, ((552,252), (650, 350), (552, 448)))
        pygame.draw.polygon(gameDisplay, blue, ((747,252), (650, 350), (746, 446)))
        pygame.draw.polygon(gameDisplay, yellow, ((650, 350), (748,448),(551,447)))
        pygame.draw.line(gameDisplay, black, (552, 252),(748, 448),3)
        pygame.draw.line(gameDisplay, black, (748, 250),(552,448),3)
        pygame.draw.rect(gameDisplay, black, [350, 50, 150, 150])
        pygame.draw.rect(gameDisplay, white, [352, 52, 146, 146])
        pygame.draw.rect(gameDisplay, black, [366, 66, 50, 50])
        pygame.draw.rect(gameDisplay, green, [367, 67, 48, 48])
        pygame.draw.rect(gameDisplay, black, [430, 66, 50, 50])
        pygame.draw.rect(gameDisplay, green, [431, 67, 48, 48])
        pygame.draw.rect(gameDisplay, black, [366, 132, 50, 50])
        pygame.draw.rect(gameDisplay, green, [367, 133, 48, 48])
        pygame.draw.rect(gameDisplay, black, [430, 132, 50, 50])
        pygame.draw.rect(gameDisplay, green, [431, 133, 48, 48])
        pygame.draw.rect(gameDisplay, black, [800, 50, 150, 150]) 
        pygame.draw.rect(gameDisplay, white, [802, 52, 146, 146])
        pygame.draw.rect(gameDisplay, black, [816, 66, 50, 50])
        pygame.draw.rect(gameDisplay, red, [817, 67, 48, 48])
        pygame.draw.rect(gameDisplay, black, [880, 66, 50, 50])
        pygame.draw.rect(gameDisplay, red, [881, 67, 48, 48])
        pygame.draw.rect(gameDisplay, black, [816, 134, 50, 50])
        pygame.draw.rect(gameDisplay, red, [817, 135, 48, 48])
        pygame.draw.rect(gameDisplay, black, [880, 134, 50, 50])
        pygame.draw.rect(gameDisplay, red, [881, 135, 48, 48])
        pygame.draw.rect(gameDisplay, black, [350, 500, 150, 150])
        pygame.draw.rect(gameDisplay, white, [352, 502, 146, 146])
        pygame.draw.rect(gameDisplay, black, [366, 516, 50, 50])
        pygame.draw.rect(gameDisplay, yellow, [367, 517, 48, 48])
        pygame.draw.rect(gameDisplay, black, [430, 516, 50, 50])
        pygame.draw.rect(gameDisplay, yellow, [431, 517, 48, 48])
        pygame.draw.rect(gameDisplay, black, [366, 584, 50, 50])
        pygame.draw.rect(gameDisplay, yellow, [367, 585, 48, 48])
        pygame.draw.rect(gameDisplay, black, [430, 584, 50, 50])
        pygame.draw.rect(gameDisplay, yellow, [431, 585, 48, 48])
        pygame.draw.rect(gameDisplay, black, [800, 500, 150, 150])
        pygame.draw.rect(gameDisplay, white, [802, 502, 146, 146])
        pygame.draw.rect(gameDisplay, black, [816, 516, 50, 50])
        pygame.draw.rect(gameDisplay, blue, [817, 517, 48, 48])
        pygame.draw.rect(gameDisplay, black, [880, 516, 50, 50])
        pygame.draw.rect(gameDisplay, blue, [881, 517, 48, 48])
        pygame.draw.rect(gameDisplay, black, [816, 584, 50, 50])
        pygame.draw.rect(gameDisplay, blue, [817, 585, 48, 48])
        pygame.draw.rect(gameDisplay, black, [880, 584, 50, 50])
        pygame.draw.rect(gameDisplay, blue, [881, 585, 48, 48])
        pygame.draw.rect(gameDisplay, silver, [0, 0, 298, 700])
        
def Text(string,(cx,cy),fontSize,color):
    fontObj = pygame.font.Font('freesansbold.ttf',fontSize)
    textSurfObj = fontObj.render(string,True,color)
    textRectObj = textSurfObj.get_rect()
    textRectObj.center = (cx,cy)
    gameDisplay.blit(textSurfObj,textRectObj)

def showButtonRoll():
    pygame.draw.rect(gameDisplay,black,(50,600,200,40))
    Text("Roll",(150,620),32,white)

def showButtonMove():
    Text("Instructions",(150,123),24,black)
    Text("1. Movement starts only",(130,155), 16, black)
    Text("on the roll of '1' or '6'",(130,175), 16, black)
    Text("2. Roll the dice",(95,195),16,black)
    Text("3. Then choose the piece ",(135,215),16,black) 
    Text("4. Later move the piece",(125,235),16,black)
    Text("5. Player who moves all",(128,255),16,black) 
    Text("the four pieces first ",(130,275),16,black)
    Text("into home is Winner ",(130,295),16,black)     
    pygame.draw.rect(gameDisplay,black,(50,650,200,40))
    Text("Move",(150,670),32,white)
    
def showDiceBox(n):
    Dice_image = pygame.image.load('Dice.jpg')
    gameDisplay.blit(Dice_image,(80,330)) 
    Text(str(n),(132,412),32,black)

def showTurnBox(n):
    pygame.draw.rect(gameDisplay,black,(20,10,250,40))
    Text("Now p"+ str(n),(100,30),20,white)
    Text("is playing",(190,30),20,white)
    pygame.draw.rect(gameDisplay,black,(20,70,250,40))
    
def showLudoButtons(): 
    pygame.draw.rect(gameDisplay,black,(50,550,40,40),3)
    Text(str(1),(70,570),32,black)
    pygame.draw.rect(gameDisplay,black,(100,550,40,40),3)
    Text(str(2),(120,570),32,black)
    pygame.draw.rect(gameDisplay,black,(150,550,40,40),3)
    Text(str(3),(170,570),32,black)
    pygame.draw.rect(gameDisplay,black,(200,550,40,40),3)
    Text(str(4),(220,570),32,black)
    pygame.draw.rect(gameDisplay,black,(30,505,220,30))
    Text('Select Piece Number',(140,520),20,white)
    pygame.draw.rect(gameDisplay,black,(370,23, 80, 25))
    Text('player1',(410,35),20,white)
    pygame.draw.rect(gameDisplay,black,(820,23, 80, 25))
    Text('player2',(860,35),20,white)
    pygame.draw.rect(gameDisplay,black,(370,473, 80, 25))
    Text('player3',(410,485),20,white)
    pygame.draw.rect(gameDisplay,black,(820,473, 80, 25))
    Text('player4',(860,485),20,white)

class LudoButton:
    radius = 15
    center_x = 0
    center_y = 0

    def drawLudoButton(self,color,(center_x,center_y)):
        self.center_x = center_x
        self.center_y = center_y
        pygame.draw.circle(gameDisplay,color,(self.center_x,self.center_y),self.radius,0)       
        Text("Now piece" + str(movepiece),(90,90),20,white)
        Text("is moving",(200,90),20,white)

class Player (LudoButton):   
    def __init__(self,color,track):
        self.color = color   
        self.LudobuttonList = [LudoButton() for i in range(1,5)]   
        self.finalstatus = [0,0,0,0]                               
        self.initialstatus = [0,0,0,0]                             
        self.track = track                                         
        self.currentposition = [-1,-1,-1,-1]  

    def placeLudoButtons(self,position,initiated):      
        for i in range(4):
            if initiated[i] != position[i]:
                pygame.draw.circle(gameDisplay,purple,position[i-1],17,0)
                self.drawLudoButton(self.color,position[i-1])
                Text(str(i + 1), (self.center_x, self.center_y), 17, black)

    def makeAMove(self,current):
        pygame.draw.circle(gameDisplay,self.color,self.track[current + 1],self.radius,0)

    def InitiateStart(self, btn_no):
        pygame.draw.circle(gameDisplay,self.color,self.track[0],self.radius,0)

    def isInHome(self):     
        for i in range (4):
            if(self.currentposition[i] == 56 and self.finalstatus[i] != 1):
                self.finalstatus[i] = 1

    def displayTransitButtons(self):
        for i in range(4):
            if(self.currentposition[i] != -1):
                pygame.draw.circle(gameDisplay,purple,self.track[self.currentposition[i]],17,0)
                self.drawLudoButton(self.color,self.track[self.currentposition[i]])
                Text(str(i + 1),(self.center_x, self.center_y), 17, black)

track1 = [(580,635),(580,592),(580,550),(580,509),(580,468),(525,410),(482,410),(441,410),(400,410), (359,410),(320,410),(320,350),(320,290),(359,290),(400,290),(441,290),(482,290),(525,290),(580,230),(580,184),(580,142),(580,100),(580,60),(580,21),(648,21),(710,21),(710,60),(710,100),(710,142),(710,184),(710,230),(770,280),(809,280),(847,280),(898,280),(938,280),(980,280),(980,350),(980,410),(938,410),(892,410),(849,410),(810,410),(770,410),(712,469),(712,509),(712, 552),(712,596),(712,642),(712,686),(648,682),(648,635),(648,596),(648, 552),(648,509),(648,469),(655,420)]

track2 = [(359,290),(400,290),(441,290),(482,290),(525,290),(580,230),(580,184),(580,142),(580,100),(580, 60),(580, 21),(648,21),(710,21),(710,60),(710,100),(710,142),(710,184),(710, 230),(770,280),(809,280),(847,280),(898,280),(938,280),(980,280),(980,350),(980,410),(938,410),(892,410),(849,410),(810,410),(770, 410),(712,469),(712,509),(712,552),(712, 596),(712,642),(712, 686),(648,682),(580,682),(580,635),(580,592),(580, 550),(580,509),(580,468),(525,410),(482,410),(441,410),(400,410),(359,410),(320, 410), (320,350),(359,350),(400,350),(441,350),(482,350),(525, 350),(576,350)]

track3 = [(710,60),(710,100),(710,142),(710,184),(710,230),(770, 280),(809,280),(847,280),(898,280),(938,280),(980,280),(980,350),(980, 410),(938,410),(892,410),(849,410),(810,410),(770, 410),(712,469),(712,509),(712,552),(712, 596),(712,642),(712, 686),(648,682),(580,682),(580,635),(580,592),(580,550),(580,509),(580,468),(525, 410),(482,410),(441,410),(400,410),(359,410),(320,410),(320,350),(320, 290),(359,290),(400,290),(441,290),(482,290),(525,290),(580,230),(580,184),(580,142),(580,100),(580,60),(590,21),(648,21),(648,60),(648,100),(648,142),(648,184),(648,230),(650,270)]

track4 = [(938, 410), (892, 410), (849, 410), (810, 410), (770, 410), (712, 469), (712, 509), (712,  552),(712, 596),(712,642),(712,686),(648, 682),(580,682),(580,635),(580, 592), (580, 550), (580, 509),(580,468), (525, 410), (482, 410), (441, 410),(400, 410), (359, 410),(320, 410), (320, 350), (320, 290), (359, 290), (400, 290), (441, 290),(482, 290), (525, 290),(580, 230), (580, 184), (580, 142), (580, 100), (580, 60), (580, 21), (648, 21),(710, 21), (710, 60),(710, 100), (710, 142), (710, 184), (710, 230), (770, 280), (809, 280), (847, 280),(898,280),(938,280),(980,280),(980,350), (938,350),(892, 350), (849, 350),(810, 350), (770, 350),(734,350)]

Player1 = Player(green, track2)
Player2 = Player(red, track3)
Player3 = Player(yellow, track1)
Player4 = Player(blue, track4)

position1 = [(389,89), (458,89), (389,158), (458,158)]
position2 = [(842,89), (904,89), (842,158), (904,158)]
position3 = [(389,544),(456,544), (389,608), (456,608)]
position4 = [(842,544), (904,544), (842,608), (904,608)]

initiated1 = [(0,0),(0,0),(0,0),(0,0)]
initiated2 = [(0,0),(0,0),(0,0),(0,0)]
initiated3 = [(0,0),(0,0),(0,0),(0,0)]
initiated4 = [(0,0),(0,0),(0,0),(0,0)]

mouse_x = 0   
mouse_y = 0   
mouseclick = False  
mousecount = 0
movepiece = 0     
player_id = 1     
move = 1            
dicenum = 0         
flag = 0
winner = 0

c = pygame.time.Clock() 
while True:   
    drawingboard()
    showButtonMove()
    showButtonRoll()
    if (mousecount == 0):
        showDiceBox(0)
    else:
        showDiceBox(dicenum)
    showLudoButtons()
    showTurnBox(player_id)   

    Player1.placeLudoButtons(position1,initiated1)   
    Player2.placeLudoButtons(position2,initiated2)  
    Player3.placeLudoButtons(position3,initiated3)  
    Player4.placeLudoButtons(position4,initiated4)  

    Player1.displayTransitButtons()      
    Player2.displayTransitButtons()
    Player3.displayTransitButtons()
    Player4.displayTransitButtons()
      
    for event in pygame.event.get():
        if event.type == QUIT:      
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:  
            (mouse_x,mouse_y) = event.pos  
            mouseclick = True
    if (mouseclick == True and mouse_x >= 50 and mouse_x <= 250 and mouse_y >= 600 and mouse_y <= 640):
        mousecount = 1
        dicenum = randint(1,6)     
        showDiceBox(dicenum)       
        mouseclick = False  
    if (mouseclick == True and mouse_y >= 550 and mouse_y <= 590):  
        if(mouse_x >= 50 and mouse_x <= 90):
            movepiece = 1
        elif(mouse_x >= 100 and mouse_x <= 140):
            movepiece = 2
        elif(mouse_x >= 150 and mouse_x <= 190):
            movepiece = 3                         
        elif(mouse_x >= 200 and mouse_x <= 240):
            movepiece = 4
        mouseclick = False          
    elif (mouseclick == True and mouse_x >= 50 and mouse_x <= 250 and mouse_y >= 650 and mouse_y <= 690):
        if (player_id == 1):      
            if (Player1.finalstatus[0] == 1 and Player1.finalstatus[1] == 1 and Player1.finalstatus[2] == 1 and Player1.finalstatus[3] == 1):
                player_id = 2
                print("Winner is player1")
                winner = 1
            else:
                if (movepiece == 1):  
                    if (flag == 0):
                        diff = (56 - Player1.currentposition[0])
                        flag = 1
                    if (Player1.initialstatus[0] == 0):
                        if (dicenum == 6 or dicenum == 1):     
                            Player1.initialstatus[0] = 1    
                            initiated1[0] = position1[0]    
                            Player1.InitiateStart(1)       
                            mouseclick = False            
                            Player1.currentposition[0] = 0
                        else:
                            player_id = 2 
                            mouseclick = False   
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0
                            if (Player1.finalstatus[0] != 1):
                                if (Player1.currentposition[0] >= 50 and dicenum <= diff):
                                    Player1.makeAMove(Player1.currentposition[0])
                                    Player1.currentposition[0] += 1
                                    move+=1
                                elif (Player1.currentposition[0] < 50):
                                    Player1.makeAMove(Player1.currentposition[0])
                                    Player1.currentposition[0] += 1
                                    move += 1
                                else:
                                    player_id = 2
                                    move = 1
                                    mouseclick = False
                        elif (move > dicenum):
                            player_id = 2
                            move = 1
                            mouseclick = False
                if (movepiece == 2):
                    if (flag == 0):
                        diff = (56 - Player1.currentposition[1])
                        flag = 1

                    if (Player1.initialstatus[1] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player1.initialstatus[1] = 1
                            initiated1[1] = position1[1]
                            Player1.InitiateStart(2)
                            mouseclick = False
                            Player1.currentposition[1] = 0
                        else:
                            player_id = 2
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player1.finalstatus[1] != 1):
                                if (Player1.currentposition[1] >= 50 and dicenum <= diff):
                                    Player1.makeAMove(Player1.currentposition[1])
                                    Player1.currentposition[1] += 1
                                    move += 1
                                elif (Player1.currentposition[1] < 50):
                                    Player1.makeAMove(Player1.currentposition[1])
                                    Player1.currentposition[1] += 1
                                    move += 1
                                else:
                                    player_id = 2
                                    move = 1
                                    mouseclick = False
                        elif (move > dicenum):
                            player_id = 2
                            move = 1
                            mouseclick = False
                if (movepiece == 3):
                    if(flag == 0):
                        diff = (56 - Player1.currentposition[2])
                        flag = 1
                    if (Player1.initialstatus[2] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player1.initialstatus[2] = 1
                            initiated1[2] = position1[2]
                            Player1.InitiateStart(3)
                            mouseclick = False
                            Player1.currentposition[2] = 0          
                        else:
                            player_id = 2
                            mouseclick =False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0
                            if (Player1.finalstatus[2] !=1):
                                if (Player1.currentposition[2] >= 50 and dicenum <= diff):
                                    Player1.makeAMove(Player1.currentposition[2])
                                    Player1.currentposition[2] += 1
                                    move += 1
                                elif (Player1.currentposition[2] < 50):
                                    Player1.makeAMove(Player1.currentposition[2])
                                    Player1.currentposition[2] += 1
                                    move += 1
                                else:
                                    player_id = 2
                                    move = 1
                                    mouseclick = False
                        elif (move > dicenum):
                            player_id = 2
                            move = 1
                            mouseclick = False
                if (movepiece == 4):
                    if (flag == 0):
                        diff = (56 - Player1.currentposition[3])
                        flag = 1
                    if (Player1.initialstatus[3] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player1.initialstatus[3] = 1
                            initiated1[3] = position1[3]
                            Player1.InitiateStart(4)
                            mouseclick = False
                            Player1.currentposition[3] = 0
                        else:
                            player_id = 2
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0
                            if (Player1.finalstatus[3] !=1):
                                if (Player1.currentposition[3] >= 50 and dicenum <= diff):
                                    Player1.makeAMove(Player1.currentposition[3])
                                    Player1.currentposition[3] += 1
                                    move += 1
                                elif (Player1.currentposition[3] < 50):
                                    Player1.makeAMove(Player1.currentposition[3])
                                    Player1.currentposition[3] += 1
                                    move += 1
                                else:
                                    player_id = 2
                                    move = 1
                                    mouseclick = False
                        elif (move > dicenum):
                            player_id = 2
                            move = 1
                            mouseclick = False
        elif (player_id == 2):
            if (Player2.finalstatus[0] == 1 and Player2.finalstatus[1] == 1 and Player2.finalstatus[2] == 1 and Player2.finalstatus[3] == 1):
                player_id = 3
                print ("Winner is player2")
                winner = 2
            else:
                if (movepiece == 1):
                    if (flag == 0):
                        diff = (56 - Player2.currentposition[0])
                        flag = 1
                    if (Player2.initialstatus[0] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player2.initialstatus[0] = 1
                            initiated2[0] = position2[0]
                            Player2.InitiateStart(1)
                            mouseclick = False
                            Player2.currentposition[0] = 0
                        else:
                            player_id = 3
                            mouseclick =False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player2.finalstatus[0] !=1):
                                if (Player2.currentposition[0] >= 50 and dicenum <= diff):
                                    Player2.makeAMove(Player2.currentposition[0])
                                    Player2.currentposition[0] += 1
                                    move += 1
                                elif (Player2.currentposition[0] < 50):
                                    Player2.makeAMove(Player2.currentposition[0])
                                    Player2.currentposition[0] += 1
                                    move += 1
                                else:
                                    player_id = 3
                                    move = 1
                                    mouseclick = False
                        elif (move > dicenum):
                            player_id = 3
                            move = 1
                            mouseclick = False
                if (movepiece == 2):
                    if (flag == 0):
                        diff = (56 - Player2.currentposition[1])
                        flag = 1
                    if(Player2.initialstatus[1] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player2.initialstatus[1] = 1
                            initiated2[1] = position2[1]
                            Player2.InitiateStart(2)
                            mouseclick = False
                            Player2.currentposition[1] = 0
                        else:
                            player_id = 3
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player2.finalstatus[1] !=1):
                                if (Player2.currentposition[1] >= 50 and dicenum <= diff):
                                    Player2.makeAMove(Player2.currentposition[1])
                                    Player2.currentposition[1] += 1
                                    move += 1
                                elif(Player2.currentposition[1] < 50):
                                    Player2.makeAMove(Player2.currentposition[1])
                                    Player2.currentposition[1] += 1
                                    move += 1
                                else:
                                    player_id = 3
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 3
                            move = 1
                            mouseclick = False
                if (movepiece == 3):
                    if (flag == 0):
                        diff = (56 - Player2.currentposition[2])
                        flag = 1

                    if (Player2.initialstatus[2] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player2.initialstatus[2] = 1
                            initiated2[2] = position2[2]
                            Player2.InitiateStart(3)
                            mouseclick = False
                            Player2.currentposition[2] = 0
                        else:
                            player_id = 3
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player2.finalstatus[2] !=1):
                                if (Player2.currentposition[2] >= 50 and dicenum <= diff):
                                    Player2.makeAMove(Player2.currentposition[2])
                                    Player2.currentposition[2] += 1
                                    move += 1

                                elif (Player2.currentposition[2] < 50):
                                    Player2.makeAMove(Player2.currentposition[2])
                                    Player2.currentposition[2] += 1
                                    move += 1
                                else:
                                    player_id = 3
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 3
                            move = 1
                            mouseclick = False
                if (movepiece == 4):
                    if (flag == 0):
                        diff = (56 - Player2.currentposition[3])
                        flag = 1

                    if (Player2.initialstatus[3] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player2.initialstatus[3] = 1
                            initiated2[3] = position2[3]
                            Player2.InitiateStart(4)
                            mouseclick = False
                            Player2.currentposition[3] = 0
                        else:
                            player_id = 1
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player2.finalstatus[3] !=1):
                                if (Player2.currentposition[3] >= 50 and dicenum <= diff):
                                    Player2.makeAMove(Player2.currentposition[3])
                                    Player2.currentposition[3] += 1
                                    move += 1
                                elif (Player2.currentposition[3] < 50):
                                    Player2.makeAMove(Player2.currentposition[3])
                                    Player2.currentposition[3] += 1
                                    move += 1
                                else:
                                    player_id = 3
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 3
                            move = 1
                            mouseclick = False

        elif (player_id == 3):
            if (Player3.finalstatus[0] == 1 and Player3.finalstatus[1] == 1 and Player3.finalstatus[2] == 1 and Player3.finalstatus[3] == 1):
                player_id = 4
                print("winner is player3")
                winner = 3
            else:
                if (movepiece ==1):
                    if (flag == 0):
                        diff = (56 - Player3.currentposition[0])
                        flag = 1
                    
                    if (Player3.initialstatus[0] == 0):
                        if (dicenum == 6 or dicenum == 1):

                            Player3.initialstatus[0] = 1
                            initiated3[0] = position3[0]
                            Player3.InitiateStart(1)
                            mouseclick = False
                            Player3.currentposition[0] = 0
                        else:
                            player_id = 4
                            mouseclick =False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player3.finalstatus[0] !=1):
                                if (Player3.currentposition[0] >= 50 and dicenum <= diff):
                                    Player3.makeAMove(Player3.currentposition[0])
                                    Player3.currentposition[0] += 1
                                    move += 1
                                elif (Player3.currentposition[0] < 50):
                                    Player3.makeAMove(Player3.currentposition[0])
                                    Player3.currentposition[0] += 1
                                    move += 1
                                else:
                                    player_id = 4
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 4
                            move = 1
                            mouseclick = False
                if (movepiece == 2):
                    if (flag == 0):
                        diff = (56 - Player3.currentposition[1])
                        flag = 1
                  
                    if (Player3.initialstatus[1] == 0):
                        if (dicenum == 6 or dicenum == 1):

                            Player3.initialstatus[1] = 1
                            initiated3[1] = position3[1]
                            Player3.InitiateStart(2)
                            mouseclick = False
                            Player3.currentposition[1] = 0
                        else:
                            player_id = 4  
                            mouseclick =False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player3.finalstatus[1] !=1):
                                if (Player3.currentposition[1] >= 50 and dicenum <= diff):
                                    Player3.makeAMove(Player3.currentposition[1])
                                    Player3.currentposition[1] += 1
                                    move += 1
                                elif (Player3.currentposition[1] < 50):
                                    Player3.makeAMove(Player3.currentposition[1])
                                    Player3.currentposition[1] += 1
                                    move += 1
                                else:
                                    player_id = 4
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 4
                            move = 1
                            mouseclick = False
                if (movepiece == 3):
                    if (flag == 0):
                        diff = (56 - Player3.currentposition[2])
                        flag = 1

                    if (Player3.initialstatus[2] == 0):
                        if (dicenum == 6 or dicenum == 1):

                            Player3.initialstatus[2] = 1
                            initiated3[2] = position3[2]
                            Player3.InitiateStart(3)
                            mouseclick = False
                            Player3.currentposition[2] = 0
                        else:
                            player_id = 4
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player3.finalstatus[2] != 1):

                                if (Player3.currentposition[2] >= 50 and dicenum <= diff):
                                    Player3.makeAMove(Player3.currentposition[2])
                                    Player3.currentposition[2] += 1
                                    move += 1

                                elif (Player3.currentposition[2] < 50):
                                    Player3.makeAMove(Player3.currentposition[2])
                                    Player3.currentposition[2] += 1
                                    move += 1
                                else:
                                    player_id = 4
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 4
                            move = 1
                            mouseclick = False
                if (movepiece == 4):
                    if (flag == 0):
                        diff = (56 - Player3.currentposition[3])
                        flag = 1

                    if (Player3.initialstatus[3] == 0):
                        if (dicenum == 6 or dicenum == 1):

                            Player3.initialstatus[3] = 1
                            initiated3[3] = position3[3]
                            Player3.InitiateStart(4)
                            mouseclick = False
                            Player3.currentposition[3] = 0
                        else:
                            player_id = 4
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player3.finalstatus[3] != 1):
                                if (Player3.currentposition[3] >= 50 and dicenum <= diff):
                                    Player3.makeAMove(Player3.currentposition[3])
                                    Player3.currentposition[3] += 1
                                    move += 1
                                elif (Player3.currentposition[3] < 50):
                                    Player3.makeAMove(Player3.currentposition[3])
                                    Player3.currentposition[3] += 1
                                    move += 1
                                else:
                                    player_id = 4
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 4
                            move = 1
                            mouseclick = False

        elif (player_id == 4):
            if (Player2.finalstatus[0] == 1 and Player2.finalstatus[1] == 1 and Player2.finalstatus[2] == 1 and Player2.finalstatus[3] == 1):
                player_id = 1
                print ("winner is player4")
                winner = 4
            else:
                if (movepiece == 1):
                    if (flag == 0):
                        diff = (56 - Player4.currentposition[0])
                        flag = 1

                    if (Player4.initialstatus[0] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player4.initialstatus[0] = 1
                            initiated4[0] = position4[0]
                            Player4.InitiateStart(1)
                            mouseclick = False
                            Player4.currentposition[0] = 0
                        else:
                            player_id = 1
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player4.finalstatus[0] != 1):
                                if (Player4.currentposition[0] >= 50 and dicenum <= diff):
                                    Player4.makeAMove(Player4.currentposition[0])
                                    Player4.currentposition[0] += 1
                                    move += 1
                                elif (Player4.currentposition[0] < 50):
                                    Player4.makeAMove(Player4.currentposition[0])
                                    Player4.currentposition[0] += 1
                                    move += 1
                                else:
                                    player_id = 1
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 1
                            move = 1
                            mouseclick = False
                if (movepiece == 2):
                    if (flag == 0):
                        diff = (56 - Player4.currentposition[1])
                        flag = 1

                    if (Player4.initialstatus[1] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player4.initialstatus[1] = 1
                            initiated4[1] = position4[1]
                            Player4.InitiateStart(2)
                            mouseclick = False
                            Player4.currentposition[1] = 0
                        else:
                            player_id = 1
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player4.finalstatus[1] != 1):
                                if (Player4.currentposition[1] >= 50 and dicenum <= diff):
                                    Player4.makeAMove(Player4.currentposition[1])
                                    Player4.currentposition[1] += 1
                                    move += 1
                                elif (Player4.currentposition[1] < 50):
                                    Player4.makeAMove(Player4.currentposition[1])
                                    Player4.currentposition[1] += 1
                                    move += 1
                                else:
                                    player_id = 1
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 1
                            move = 1
                            mouseclick = False
                if (movepiece == 3):
                    if (flag == 0):
                        diff = (56 - Player4.currentposition[2])
                        flag = 1

                    if (Player4.initialstatus[2] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player4.initialstatus[2] = 1
                            initiated4[2] = position4[2]
                            Player4.InitiateStart(3)
                            mouseclicked = False
                            Player4.currentposition[2] = 0
                        else:
                            player_id = 1
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player4.finalstatus[2] != 1):

                                if (Player4.currentposition[2] >= 50 and dicenum <= diff):
                                    Player4.makeAMove(Player4.currentposition[2])
                                    Player4.currentposition[2] += 1
                                    move += 1

                                elif (Player4.currentposition[2] < 50):                                   
                                    Player4.makeAMove(Player4.currentposition[2])
                                    Player4.currentposition[2] += 1
                                    move += 1
                                else:
                                    player_id = 1
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 1
                            move = 1
                            mouseclick = False
                if (movepiece == 4):
                    if(flag == 0):
                        diff = (56 - Player4.currentposition[3])
                        flag = 1
                    if (Player4.initialstatus[3] == 0):
                        if (dicenum == 6 or dicenum == 1):
                            Player4.initialstatus[3] = 1
                            initiated4[3] = position4[3]
                            Player4.InitiateStart(4)
                            mouseclick = False
                            Player4.currentposition[3] = 0
                        else:
                            player_id = 1
                            mouseclick = False
                    else:
                        if (move <= dicenum):
                            if (move == dicenum):
                                flag = 0

                            if (Player4.finalstatus[3] !=1):
                                if (Player4.currentposition[3] >= 50 and dicenum <= diff):
                                    Player4.makeAMove(Player4.currentposition[3])
                                    Player4.currentposition[3] += 1
                                    move += 1
                                elif (Player4.currentposition[3] < 50):
                                    Player4.makeAMove(Player4.currentposition[3])
                                    Player4.currentposition[3] += 1
                                    move += 1
                                else:
                                    player_id = 1
                                    move = 1
                                    mouseclick = False

                        elif (move > dicenum):
                            player_id = 1
                            move = 1
                            mouseclick = False
    Player1.isInHome()
    Player2.isInHome()
    Player3.isInHome()
    Player4.isInHome()

    pygame.display.update()
    fpsClock.tick(FPS)
