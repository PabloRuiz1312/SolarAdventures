import pygame
class Texto:

    def __init__(self):
        pass
    #Funcion para crear el HUD en el juego
    def mensajesHUD(self,screen,gasolina,arreglos,vida,balas,bidones,piezas):
        blanco = pygame.Color(255,255,255)
        fraseInteractuar = pygame.font.Font(None,50)
        fraseIteraccion = pygame.font.Font(None,35)
        colocarMision = "MISIONES"
        transmitirMision = fraseInteractuar.render(colocarMision,1,blanco)
        screen.blit(transmitirMision,(900,580))
        colocarInteractuar = "MENSAJES"
        transmitirInteractuar = fraseInteractuar.render(colocarInteractuar,1,blanco)
        screen.blit(transmitirInteractuar,(900,700))
        colocarEstadoNave = "ESTADO NAVE"
        transmitirEstadoNave = fraseInteractuar.render(colocarEstadoNave,1,blanco)
        screen.blit(transmitirEstadoNave,(870,50))
        colocarGasolina = "GASOLINA "+str(int(gasolina))+"%"
        transmitirGasolina = fraseIteraccion.render(colocarGasolina,1,blanco)
        screen.blit(transmitirGasolina,(900,90))
        colocarArregloNave = "COMPOSICION NAVE "+str(arreglos)+"%"
        transmitirArregloNave = fraseIteraccion.render(colocarArregloNave,1,blanco)
        screen.blit(transmitirArregloNave,(850,150))
        colocarVida = "VIDA "+str(int(vida))+"%"
        transmitirVida = fraseIteraccion.render(colocarVida,1,blanco)
        screen.blit(transmitirVida,(930,300))
        colocarBalas = "BALAS "+str(balas)
        transmitirBalas = fraseIteraccion.render(colocarBalas,1,blanco)
        screen.blit(transmitirBalas,(930,370))
        colocarBidones = "BIDONES "+str(bidones)
        transmitirBidones = fraseIteraccion.render(colocarBidones,1,blanco)
        screen.blit(transmitirBidones,(930,440))
        colocarPiezas = "PIEZAS "+str(piezas)
        transmitirPiezas = fraseIteraccion.render(colocarPiezas,1,blanco)
        screen.blit(transmitirPiezas,(930,510))
        colocarEstadoPersonaje  =  "ESTADO PERSONAJE"
        transmitirEstadoPersonaje = fraseInteractuar.render(colocarEstadoPersonaje,1,blanco)
        screen.blit(transmitirEstadoPersonaje,(815,250))
    #Funcion para crear las iteracciones en la nave
    def mensajesIteraccionesNave(self,screen,protagonista,escena1,escena2,escena3):
        blanco = pygame.Color(255,255,255)
        fraseIteraccion = pygame.font.Font(None,35)
        if(protagonista.rect.x>540 and protagonista.rect.x<590 and protagonista.rect.y>100 and protagonista.rect.y<360 and escena3==True):
            Interaccion = "Pulse e para recoger balas"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760)) 
        if(protagonista.rect.x>60 and protagonista.rect.x<190 and protagonista.rect.y>500 and protagonista.rect.y<570 and escena3==True):
            Interaccion = "Pulse e para rellenar gasolina"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760)) 
        if(protagonista.rect.x>500 and protagonista.rect.x<760 and protagonista.rect.y>540 and escena3==True):
            Interaccion = "Pulse e para arreglar la nave"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(protagonista.rect.x>660  and protagonista.rect.y>120 and protagonista.rect.y<210 and escena1==True):
            Interaccion = "Pulse e para curarse"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(protagonista.rect.x>310 and protagonista.rect.x<410 and protagonista.rect.y>590 and escena2==True):
            Interaccion = "Pulse e para pilotar la nave"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
    def mensajesMapa(self,screen,flecha,primeraMision,segundaMision,terceraMision,cuartaMision,quintaMision):
        blanco = pygame.Color(255,255,255)
        fraseIteraccion = pygame.font.Font(None,35)
        mensajeEscape = "PULSA ESC PARA SALIR DEL MAPA"
        transmitirEscape = fraseIteraccion.render(mensajeEscape,1,blanco)
        screen.blit(transmitirEscape,(10,10))
        mensajeEnter = "PULSA ENTER PARA VIAJAR A UN PLANETA"
        transmitirEnter = fraseIteraccion.render(mensajeEnter,1,blanco)
        screen.blit(transmitirEnter,(10,40))
        mensajeFDerecha = "PULSA --> PARA MOVERTE A LA DERECHA"
        transmitirFDerecha = fraseIteraccion.render(mensajeFDerecha,1,blanco)
        screen.blit(transmitirFDerecha,(10,70))
        mensajeFIzquierda = "PULSA <-- PARA MOVERTE A LA IZQUIERDA"
        transmitirFIzquierda = fraseIteraccion.render(mensajeFIzquierda,1,blanco)
        screen.blit(transmitirFIzquierda,(10,100))
        if(flecha.rect.x>500 and flecha.rect.x<515 and primeraMision==True):
            Interaccion = "Pulse enter para ir a la luna"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(flecha.rect.x>450 and flecha.rect.x<480 and segundaMision==True):
            Interaccion = "Pulse enter para ir a marte"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(flecha.rect.x>290 and flecha.rect.x<350 and terceraMision==True):
            Interaccion = "Pulse enter para ir a jupiter"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(flecha.rect.x>110 and flecha.rect.x<130 and cuartaMision==True):
            Interaccion = "Pulse enter para ir a urano"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(flecha.rect.x>5 and flecha.rect.x<17 and quintaMision==True):
            Interaccion = "Pulse enter para ir a pluton"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        
    def mensajesIteraccionesLuna(self,screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escena1,cogerPieza,cogerBidon,cogerPropulsor,secretoLuna):
        blanco = pygame.Color(255,255,255)
        fraseIteraccion = pygame.font.Font(None,35)
        if(protagonista.rect.y>430 and protagonista.rect.y<470 and protagonista.rect.x>530 and protagonista.rect.x<620 and luna1==True):
            Interaccion = "Pulse e para entrar a la nave"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760)) 
        if(protagonista.rect.x > 280 and protagonista.rect.x <390 and protagonista.rect.y < 110 and escena1==True and volverNave==True):
            Interaccion = "Pulse e para salir de la nave"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760)) 
        if(protagonista.rect.x>320 and protagonista.rect.x<480 and protagonista.rect.y>540 and protagonista.rect.y<665 and luna4==True and cogerPieza==False):
            Interaccion = "Pulse e para coger la pieza"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(protagonista.rect.x>445 and protagonista.rect.x<645 and protagonista.rect.y>600 and protagonista.rect.y<700 and luna3==True and cogerBidon==False):
            Interaccion = "Pulse e para coger el bidon"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(protagonista.rect.x>220 and protagonista.rect.x<520 and protagonista.rect.y>330 and protagonista.rect.y<592 and luna5==True and cogerPropulsor==False):
            Interaccion = "Pulse e para coger el propulsor"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760))
        if(protagonista.rect.x>365 and protagonista.rect.x<495 and protagonista.rect.y>230 and protagonista.rect.y<375 and luna6==True and secretoLuna==False):
            Interaccion = "???"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(975,760))

    def mensajesIteraccionesMarte(self,screen,protagonista,volverNave,escena1,escena3,marte1,marte2,marte3,marte4,marte5,marte6,marte8,marte9,marte10,marte11,cogerBidon,cogerBidon2,cogerPieza,cogerPieza2,cogerPieza3,cogerPieza4,entrarParaiso,piezas):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(volverNave==False):
            if(marte1):
                if(protagonista.rect.x>130 and protagonista.rect.x<270 and protagonista.rect.y>520 and protagonista.rect.y<680 and cogerBidon==False):
                    Interaccion = "Pulse e para coger el bidon"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
                if(protagonista.rect.x>65 and protagonista.rect.x<145 and protagonista.rect.y>60 and protagonista.rect.y<130):
                    Interaccion = "Pulse e para recuperar vida"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
            if(marte2):
                if(protagonista.rect.x>530 and protagonista.rect.x<610 and protagonista.rect.y>100 and protagonista.rect.y<190):
                    Interaccion = "???"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(975,760))
            if(marte3):
                if(protagonista.rect.x>505 and protagonista.rect.x<590 and protagonista.rect.y>465 and protagonista.rect.y<540 and cogerPieza==False):
                    Interaccion = "Pulse e para coger la pieza"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
            if(marte4):
                if(entrarParaiso==True):
                    if(protagonista.rect.x>325 and protagonista.rect.x<385 and protagonista.rect.y>235 and protagonista.rect.y<300 and entrarParaiso==True):
                        Interaccion = "???"
                        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                        screen.blit(Transmitir,(975,760))
                    if(protagonista.rect.x>240 and protagonista.rect.x<510 and protagonista.rect.y>10 and protagonista.rect.y<250 and entrarParaiso==True):
                        Interaccion = "Pulse e para entrar a la cueva"
                        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                        screen.blit(Transmitir,(830,760))
                else:
                    Interaccion = "No deberias de estar aqui"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
            if(marte5):
                if(protagonista.rect.x>65 and protagonista.rect.x<155 and protagonista.rect.y>535 and protagonista.rect.y<635  and cogerPieza2==False):
                    Interaccion = "Pulse e para coger la pieza"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
            if(marte6):
                if(protagonista.rect.x>35 and protagonista.rect.x<115 and protagonista.rect.y>380 and protagonista.rect.y<460):
                    Interaccion = "Pulse e para recuperar vida"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
                if(protagonista.rect.x>475 and protagonista.rect.x<540 and protagonista.rect.y>550 and protagonista.rect.y<580):
                    Interaccion = "Pulse e para entrar a la nave"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
            if(marte8):
                if(protagonista.rect.x>95 and protagonista.rect.x<205 and protagonista.rect.y>575 and protagonista.rect.y<665 and cogerPieza3==False):
                    Interaccion = "Pulse e para coger la pieza"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
                if(protagonista.rect.x>665 and protagonista.rect.x<720 and protagonista.rect.y>305 and protagonista.rect.y<365):
                    Interaccion = "Pulse e para recuperar vida"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
            if(marte9):
                if(protagonista.rect.x>80 and protagonista.rect.x<180 and protagonista.rect.y>605 and protagonista.rect.y<665 ):
                    Interaccion = "Pulse e para recuperar vida"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
            if(marte10):
                if(protagonista.rect.x>550 and protagonista.rect.x<640 and protagonista.rect.y>355 and protagonista.rect.y<445 and cogerPieza4==False):
                    Interaccion = "Pulse e para coger la pieza"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
            if(marte11):
                if(protagonista.rect.x>310 and protagonista.rect.x<460 and protagonista.rect.y>310 and protagonista.rect.y<460 and cogerBidon2==False):
                    Interaccion = "Pulse e para coger el bidon"
                    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                    screen.blit(Transmitir,(830,760))
        if(volverNave and escena1):
            if(protagonista.rect.x > 280 and protagonista.rect.x <390 and protagonista.rect.y < 110 and escena1==True and volverNave==True):
                Interaccion = "Pulse e para salir de la nave"
                transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(transmitir,(830,760)) 
        if(volverNave and escena3 and piezas>=4):
            if(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540):
                Interaccion = "Pulse e para crear el generador"
                transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(transmitir,(820,760))

    def mensajesParaiso(self,screen,protagonista,primeraParaiso,segundaParaiso,saquear,soporteVital):
        blanco = pygame.Color(255,255,255)
        fraseIteraccion = pygame.font.Font(None,35)
        if(primeraParaiso):
            if(protagonista.rect.x>460 and protagonista.rect.x<540 and protagonista.rect.y>130 and protagonista.rect.y<210):
                Interaccion = "???"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))
            if(protagonista.rect.x>290 and protagonista.rect.x<475 and protagonista.rect.y>580 and protagonista.rect.y<750 and primeraParaiso==True):
                Interaccion = "Pulse e para salir del paraiso"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))    
        if(segundaParaiso):
            if(protagonista.rect.x>240 and protagonista.rect.x<320 and protagonista.rect.y>50 and protagonista.rect.y<140 and segundaParaiso==True):
                Interaccion = "???"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))
            if(protagonista.rect.x>230 and protagonista.rect.x<480 and protagonista.rect.y>0 and protagonista.rect.y<120 and segundaParaiso==True and saquear==True and soporteVital==False):
                Interaccion = "Pulse e para registrar el cadaver"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))
            if(protagonista.rect.x>90 and protagonista.rect.x<190 and protagonista.rect.y>250 and protagonista.rect.y<315 and segundaParaiso==True):
                Interaccion = "Pulse e para recuperar vida"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))

    def mensajeCristal(self,screen,protagonista,cristal,distribuidor,escena3):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(cristal==True and escena3==True):
            if(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540):
                Interaccion = "Pulse e para crear el distribuidor"
                transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(transmitir,(815,760))

    def cogerHidrogeno(self,screen,protagonista,pintarHidrogeno,cogerHidrogeno):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(protagonista.rect.x>(pintarHidrogeno.rect.x-70) and protagonista.rect.x<(pintarHidrogeno.rect.x+70) and protagonista.rect.y>(pintarHidrogeno.rect.y-70) and protagonista.rect.y<(pintarHidrogeno.rect.y+70) and cogerHidrogeno==True):
            Interaccion = "Pulse e para coger hidrogeno"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(815,760))

    def mensajesUrano(self,screen,protagonista,urano1,urano2,urano3,urano4,cogerPieza,cogerBidon,volverNave,escenaNave1):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(urano1):
            if(protagonista.rect.x>120 and protagonista.rect.x<190  and protagonista.rect.y<285 and volverNave==False):
                Interaccion = "Pulse e para entrar a la nave"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))
            if(protagonista.rect.x>55 and protagonista.rect.x<140 and protagonista.rect.y>520 and protagonista.rect.y<595):
                Interaccion = "Pulse e para entrar en calor"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))    
        if(urano2):
            if(protagonista.rect.x>540 and protagonista.rect.x<625 and protagonista.rect.y>160 and protagonista.rect.y<230  and cogerPieza==False):
                Interaccion = "Pulse e para coger la pieza"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))
        if(urano3):
            if(protagonista.rect.x>325 and protagonista.rect.x<430 and protagonista.rect.y>115 and protagonista.rect.y<195  and cogerBidon==False):
                Interaccion = "Pulse e para coger el bidon"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760))
        if(urano4):
            if(protagonista.rect.x>315 and protagonista.rect.x<430 and protagonista.rect.y>480 and protagonista.rect.y<570):
                Interaccion = "Pulse e para entrar en calor"
                Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(Transmitir,(830,760)) 
        if(volverNave==True and escenaNave1==True):
            if(protagonista.rect.x > 280 and protagonista.rect.x <390 and protagonista.rect.y < 110 and escenaNave1==True and volverNave==True):
                Interaccion = "Pulse e para salir de la nave"
                transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(transmitir,(830,760)) 
    
    def mensajeTraje(self,screen,protagonista,hidrogeno,trajeAP,escenaNave3):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(hidrogeno>=5 and escenaNave3==True):
            if(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540):
                Interaccion = "Pulse e para crear el traje"
                transmitir = fraseIteraccion.render(Interaccion,1,blanco)
                screen.blit(transmitir,(815,760))
    def mensajeMedicamento(self,screen,protagonista,vidaJefe,vida):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(protagonista.rect.x>350 and protagonista.rect.x<480 and protagonista.rect.y>350 and protagonista.rect.y<480 and vida<50):
            Interaccion = "Pulsa e para abastecerte"
            Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(Transmitir,(830,760))
        if(vidaJefe>0):
            Interaccion = "Vida jefe "+str(vidaJefe)
            Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(Transmitir,(855,640))

    def mensajesNavePluton(self,screen,protagonista,volverNave,escenaNave1,pluton1):
        fraseIteraccion = pygame.font.Font(None,35)
        blanco = pygame.Color(255,255,255)
        if(protagonista.rect.y>635 and protagonista.rect.y<670 and protagonista.rect.x>335 and protagonista.rect.x<415 and pluton1==True):
            Interaccion = "Pulse e para entrar a la nave"
            Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(Transmitir,(830,760))
        if(protagonista.rect.x > 280 and protagonista.rect.x <390 and protagonista.rect.y < 110 and escenaNave1==True and volverNave==True):
            Interaccion = "Pulse e para salir de la nave"
            transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(transmitir,(830,760)) 

    def explosion(self,screen,vidaJefe,contadorMensaje):
        fraseIteraccion = pygame.font.Font(None,125)
        rojo = pygame.Color(255,150,0)
        if(vidaJefe<=60 and vidaJefe>30 and contadorMensaje!=200):
            mensaje="EXPLOSIONES"
            transmitir = fraseIteraccion.render(mensaje,1,rojo)
            screen.blit(transmitir,(90,480))
            contadorMensaje+=1
        return contadorMensaje
    def hemorragia(self,screen,vidaJefe,contadorMensaje):
        fraseIteraccion = pygame.font.Font(None,125)
        rojo = pygame.Color(255,0,0)
        if(vidaJefe<=30 and contadorMensaje!=400):
            mensaje="HEMORRAGIA"
            transmitir = fraseIteraccion.render(mensaje,1,rojo)
            screen.blit(transmitir,(100,480))
            contadorMensaje+=1
        return contadorMensaje