import pygame
class misionesTexto:

    def misionInicial(screen,primeraMision):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(primeraMision==False):
            mision = "Ve a la sala de mandos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(865,640))
        if(primeraMision==True):
            mision = "Ve a la luna"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(865,640))

    def misionLuna(screen,segundaMision,mapa,volverNave):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(segundaMision==False and volverNave==False):
            mision = "Coge el propulsor de luz"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        elif(segundaMision==False and volverNave==True):
            mision = "Sal de la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(865,640))
        elif(segundaMision==True and volverNave==False):
            mision = "Vuelve a la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(865,640))
        elif(segundaMision==True and volverNave==True and mapa==False):
            mision = "Ve a la sala de mandos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(865,640))
        elif(segundaMision==True and volverNave==True and mapa==True):
            mision = "Ve a marte"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(885,640))
    
    def misionMarte(screen,terceraMision,piezas,volverNave,mapa,entrarParaiso,soporteVital,paraiso,escena3):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(terceraMision==False and piezas<4 and volverNave==False):
            mision = "Reune "+str(4-piezas)+" piezas"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==False and piezas<4 and volverNave==True):
            mision = "Sal de la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==False and piezas>=4 and volverNave==False and entrarParaiso==False):
            mision = "Vuelve a la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==False and piezas>=4 and volverNave==False and soporteVital==True):
            mision = "Vuelve a la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==True and volverNave==False):
            mision = "Vuelve a la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==False and piezas>=4 and volverNave==False and entrarParaiso==True and paraiso==False and soporteVital==False):
            mision = "Vuelve a la nave o ve al paraiso"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(825,640))
        if(terceraMision==False and volverNave==False and paraiso==True and soporteVital==False and piezas>=4):
            mision = "Desvela secretos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==False and volverNave==True and escena3==False and piezas>=4):
            mision = "Ve a la sala de recursos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==False and volverNave==True and escena3==True and piezas>=4):
            mision = "Construye el generador"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==True and volverNave==True and mapa==False):
            mision = "Ve a la sala de mandos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(terceraMision==True and mapa==True):
            mision = "Ve a jupiter"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        
    def misionJupiter(screen,protagonista,mapa,cuartaMision,volverNave,espacio3,cristal,distribuidor,escenaNave3):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(espacio3==False and volverNave==False):
            mision = "Avanza en el espacio"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(volverNave==True and cristal==True and escenaNave3==False):
            mision = "Ve a la sala de recursos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640)) 
        if(volverNave==True and cristal==True and escenaNave3==True and distribuidor==False):
            mision = "Construye el distribuidor"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640)) 
        if(volverNave==True and cristal==False and mapa==False and distribuidor==True):
            mision = "Ve a la sala de mandos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640)) 
        if(volverNave==True and cristal==False and mapa==False and distribuidor==False):
            mision = "Ve a la sala de mandos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640)) 
        if(cuartaMision==True and mapa==True):
            mision = "Ve a Urano"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640)) 
        if(espacio3==True and protagonista.rect.x>341 and volverNave==False):
            mision = "Acercate a jupiter"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        elif(espacio3==True and protagonista.rect.x<340 and volverNave==False):
            mision = "Toma una decision"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))

    def misionUrano(screen,quintaMision,mapa,hidrogeno,trajeAP,volverNave,escenaNave3):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(hidrogeno<5 and volverNave==False and quintaMision==False):
            mision = "Reune "+str(5-hidrogeno)+" de hidrogeno"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(hidrogeno<5 and volverNave==True and quintaMision==False):
            mision = "Sal de la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(hidrogeno>=5 and volverNave==False and quintaMision==False):
            mision = "Vuelve a la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(volverNave==True and quintaMision==False and escenaNave3==False and trajeAP==False and hidrogeno>=5):
            mision = "Ve a la sala de recursos "
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(volverNave==True and quintaMision==False and escenaNave3==True and trajeAP==False and hidrogeno>=5):
            mision = "Construye el traje antipresion"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(825,640))
        if(volverNave==True and quintaMision==True and mapa==False and trajeAP==True):
            mision = "Ve a la sala de mandos"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
        if(volverNave==True and quintaMision==True and mapa==True ):
            mision = "Ve a pluton"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(855,640))
