import pygame
class Colisiones:
    
    def colisionNave(protagonista,escena1,escena2,escena3):
        if(escena1):
            if(protagonista.rect.x<50 and protagonista.rect.y>301 and protagonista.rect.y<800):
                protagonista.rect.x=60
            if(protagonista.rect.x<50 and protagonista.rect.y>90 and protagonista.rect.y<149):
                protagonista.rect.x=60
            if(protagonista.rect.x>680 and protagonista.rect.y>90 and protagonista.rect.y<800):
                protagonista.rect.x=670
            if(protagonista.rect.y<90 and protagonista.rect.x>20 and protagonista.rect.x<750):
                protagonista.rect.y=100
        if(escena2):
            if(protagonista.rect.x<60 and protagonista.rect.y>10 and protagonista.rect.y<800):
                protagonista.rect.x=70
            if(protagonista.rect.x>660 and protagonista.rect.y>5 and protagonista.rect.y<160):
                protagonista.rect.x=650
            if(protagonista.rect.x>660 and protagonista.rect.y>250 and protagonista.rect.y<800):
                protagonista.rect.x=650
            if(protagonista.rect.y<10 and protagonista.rect.x>60 and protagonista.rect.x<800):
                protagonista.rect.y=20
            #Mesa
            if(protagonista.rect.y>710 and protagonista.rect.x>60 and protagonista.rect.x<800):
                protagonista.rect.y=700
            if(protagonista.rect.y>610 and protagonista.rect.x>140 and protagonista.rect.x<610):
                protagonista.rect.y=600
            if((protagonista.rect.x>130 and protagonista.rect.x<135 ) and protagonista.rect.y>620 and protagonista.rect.y<800):
                protagonista.rect.x=120
            if((protagonista.rect.x>615 and protagonista.rect.x<620) and protagonista.rect.y>620 and protagonista.rect.y<800):
                protagonista.rect.x=625
        if(escena3):
            if(protagonista.rect.x<60 and protagonista.rect.y>-60 and protagonista.rect.y<800):
                protagonista.rect.x=70
            if(protagonista.rect.x>660 and protagonista.rect.y>-60 and protagonista.rect.y<800):
                protagonista.rect.x=650
            if(protagonista.rect.y>580 and protagonista.rect.x>160 and protagonista.rect.x<660):
                protagonista.rect.y = 570
            #Tanque de gasolina
            if(protagonista.rect.x>190 and protagonista.rect.x<195 and protagonista.rect.y>565):
                protagonista.rect.x=200
            if(protagonista.rect.y>520 and protagonista.rect.x>80 and protagonista.rect.x<149):
                protagonista.rect.y = 510
            if(protagonista.rect.y>560 and protagonista.rect.x>111 and protagonista.rect.x<190):
                protagonista.rect.y = 550
            if(protagonista.rect.x>150 and protagonista.rect.x<155 and protagonista.rect.y>550 and protagonista.rect.y<560):
                protagonista.rect.x = 160
            if(protagonista.rect.y>100 and protagonista.rect.y<360 and protagonista.rect.x>580 and protagonista.rect.x<760):
                protagonista.rect.y=90
            if(protagonista.rect.x>60 and protagonista.rect.x<99 and protagonista.rect.y>530):
                protagonista.rect.y = 520
            #Caja de armas
            if(protagonista.rect.x>570 and protagonista.rect.y>100 and protagonista.rect.y<360):
                protagonista.rect.x=560
            if(protagonista.rect.y<370 and protagonista.rect.y>100 and protagonista.rect.x>580 and protagonista.rect.x<760):
                protagonista.rect.y=380
    def colisionesMapa(flecha):
        if(flecha.rect.x<-10):
            flecha.rect.x=0
        if(flecha.rect.x>800):
            flecha.rect.x=790
    def colisionesLuna(protagonista,nave,luna1,luna2,luna3,luna4,luna5,luna6):
        if(luna1==True):
            if(protagonista.rect.x>680):
                protagonista.rect.x=670
            if(protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x-40) and protagonista.rect.y>(nave.rect.y-20) and protagonista.rect.y<(nave.rect.y+237)):
                protagonista.rect.x = nave.rect.x - 60
            if (protagonista.rect.y>(nave.rect.y-50) and protagonista.rect.y<(nave.rect.y-40) and protagonista.rect.x>(nave.rect.x-20) and protagonista.rect.x<(nave.rect.x+310)):
                protagonista.rect.y = nave.rect.y - 60
            if(protagonista.rect.x>(nave.rect.x+295) and protagonista.rect.x<(nave.rect.x+300) and protagonista.rect.y>(nave.rect.y-10) and protagonista.rect.y<(nave.rect.y+227)):
                protagonista.rect.x = nave.rect.x +310
            if(protagonista.rect.y>(nave.rect.y+227) and protagonista.rect.y<(nave.rect.y+237) and protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x+310)):
                protagonista.rect.y = nave.rect.y + 247
        if(luna2==True):
            if(protagonista.rect.x<45):
                protagonista.rect.x=55
            if(protagonista.rect.y>675):
                protagonista.rect.y=665
        if(luna4==True):
            if(protagonista.rect.x>675):
                protagonista.rect.x=665
            if(protagonista.rect.x<45):
                protagonista.rect.x=55
            if(protagonista.rect.y>675):
                protagonista.rect.y=665
        if(luna3==True):
            if(protagonista.rect.y<40):
                protagonista.rect.y=50
        if(luna5==True):
            if(protagonista.rect.x<45):
                protagonista.rect.x=55
            if(protagonista.rect.y<40):
                protagonista.rect.y=50
        if(luna6==True):
            if(protagonista.rect.x>670):
                protagonista.rect.x=660
            if(protagonista.rect.y<40):
                protagonista.rect.y=50
            if(protagonista.rect.y>675):
                protagonista.rect.y=665
                
    def colisionesMarte(protagonista,nave,marte1,marte2,marte3,marte4,marte5,marte6,marte8,marte9,marte10,marte11,primeraParaiso,segundaParaiso):
        if(marte1):
            if(protagonista.rect.y<35):
                protagonista.rect.y=45
            if(protagonista.rect.x<30):
                protagonista.rect.x=40
        if(marte2):
            if(protagonista.rect.y<35):
                protagonista.rect.y=45
        if(marte3):
            if(protagonista.rect.x>710):
                protagonista.rect.x=700
        if(marte4):
            if(protagonista.rect.x>710):
                protagonista.rect.x=700
            if(protagonista.rect.x<30):
                protagonista.rect.x=40
            if(protagonista.rect.y<35):
                protagonista.rect.y=45
            if(protagonista.rect.x>270 and protagonista.rect.x<275 and protagonista.rect.y>30 and protagonista.rect.y<230):
                protagonista.rect.x=260
            if(protagonista.rect.x>490 and protagonista.rect.x<495 and protagonista.rect.y>30 and protagonista.rect.y<230):
                protagonista.rect.x=500
            if(protagonista.rect.y>30 and protagonista.rect.y<40 and protagonista.rect.x>270 and protagonista.rect.x<490):
                protagonista.rect.y = 20
            if(protagonista.rect.y>220 and protagonista.rect.y<230 and protagonista.rect.x>270 and protagonista.rect.x<490):
                protagonista.rect.y = 230
        if(marte5):
            if(protagonista.rect.x<30):
                protagonista.rect.x=40
        if(marte6):
            if(protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x-40) and protagonista.rect.y>(nave.rect.y-20) and protagonista.rect.y<(nave.rect.y+237)):
                protagonista.rect.x = nave.rect.x - 60
            if(protagonista.rect.y>(nave.rect.y-50) and protagonista.rect.y<(nave.rect.y-40) and protagonista.rect.x>(nave.rect.x-20) and protagonista.rect.x<(nave.rect.x+310)):
                protagonista.rect.y = nave.rect.y - 60
            if(protagonista.rect.x>(nave.rect.x+295) and protagonista.rect.x<(nave.rect.x+300) and protagonista.rect.y>(nave.rect.y-10) and protagonista.rect.y<(nave.rect.y+227)):
                protagonista.rect.x = nave.rect.x +310
            if(protagonista.rect.y>(nave.rect.y+227) and protagonista.rect.y<(nave.rect.y+237) and protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x+310)):
                protagonista.rect.y = nave.rect.y + 247
        if(marte8):
            if(protagonista.rect.x>710):
                protagonista.rect.x=700
            if(protagonista.rect.y>705):
                protagonista.rect.y=695
            if(protagonista.rect.y<35):
                protagonista.rect.y=45
        if(marte9):
            if(protagonista.rect.x<30):
                protagonista.rect.x = 40
            if(protagonista.rect.y>705):
                protagonista.rect.y = 695
        if(marte10):
            if(protagonista.rect.y>705):
                protagonista.rect.y = 695
        if(marte11):
            if(protagonista.rect.x>710):
                protagonista.rect.x = 700
            if(protagonista.rect.y>705):
                protagonista.rect.y = 695
        if(primeraParaiso):
            if(protagonista.rect.x>750):
                protagonista.rect.x = 740
            if(protagonista.rect.x<5):
                protagonista.rect.x = 15
            if(protagonista.rect.y>750):
                protagonista.rect.y = 740
        if(segundaParaiso):
            if(protagonista.rect.x>750):
                protagonista.rect.x = 740
            if(protagonista.rect.x<5):
                protagonista.rect.x = 15
            if(protagonista.rect.y<5):
                protagonista.rect.y = 15

    def colisionesConMeteorito(protagonista,meteorito1,meteorito2,meteorito4,meteorito3,arreglos,espacio1,espacio2,espacio3):
        if(espacio1==True):
            if(protagonista.rect.y>meteorito1.rect.y-20 and protagonista.rect.y<(meteorito1.rect.y+60) and protagonista.rect.x>510 and protagonista.rect.x<630):
                arreglos-=15
                meteorito1.rect.y = -40
            if(protagonista.rect.y>meteorito2.rect.y-20 and protagonista.rect.y<(meteorito2.rect.y+105) and protagonista.rect.x>295 and protagonista.rect.x<405):
                arreglos-=25
                meteorito2.rect.y = -40
            if(protagonista.rect.y>meteorito3.rect.y-20 and protagonista.rect.y<(meteorito3.rect.y+85) and protagonista.rect.x>80 and protagonista.rect.x<240):
                arreglos-=40
                meteorito3.rect.y = -40
        if(espacio2==True):
            if(protagonista.rect.y>meteorito4.rect.y-20 and protagonista.rect.y<(meteorito4.rect.y+280) and protagonista.rect.x>200 and protagonista.rect.x<500):
                arreglos-=60
                meteorito4.rect.y = -100
        return arreglos
    #Funcion para las colisiones de la nave con los bordes
    def colisionesNave(protagonista,espacio1,espacio3):
        if(espacio1==True):
            if(protagonista.rect.x>736):
                protagonista.rect.x = 726
        if(espacio3==True):
            if(protagonista.rect.x<300):
                protagonista.rect.x = 310
        if(protagonista.rect.y<0):
            protagonista.rect.y = 10    
        if(protagonista.rect.y>736):
            protagonista.rect.y = 726
    
    def colisionesUrano(protagonista,nave,urano1,urano2,urano3,urano4):
        if(urano1==True):
            if(protagonista.rect.y<25):
                protagonista.rect.y = 35
            if(protagonista.rect.y>710):
                protagonista.rect.y = 700
            if(protagonista.rect.x<25):
                protagonista.rect.x = 35
            if(protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x-40) and protagonista.rect.y>(nave.rect.y-20) and protagonista.rect.y<(nave.rect.y+237)):
                protagonista.rect.x = nave.rect.x - 60
            if(protagonista.rect.y>(nave.rect.y-50) and protagonista.rect.y<(nave.rect.y-40) and protagonista.rect.x>(nave.rect.x-20) and protagonista.rect.x<(nave.rect.x+310)):
                protagonista.rect.y = nave.rect.y - 60
            if(protagonista.rect.x>(nave.rect.x+295) and protagonista.rect.x<(nave.rect.x+300) and protagonista.rect.y>(nave.rect.y-10) and protagonista.rect.y<(nave.rect.y+227)):
                protagonista.rect.x = nave.rect.x +310
            if(protagonista.rect.y>(nave.rect.y+227) and protagonista.rect.y<(nave.rect.y+237) and protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x+310)):
                protagonista.rect.y = nave.rect.y + 247
        if(urano2==True):
            if(protagonista.rect.x>710):
                protagonista.rect.x = 700
        if(urano4==True):
            if(protagonista.rect.x>710):
                protagonista.rect.x = 700
            if(protagonista.rect.x<25):
                protagonista.rect.x = 35
            if(protagonista.rect.y>710):
                protagonista.rect.y = 700
        if(urano3==True):
            if(protagonista.rect.x>710):
                protagonista.rect.x = 700
            if(protagonista.rect.x<25):
                protagonista.rect.x = 35
            if(protagonista.rect.y<25):
                protagonista.rect.y = 35 

    def colisionesPluton(protagonista,nave,pluton1,pluton2):
        if(pluton1):
            if(protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x-40) and protagonista.rect.y>(nave.rect.y-20) and protagonista.rect.y<(nave.rect.y+237)):
                protagonista.rect.x = nave.rect.x - 60
            if(protagonista.rect.y>(nave.rect.y-50) and protagonista.rect.y<(nave.rect.y-40) and protagonista.rect.x>(nave.rect.x-20) and protagonista.rect.x<(nave.rect.x+310)):
                protagonista.rect.y = nave.rect.y - 60
            if(protagonista.rect.x>(nave.rect.x+295) and protagonista.rect.x<(nave.rect.x+300) and protagonista.rect.y>(nave.rect.y-10) and protagonista.rect.y<(nave.rect.y+227)):
                protagonista.rect.x = nave.rect.x +310
            if(protagonista.rect.y>(nave.rect.y+227) and protagonista.rect.y<(nave.rect.y+237) and protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x+310)):
                protagonista.rect.y = nave.rect.y + 247
            if(protagonista.rect.x>730):
                protagonista.rect.x=720
            if(protagonista.rect.x<10):
                protagonista.rect.x=20
            if(protagonista.rect.y>730):
                protagonista.rect.y=720
        if(pluton2):
            if(protagonista.rect.x>730):
                protagonista.rect.x=720
            if(protagonista.rect.x<10):
                protagonista.rect.x=20
            if(protagonista.rect.y>730):
                protagonista.rect.y=720
            if(protagonista.rect.y<10):
                protagonista.rect.y=20