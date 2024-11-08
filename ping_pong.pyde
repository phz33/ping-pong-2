def setup():
    fullScreen()



cpu_y = 0
dir = 30
bola_x = 100
dir_x = 30
perdeu = False

def mouseClicked():
    global cpu_y  
    global dir
    global bola_x
    global dir_x
    global perdeu
    
    if perdeu == True:
        perdeu = False
        cpu_y = 0
        dir = 30
        bola_x = 100
        dir_x = 30
    

def draw():

    #computeitor
    global cpu_y  
    global dir
    global bola_x
    global dir_x
    global perdeu
    if perdeu == True:
        textAlign(CENTER)
        textSize(64)
        text('muito ruim(* *)kkkkkkkkkkkkkkkkkkkkkkkkk',width/2,height/2)
        return
    background(51)
    rectMode(CENTER) #define que o retangulo do computador sera frito apartir do canto 
    fill(240,138,138)
    rect(30,cpu_y,60,180)
    cpu_y += dir 
    if cpu_y + 20 >= height:
        dir = -5
    elif cpu_y <= 0:
        dir = 5
        
      #eu  
    
    rect(width - 30,mouseY,60,180)
    #bola
    rectMode(CORNER)
    ellipse(bola_x, cpu_y,20,20)
    bola_x += dir_x
    
    if bola_x + 20 >=width:
        perdeu = True
    elif bola_x <= 60:
        dir_x = 30
    
    #jogavel
    if bola_x >= width -90 and  cpu_y -15 >= mouseY -100 and cpu_y +15 <= mouseY +90:
        dir_x= -30
    
        
        
        
        
        
        
        
        
