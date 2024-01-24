import pygame
class CambioEscena:
    def __init__(self) -> None:
        pass
    def cambioEcenaNave(self,protagonista,escena1,escena2,escena3):
        if(protagonista.rect.x<10 and (protagonista.rect.y>150 and protagonista.rect.y<300) and escena2==False):
            escena1 = False
            escena2 = True
            posicion = True
            if(posicion):
                protagonista.rect.x = 690
        elif(protagonista.rect.x>690 and (protagonista.rect.y>50 and protagonista.rect.y<250) and escena1==False):
            escena2 = False
            escena1 = True
            posicion = True
            if(posicion):
                protagonista.rect.x = 60
        elif(protagonista.rect.y>770 and (protagonista.rect.x>60 and protagonista.rect.x<740) and escena3==False):
            escena1=False
            escena3=True
            posicion=True
            if(posicion):
                protagonista.rect.y = 10
        elif(protagonista.rect.y<-30 and (protagonista.rect.x>60 and protagonista.rect.x<740) and escena1==False):
            escena3=False
            escena1=True
            posicion=True
            if(posicion):
                protagonista.rect.y=740

        return escena1,escena2,escena3
    
    def cambioEscenaLuna(self,protagonista,luna1,luna2,luna3,luna4,luna5,luna6):
        if(protagonista.rect.x<0 and luna1==True):
            luna1=False
            luna2 = True
            protagonista.rect.x=700
        elif(protagonista.rect.y>790 and luna1==True):
            luna1=False
            luna4 = True
            protagonista.rect.y=30
        elif(protagonista.rect.y<-10 and luna1==True):
            luna1=False
            luna3=True
            protagonista.rect.y=780
        elif(protagonista.rect.x>730 and luna2==True):
            luna2=False
            luna1=True
            protagonista.rect.x=30
        elif(protagonista.rect.y<-10 and luna2==True):
            luna5=True
            luna2=False
            protagonista.rect.y=780
        elif(protagonista.rect.y<-10 and luna4==True):
            luna1=True
            luna4=False
            protagonista.rect.y=780
        elif(protagonista.rect.y>790 and luna3==True):
            luna1=True
            luna3=False
            protagonista.rect.y=20
        elif(protagonista.rect.x<10 and luna3==True):
            luna5=True
            luna3=False
            protagonista.rect.x=700
        elif(protagonista.rect.x>730 and luna3==True):
            luna6=True
            luna3=False
            protagonista.rect.x=30
        elif(protagonista.rect.x<10 and luna6==True):
            luna3=True
            luna6=False
            protagonista.rect.x=700
        elif(protagonista.rect.x>730 and luna5==True):
            luna3=True
            luna5=False
            protagonista.rect.x=30
        elif(protagonista.rect.y>790 and luna5==True):
            luna2=True
            luna5=False
            protagonista.rect.y=30

        return luna1,luna2,luna3,luna4,luna5,luna6 
    
    def cambioEscenaMarte(self,protagonista,marte1,marte2,marte3,marte4,marte5,marte6,marte7,marte8,marte9,marte10,marte11,paraiso,primeraParaiso,segundaParaiso):
        if(paraiso==True):
            marte4=False
        if(protagonista.rect.x>760 and marte1==True):
            marte2=True
            marte1=False
            protagonista.rect.x = 20
        if(protagonista.rect.y>790 and marte1==True):
            marte5=True
            marte1=False
            protagonista.rect.y = 20
        #Escena central
        if(protagonista.rect.x>760 and marte2==True):
            marte3=True
            marte2=False
            protagonista.rect.x = 20
        if(protagonista.rect.x<10 and marte2==True):
            marte1=True
            marte2=False
            protagonista.rect.x = 750
        if(protagonista.rect.y>790 and marte2==True):
            marte6=True
            marte2=False
            protagonista.rect.y = 20
        #Escena de la derecha
        if(protagonista.rect.x<10 and marte3==True):
            marte2=True
            marte3=False
            protagonista.rect.x = 750
        if(protagonista.rect.y>790 and marte3==True):
            marte7=True
            marte3=False
            protagonista.rect.y = 20
        if(protagonista.rect.y<-10 and marte3==True):
            marte4=True
            marte3=False
            protagonista.rect.y = 780
        #Escena especial
        if(protagonista.rect.y>790 and marte4==True):
            marte3=True
            marte4=False
            protagonista.rect.y = 20    
        #Escena centro
        if(protagonista.rect.x>760 and marte6==True):
            marte7=True
            marte6=False
            protagonista.rect.x = 20
        if(protagonista.rect.x<10 and marte6==True):
            marte5=True
            marte6=False
            protagonista.rect.x = 750
        if(protagonista.rect.y>790 and marte6==True):
            marte10=True
            marte6=False
            protagonista.rect.y = 20
        if(protagonista.rect.y<-10 and marte6==True):
            marte2=True
            marte6=False
            protagonista.rect.y = 770
        #Escena derecha
        if(protagonista.rect.x>760 and marte7==True):
            marte8=True
            marte7=False
            protagonista.rect.x = 20
        if(protagonista.rect.x<10 and marte7==True):
            marte6=True
            marte7=False
            protagonista.rect.x = 750
        if(protagonista.rect.y>790 and marte7==True):
            marte11=True
            marte7=False
            protagonista.rect.y = 20
        if(protagonista.rect.y<-10 and marte7==True):
            marte3=True
            marte7=False
            protagonista.rect.y = 780
        #Escena izquierda
        if(protagonista.rect.x>760 and marte5==True):
            marte6=True
            marte5=False
            protagonista.rect.x = 20
        if(protagonista.rect.y>790 and marte5==True):
            marte9=True
            marte5=False
            protagonista.rect.y = 20
        if(protagonista.rect.y<-10 and marte5==True):
            marte1=True
            marte5=False
            protagonista.rect.y = 780
        #Escena especial
        if(protagonista.rect.x<10 and marte8==True):
            marte7=True
            marte8=False
            protagonista.rect.x = 750
        if(protagonista.rect.x>760 and marte9==True):
            marte10=True
            marte9=False
            protagonista.rect.x = 20
        if(protagonista.rect.y<-10 and marte9==True):
            marte5=True
            marte9=False
            protagonista.rect.y = 780
        #Escena central
        if(protagonista.rect.x>760 and marte10==True):
            marte11=True
            marte10=False
            protagonista.rect.x = 20
        if(protagonista.rect.x<10 and marte10==True):
            marte9=True
            marte10=False
            protagonista.rect.x = 750
        if(protagonista.rect.y<-10 and marte10==True):
            marte6=True
            marte10=False
            protagonista.rect.y = 780
        #Escena de la derecha
        if(protagonista.rect.x<10 and marte11==True):
            marte10=True
            marte11=False
            protagonista.rect.x = 750
        if(protagonista.rect.y<-10 and marte11==True):
            marte7=True
            marte11=False
            protagonista.rect.y = 780
        if(protagonista.rect.y<-10 and primeraParaiso==True):
            segundaParaiso=True
            primeraParaiso=False
            protagonista.rect.y = 780
        if(protagonista.rect.y>790 and segundaParaiso==True):
            primeraParaiso=True
            segundaParaiso=False
            protagonista.rect.y = 10

        return marte1,marte2,marte3,marte4,marte5,marte6,marte7,marte8,marte9,marte10,marte11,primeraParaiso,segundaParaiso
    
    def cambioEscenaJupiter(self,protagonista,espacio1,espacio2,espacio3):
        if(protagonista.rect.x<20 and espacio1==True):
            espacio2=True
            espacio1=False
            protagonista.rect.x = 750
        if(protagonista.rect.x>760 and espacio2==True):
            espacio1=True
            espacio2=False
            protagonista.rect.x=30
        if(protagonista.rect.x<20 and espacio2==True):
            espacio3=True
            espacio2=False
            protagonista.rect.x=750
        if(protagonista.rect.x>760 and espacio3==True):
            espacio2=True
            espacio3=False
            protagonista.rect.x=30
        return espacio1,espacio2,espacio3
    
    def cambioEscenaUrano(self,protagonista,urano1,urano2,urano3,urano4):
        #Cambios escena central
        if(protagonista.rect.x>760 and urano1==True):
            urano2=True
            urano1=False
            protagonista.rect.x=20
        #Cambios escena cruce
        if(protagonista.rect.x<20 and urano2==True):
            urano1=True
            urano2=False
            protagonista.rect.x = 750
        if(protagonista.rect.y>760 and urano2==True):
            urano4=True
            urano2=False
            protagonista.rect.y = 20
        if(protagonista.rect.y<10 and urano2==True):
            urano3=True
            urano2=False
            protagonista.rect.y = 750
        #Cambios escena arriba
        if(protagonista.rect.y>760 and urano3==True):
            urano2 = True
            urano3 = False
            protagonista.rect.y = 20
        #Cambios escena abajo
        if(protagonista.rect.y<10 and urano4==True):
            urano2 = True
            urano4=False
            protagonista.rect.y = 750
        return urano1,urano2,urano3,urano4
    
    def cambioEscenaPluton(self,protagonista,pluton1,pluton2):
        if(protagonista.rect.y<-10 and pluton1==True):
            pluton2 = True
            pluton1 = False
            protagonista.rect.y = 760
        return pluton1,pluton2