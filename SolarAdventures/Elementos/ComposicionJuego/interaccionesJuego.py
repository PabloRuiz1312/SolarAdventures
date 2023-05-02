import pygame
import random
from mensajesJuego import Texto
class iteracciones:
    def iteraccionesNave(screen,protagonista,balas,gasolina,bidones,arreglo,piezas,vida,escena1,escena2,escena3,contadorIteraccion,mapa,distribuidor):
        teclaPulsada = pygame.key.get_pressed()
        #Balas
        if(protagonista.rect.x>540 and protagonista.rect.x<580 and protagonista.rect.y>100 and protagonista.rect.y<360 and escena3==True):
            Texto.mensajesIteraccionesNave(screen,protagonista,escena1,escena2,escena3)
            if(teclaPulsada[pygame.K_e] and contadorIteraccion==0):
                balas+=100
                contadorIteraccion+=1
                if(balas>100):
                    balas=100
            if(contadorIteraccion!=0):
                contadorIteraccion+=1
                if(contadorIteraccion==40):
                    contadorIteraccion=0
        if(protagonista.rect.x>60 and protagonista.rect.x<190 and protagonista.rect.y>500 and protagonista.rect.y<570 and escena3==True):
            Texto.mensajesIteraccionesNave(screen,protagonista,escena1,escena2,escena3)
            if(teclaPulsada[pygame.K_e] and contadorIteraccion==0 and bidones>0):                                   
                if(gasolina<100):
                    if(distribuidor==False):
                        gasolina+=33
                    if(distribuidor==True):
                        gasolina+=45
                    bidones-=1
                    if(gasolina>100):
                        gasolina = 100
                contadorIteraccion+=1
            if(contadorIteraccion!=0):
                contadorIteraccion+=1
            if(contadorIteraccion==40):
                contadorIteraccion=0
        if(protagonista.rect.x>500 and protagonista.rect.x<760 and protagonista.rect.y>540 and escena3==True):
            Texto.mensajesIteraccionesNave(screen,protagonista,escena1,escena2,escena3)
            if(teclaPulsada[pygame.K_e] and contadorIteraccion==0 and piezas>0):
                if(arreglo<100):
                    if(distribuidor==False):
                        arreglo+=10
                    if(distribuidor==True):
                        arreglo+=15
                    piezas-=1
                    if(arreglo>100):
                        arreglo=100
                contadorIteraccion+=1
            if(contadorIteraccion!=0):
                contadorIteraccion+=1
            if(contadorIteraccion==40):
                contadorIteraccion=0
        if(protagonista.rect.x>660  and protagonista.rect.y>120 and protagonista.rect.y<210 and escena1==True):
            Texto.mensajesIteraccionesNave(screen,protagonista,escena1,escena2,escena3)
            if(teclaPulsada[pygame.K_e]  and vida<100):
                vida+=100
                if(vida>100):
                    vida=100
        if(protagonista.rect.x>310 and protagonista.rect.x<410 and protagonista.rect.y>590 and escena2==True):
            Texto.mensajesIteraccionesNave(screen,protagonista,escena1,escena2,escena3)
            if(teclaPulsada[pygame.K_e]):
                mapa = True

        return balas,gasolina,bidones,arreglo,piezas,vida,escena1,escena2,escena3,contadorIteraccion,mapa

    def iteraccionesMapa(screen,flecha,infoSol,infoMercurio,infoVenus,infoTierra,infoMarte,infoJupiter,infoSaturno,infoUrano,infoNeptuno,infoPluton):
        if(flecha.rect.x>680 and flecha.rect.x<760):
            infoSol.draw(screen)
        if(flecha.rect.x>630 and flecha.rect.x<650):
            infoMercurio.draw(screen)
        if(flecha.rect.x>580 and flecha.rect.x<610):
            infoVenus.draw(screen)
        if(flecha.rect.x>530 and flecha.rect.x<560):
            infoTierra.draw(screen)
        if(flecha.rect.x>450 and flecha.rect.x<480):
            infoMarte.draw(screen)
        if(flecha.rect.x>290 and flecha.rect.x<350):
            infoJupiter.draw(screen)
        if(flecha.rect.x>200 and flecha.rect.x<260):
            infoSaturno.draw(screen)
        if(flecha.rect.x>110 and flecha.rect.x<130):
            infoUrano.draw(screen)
        if(flecha.rect.x>50 and flecha.rect.x<70):
            infoNeptuno.draw(screen)
        if(flecha.rect.x>5 and flecha.rect.x<17):
            infoPluton.draw(screen)   

    def iteraccionesLuna(screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escena1,cogerBidon,cogerPieza,cogerPropulsor,bidones,piezas,secretoLuna,mostrarInyector,inyector):
        teclaPulsada = pygame.key.get_pressed()
        if(protagonista.rect.y>430 and protagonista.rect.y<470 and protagonista.rect.x>530 and protagonista.rect.x<620 and luna1==True):
            Texto.mensajesIteraccionesLuna(screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escena1,cogerPieza,cogerBidon,cogerPropulsor,secretoLuna)
            if(teclaPulsada[pygame.K_e]):
                volverNave=True
        if(protagonista.rect.x > 280 and protagonista.rect.x <390 and protagonista.rect.y < 110):
            Texto.mensajesIteraccionesLuna(screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escena1,cogerPieza,cogerBidon,cogerPropulsor,secretoLuna)
            if(teclaPulsada[pygame.K_e]):
                volverNave=False
        if(protagonista.rect.x>320 and protagonista.rect.x<480 and protagonista.rect.y>540 and protagonista.rect.y<665 and luna4==True and cogerPieza==False):
            Texto.mensajesIteraccionesLuna(screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escena1,cogerPieza,cogerBidon,cogerPropulsor,secretoLuna)
            if(teclaPulsada[pygame.K_e]):
                cogerPieza=True
                piezas+=1
        if(protagonista.rect.x>445 and protagonista.rect.x<645 and protagonista.rect.y>600 and protagonista.rect.y<700 and luna3==True and cogerBidon==False):
            Texto.mensajesIteraccionesLuna(screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escena1,cogerPieza,cogerBidon,cogerPropulsor,secretoLuna)
            if(teclaPulsada[pygame.K_e]):
                cogerBidon=True
                bidones+=1
        if(protagonista.rect.x>220 and protagonista.rect.x<520 and protagonista.rect.y>330 and protagonista.rect.y<592 and luna5==True and cogerPropulsor==False):
            Texto.mensajesIteraccionesLuna(screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escena1,cogerPieza,cogerBidon,cogerPropulsor,secretoLuna)
            if(teclaPulsada[pygame.K_e]):
                cogerPropulsor=True
        if(protagonista.rect.x>365 and protagonista.rect.x<495 and protagonista.rect.y>230 and protagonista.rect.y<375 and luna6==True and secretoLuna==False):
            Texto.mensajesIteraccionesLuna(screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escena1,cogerPieza,cogerBidon,cogerPropulsor,secretoLuna)
            if(teclaPulsada[pygame.K_e] and secretoLuna==False):
                mostrarInyector=True
            if(mostrarInyector==True):
                inyector.draw(screen)
                if(teclaPulsada[pygame.K_RETURN]):
                    secretoLuna=True

        return volverNave,cogerPieza,piezas,cogerBidon,bidones,cogerPropulsor,secretoLuna,mostrarInyector
    
    def iteraccionesMarte(screen,protagonista,marte1,marte2,marte3,marte4,marte5,marte6,marte8,marte9,marte10,marte11,vida,bidones,piezas,cogerBidon,cogerBidon2,cogerPieza,cogerPieza2,cogerPieza3,cogerPieza4,volverNave,escena1,escena3,mostrarCarta,entrarParaiso,carta1,carta2,paraiso,primeraParaiso):
        teclaPulsada = pygame.key.get_pressed()
        if(marte1):
            
            if(protagonista.rect.x>130 and protagonista.rect.x<270 and protagonista.rect.y>520 and protagonista.rect.y<680 and cogerBidon==False):
                if(teclaPulsada[pygame.K_e]):
                    bidones+=1
                    cogerBidon=True
            if(protagonista.rect.x>65 and protagonista.rect.x<145 and protagonista.rect.y>60 and protagonista.rect.y<130):
                if(teclaPulsada[pygame.K_e] and vida<100):
                    vida+=0.35
                    
        if(marte2):
            if(protagonista.rect.x>530 and protagonista.rect.x<610 and protagonista.rect.y>100 and protagonista.rect.y<190):    
                if(teclaPulsada[pygame.K_e]):
                    mostrarCarta=True
                if(teclaPulsada[pygame.K_RETURN] and mostrarCarta==True):
                    mostrarCarta=False
                    entrarParaiso=True
                if(mostrarCarta==True):
                    carta1.draw(screen)
            else:
                mostrarCarta = False
        if(marte3):
            
            if(protagonista.rect.x>505 and protagonista.rect.x<590 and protagonista.rect.y>465 and protagonista.rect.y<540 and cogerPieza==False):
                if(teclaPulsada[pygame.K_e]):
                    piezas+=1
                    cogerPieza=True
        if(marte4 and entrarParaiso==True):
            if(protagonista.rect.x>325 and protagonista.rect.x<385 and protagonista.rect.y>235 and protagonista.rect.y<300):
                if(teclaPulsada[pygame.K_e]):
                    mostrarCarta=True
                if(teclaPulsada[pygame.K_RETURN]):
                    mostrarCarta=False
                if(mostrarCarta==True):
                    carta2.draw(screen)
            else:
                mostrarCarta = False
            if(protagonista.rect.x>240 and protagonista.rect.x<510 and protagonista.rect.y>10 and protagonista.rect.y<250 and entrarParaiso==True):
                if(teclaPulsada[pygame.K_e]):
                    paraiso=True
                    if(paraiso==True):
                        primeraParaiso=True
                        protagonista.rect.y = 520
        if(marte5):
            
            if(protagonista.rect.x>65 and protagonista.rect.x<155 and protagonista.rect.y>535 and protagonista.rect.y<635  and cogerPieza2==False):
                if(teclaPulsada[pygame.K_e]):
                    piezas+=1
                    cogerPieza2=True
        if(marte6):
            
            if(protagonista.rect.x>35 and protagonista.rect.x<115 and protagonista.rect.y>380 and protagonista.rect.y<460):
                if(teclaPulsada[pygame.K_e] and vida<100):
                    vida+=0.35
            if(protagonista.rect.x>475 and protagonista.rect.x<540 and protagonista.rect.y>550 and protagonista.rect.y<580):
                if(teclaPulsada[pygame.K_e]):
                    volverNave=True
        if(marte8):
            
            if(protagonista.rect.x>95 and protagonista.rect.x<205 and protagonista.rect.y>575 and protagonista.rect.y<665 and cogerPieza3==False):
                if(teclaPulsada[pygame.K_e]):
                    piezas+=1
                    cogerPieza3=True
            if(protagonista.rect.x>665 and protagonista.rect.x<720 and protagonista.rect.y>305 and protagonista.rect.y<365):
                if(teclaPulsada[pygame.K_e] and vida<100):
                    vida+=0.35
        if(marte9):
            
            if(protagonista.rect.x>80 and protagonista.rect.x<180 and protagonista.rect.y>605 and protagonista.rect.y<665 ):
                if(teclaPulsada[pygame.K_e] and vida<100):
                    vida+=0.35
        if(marte10):

            if(protagonista.rect.x>550 and protagonista.rect.x<640 and protagonista.rect.y>355 and protagonista.rect.y<445 and cogerPieza4==False):
                if(teclaPulsada[pygame.K_e]):
                    piezas+=1
                    cogerPieza4=True
        if(marte11):
            
            if(protagonista.rect.x>310 and protagonista.rect.x<460 and protagonista.rect.y>310 and protagonista.rect.y<460 and cogerBidon2==False):
                if(teclaPulsada[pygame.K_e]):
                    bidones+=1
                    cogerBidon2=True
        if(escena1 and volverNave):
            if(protagonista.rect.x > 280 and protagonista.rect.x <390 and protagonista.rect.y < 110 and escena1==True and volverNave==True):
                if(teclaPulsada[pygame.K_e]):
                    volverNave=False

        Texto.mensajesIteraccionesMarte(screen,protagonista,volverNave,escena1,escena3,marte1,marte2,marte3,marte4,marte5,marte6,marte8,marte9,marte10,marte11,cogerBidon,cogerBidon2,cogerPieza,cogerPieza2,cogerPieza3,cogerPieza4,entrarParaiso,piezas)
        
        return bidones,piezas,cogerBidon,cogerBidon2,cogerPieza,cogerPieza2,cogerPieza3,cogerPieza4,volverNave,vida,mostrarCarta,entrarParaiso,paraiso,primeraParaiso
    
    def iteraccionesParaiso(screen,protagonista,paraiso,primeraParaiso,segundaParaiso,mensajeSoporteVital,soporteVital,mostrarSoporte,mostrar,vida,piezas,carta3,carta4,saquear,marte4):
        teclaPulsada = pygame.key.get_pressed()
        if(primeraParaiso):
            if(protagonista.rect.x>460 and protagonista.rect.x<540 and protagonista.rect.y>130 and protagonista.rect.y<210):
                if(teclaPulsada[pygame.K_e]):
                    mostrar=True
                if(teclaPulsada[pygame.K_RETURN] and mostrar==True):
                    mostrar=False
                if(mostrar==True):
                    carta3.draw(screen)
            if(protagonista.rect.x>290 and protagonista.rect.x<475 and protagonista.rect.y>580 and protagonista.rect.y<750 and primeraParaiso==True):
                if(teclaPulsada[pygame.K_e]):
                    paraiso=False
                    primeraParaiso=False
                    marte4=True
                    protagonista.rect.y=270
                    protagonista.rect.x= 460   
        if(segundaParaiso):
            if(protagonista.rect.x>240 and protagonista.rect.x<320 and protagonista.rect.y>50 and protagonista.rect.y<140 and segundaParaiso==True):
                if(teclaPulsada[pygame.K_e]):
                    mostrar=True
                if(teclaPulsada[pygame.K_RETURN]):
                    mostrar = False
                    saquear=True
                if(mostrar==True):
                    carta4.draw(screen)
            if(protagonista.rect.x>230 and protagonista.rect.x<480 and protagonista.rect.y>0 and protagonista.rect.y<120 and segundaParaiso==True and saquear==True and soporteVital==False):
                if(teclaPulsada[pygame.K_e]):
                    mostrarSoporte=True
                if(teclaPulsada[pygame.K_RETURN] and mostrarSoporte==True):
                    mostrarSoporte = False
                    soporteVital=True
                    piezas+=2
                    saquear=False
                if(mostrarSoporte):
                    mensajeSoporteVital.draw(screen)
            if(protagonista.rect.x>90 and protagonista.rect.x<190 and protagonista.rect.y>250 and protagonista.rect.y<315 and segundaParaiso==True):
                if(teclaPulsada[pygame.K_e] and vida<100):
                    vida+=0.35
        Texto.mensajesParaiso(screen,protagonista,primeraParaiso,segundaParaiso,saquear,soporteVital)
        return paraiso,mostrarSoporte,mostrar,soporteVital,vida,piezas,saquear,marte4,primeraParaiso

    def decision(screen,protagonista,cristal,volverNave,jupiter,finJupiter,finEntrarJupiter,decision):
        teclaPulsada = pygame.key.get_pressed()
        if(protagonista.rect.x<340):
            teclaPulsada = pygame.key.get_pressed()
            decision.draw(screen)
            if(teclaPulsada[pygame.K_1] or teclaPulsada[pygame.K_KP1]):
                finJupiter = True
                finEntrarJupiter = True
                jupiter = False
            elif(teclaPulsada[pygame.K_2] or teclaPulsada[pygame.K_KP2]):
                volverNave = True
                cristal = True
            elif(teclaPulsada[pygame.K_3] or teclaPulsada[pygame.K_KP3]):
                volverNave = True

        return cristal,volverNave,jupiter,finJupiter,finEntrarJupiter
    
    def construirDistribuidor(screen,protagonista,mostrarCarta,cristal,cristalEnergia,distribuidor,distribuidorEnergia,escena3):
        teclaPulsada = pygame.key.get_pressed()
        if(cristal==True and escena3==False):
            if(mostrarCarta==True):
                cristalEnergia.draw(screen)
            if(teclaPulsada[pygame.K_RETURN]):
                mostrarCarta=False
        if(cristal==True and escena3==True and distribuidor==False):
            if(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540): 
                if(teclaPulsada[pygame.K_e]):
                    mostrarCarta=True
                if(mostrarCarta==True):
                    distribuidorEnergia.draw(screen)
                if(teclaPulsada[pygame.K_RETURN]):
                    mostrarCarta=False
                    cristal=False
                    distribuidor=True
           
        
        Texto.mensajeCristal(screen,protagonista,cristal,distribuidor,escena3)
        return mostrarCarta,cristal,distribuidor

    def mostrarHidrogeno(screen,protagonista,bolaHidrogeno,pintarHidrogeno,cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera):
        teclaPulsada = pygame.key.get_pressed()
        if(contadorHidrogeno<=0):
            pintarHidrogeno.rect.x = random.randint(100,600)
            pintarHidrogeno.rect.y = random.randint(100,600)
            contadorHidrogeno = 3000
            contadorEspera = 4000
        if(contadorEspera>=0):
            contadorEspera-=9
            cogerHidrogeno=False
        else:
           contadorHidrogeno-=9
           cogerHidrogeno=True
           bolaHidrogeno.draw(screen)
           
        if(teclaPulsada[pygame.K_e] and (protagonista.rect.x>(pintarHidrogeno.rect.x-70) and protagonista.rect.x<(pintarHidrogeno.rect.x+70) and protagonista.rect.y>(pintarHidrogeno.rect.y-70) and protagonista.rect.y<(pintarHidrogeno.rect.y+70)) and cogerHidrogeno==True):
            hidrogeno+=1
            cogerHidrogeno=False
            contadorHidrogeno=0
        Texto.cogerHidrogeno(screen,protagonista,pintarHidrogeno,cogerHidrogeno)
        return cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera
    
    def iteraccionesUrano(screen,protagonista,urano1,urano2,urano3,urano4,cogerBidon,cogerPieza,piezas,bidones,vida,volverNave,escenaNave1):
        teclaPulsada = pygame.key.get_pressed()
        if(urano1):
            if(protagonista.rect.x>120 and protagonista.rect.x<190  and protagonista.rect.y<285):
                if(teclaPulsada[pygame.K_e]):
                    volverNave=True
            if(protagonista.rect.x>55 and protagonista.rect.x<140 and protagonista.rect.y>520 and protagonista.rect.y<595):
                if(teclaPulsada[pygame.K_e] and vida<100):
                    vida+=0.45   
        if(urano2):
            if(protagonista.rect.x>540 and protagonista.rect.x<625 and protagonista.rect.y>160 and protagonista.rect.y<230  and cogerPieza==False):
                if(teclaPulsada[pygame.K_e]):
                    piezas+=1
                    cogerPieza=True   
        if(urano3):
            if(protagonista.rect.x>325 and protagonista.rect.x<430 and protagonista.rect.y>115 and protagonista.rect.y<195  and cogerBidon==False):
                if(teclaPulsada[pygame.K_e]):
                    bidones+=1
                    cogerBidon=True   
        if(urano4):
            if(protagonista.rect.x>315 and protagonista.rect.x<430 and protagonista.rect.y>480 and protagonista.rect.y<570):
                if(teclaPulsada[pygame.K_e] and vida<100):
                    vida+=0.45 
        if(volverNave and escenaNave1):
            if(protagonista.rect.x > 280 and protagonista.rect.x <390 and protagonista.rect.y < 110 and escenaNave1==True and volverNave==True):
                if(teclaPulsada[pygame.K_e]):
                    volverNave=False  
        Texto.mensajesUrano(screen,protagonista,urano1,urano2,urano3,urano4,cogerPieza,cogerBidon,volverNave,escenaNave1)
        return cogerBidon,cogerPieza,piezas,bidones,vida,volverNave,escenaNave1

    def construirTraje(screen,protagonista,trajeAP,trajeAntipresion,hidrogeno,mostrarCarta,escenaNave3):
        teclaPulsada = pygame.key.get_pressed()
        if(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540):
            if(escenaNave3==True and teclaPulsada[pygame.K_e]):
                mostrarCarta=True
            if(mostrarCarta==True):
                trajeAntipresion.draw(screen)
            if(teclaPulsada[pygame.K_RETURN] and mostrarCarta==True):
                mostrarCarta=False
                trajeAP=True
                hidrogeno-=5
        Texto.mensajeTraje(screen,protagonista,hidrogeno,trajeAP,escenaNave3)
        return mostrarCarta,trajeAP,hidrogeno
    
    def combate(screen,protagonista,antagonista,vidaJefe,dispararBala,disparo,contadorDisparo,disparoMaligno,balaOscura,pintarBalaOscura,vida,miraEspecial,explosionEspecial,pintarMira,pintarExplosion,ataqueEspecial,contadorAtaqueEspecial,contadorMira,contadorExplosion,derechaJefe,izquierdaJefe,soporteVital,balas,pintarMedicamentos,crearMedicamento):
        teclaPulsada = pygame.key.get_pressed()
        if(contadorDisparo<=0):
            if(vidaJefe<=101 and vidaJefe>=60):
                if(antagonista.rect.x<10):
                    antagonista.rect.x=11
                    derechaJefe=1
                    izquierdaJefe=0
                elif(antagonista.rect.x>667):
                    antagonista.rect.x=666
                    izquierdaJefe=1
                    derechaJefe=0
                elif(antagonista.rect.x>protagonista.rect.x-56 and antagonista.rect.x<protagonista.rect.x+56):
                    izquierdaJefe=0
                    derechaJefe=0
                    contadorDisparo=1600
            if(vidaJefe<60 and vidaJefe>=30):
                if(antagonista.rect.x<10):
                    antagonista.rect.x=11
                    derechaJefe=1
                    izquierdaJefe=0
                elif(antagonista.rect.x>667):
                    antagonista.rect.x=666
                    izquierdaJefe=1
                    derechaJefe=0
                elif(antagonista.rect.x>protagonista.rect.x-56 and antagonista.rect.x<protagonista.rect.x+56):
                    izquierdaJefe=0
                    derechaJefe=0
                    contadorDisparo=1100
            if(vidaJefe>=0 and vidaJefe<30):
                if(antagonista.rect.x<10):
                    antagonista.rect.x=11
                    derechaJefe=1
                    izquierdaJefe=0
                elif(antagonista.rect.x>667):
                    antagonista.rect.x=666
                    izquierdaJefe=1
                    derechaJefe=0
                elif(antagonista.rect.x>protagonista.rect.x-56 and antagonista.rect.x<protagonista.rect.x+56):
                    izquierdaJefe=0
                    derechaJefe=0
                    contadorDisparo=1050
                
                
        else:
            contadorDisparo-=9
            if(contadorDisparo>1000 and contadorDisparo<1200 and disparoMaligno==False):
                    disparoMaligno=True
                    pintarBalaOscura.rect.x=protagonista.rect.x+20
                    pintarBalaOscura.rect.y=antagonista.rect.y
            if(contadorDisparo<=0):
                numero = random.randint(1,2)
                if(numero==1):
                    derechaJefe=1
                    izquierdaJefe=0
                else:
                    izquierdaJefe=1
                    derechaJefe=0
                
                
        if(disparoMaligno==True):
            balaOscura.draw(screen)
            if(vidaJefe<30):
                pintarBalaOscura.rect.y+=45
            else:
                pintarBalaOscura.rect.y+=35
            if(pintarBalaOscura.rect.y>790):
                disparoMaligno=False
                pintarBalaOscura.rect.y = 1000
        if(dispararBala.rect.y>(antagonista.rect.y) and dispararBala.rect.y<(antagonista.rect.y+145) and dispararBala.rect.x>(antagonista.rect.x-10) and dispararBala.rect.x<(antagonista.rect.x+143)):
            disparo=False
            vidaJefe-=1
            dispararBala.rect.y = -50
        if(pintarBalaOscura.rect.y>(protagonista.rect.y) and pintarBalaOscura.rect.y<(protagonista.rect.y+56) and pintarBalaOscura.rect.x>(protagonista.rect.x-20) and pintarBalaOscura.rect.x<(protagonista.rect.x+40)):
            if(soporteVital):
                vida-=8
            else:
                vida-=15
            if(vidaJefe<25):
                vidaJefe+=5
            pintarBalaOscura.rect.y = 1000
        if(vidaJefe<=60 and vidaJefe>30):
            
            if(contadorAtaqueEspecial<=0):
                ataqueEspecial=True
            else:
                contadorAtaqueEspecial-=9
            if(ataqueEspecial==True):
                contadorMira=3000
                contadorExplosion=1500
                ataqueEspecial=False
                contadorAtaqueEspecial=15000
            if(contadorMira>=0):
                pintarMira.rect.x=protagonista.rect.x+10
                pintarMira.rect.y = protagonista.rect.y+10
                miraEspecial.draw(screen)
                contadorMira-=9
            if(contadorMira<=200):
                contadorExplosion-=9
                if(contadorExplosion>=0):
                    miraEspecial.draw(screen)
                if(contadorExplosion>1 and contadorExplosion<600):
                    pintarExplosion.rect.x = pintarMira.rect.x-30
                    pintarExplosion.rect.y = pintarMira.rect.y-15
                    explosionEspecial.draw(screen)
                    if(protagonista.rect.x>(pintarExplosion.rect.x-60) and protagonista.rect.x<(pintarExplosion.rect.x+150) and protagonista.rect.y>(pintarExplosion.rect.y-60) and protagonista.rect.y<(pintarExplosion.rect.y+91)):
                        vida-=50
               
        if(vidaJefe<=30):
            if(soporteVital):
                vida-=0.02
            else:
                vida-=0.06
            if(contadorAtaqueEspecial<=0):
                ataqueEspecial=True
            else:
                contadorAtaqueEspecial-=10
            if(ataqueEspecial==True):
                contadorMira=2500
                contadorExplosion=1250
                ataqueEspecial=False
                contadorAtaqueEspecial=5000
            if(contadorMira>=0):
                pintarMira.rect.x=protagonista.rect.x+10
                pintarMira.rect.y = protagonista.rect.y+10
                miraEspecial.draw(screen)
                contadorMira-=9
            if(contadorMira<=200):
                contadorExplosion-=9
                if(contadorExplosion>=0):
                    miraEspecial.draw(screen)
                if(contadorExplosion>1 and contadorExplosion<600):
                    pintarExplosion.rect.x = pintarMira.rect.x-30
                    pintarExplosion.rect.y = pintarMira.rect.y-15
                    explosionEspecial.draw(screen)
                    if(protagonista.rect.x>(pintarExplosion.rect.x-60) and protagonista.rect.x<(pintarExplosion.rect.x+150) and protagonista.rect.y>(pintarExplosion.rect.y-60) and protagonista.rect.y<(pintarExplosion.rect.y+91)):
                        vida-=50
        
        if(vida<50):
            pintarMedicamentos.rect.x = 400
            pintarMedicamentos.rect.y = 400
            crearMedicamento.draw(screen)
            if(protagonista.rect.x>350 and protagonista.rect.x<480 and protagonista.rect.y>350 and protagonista.rect.y<480):
                if(teclaPulsada[pygame.K_e]):
                    vida+=40
                    balas+=30
                    if(balas>100):
                        balas=100
        Texto.mensajeMedicamento(screen,protagonista,vidaJefe,vida)
                
        return contadorDisparo,disparoMaligno,vidaJefe,disparo,vida,ataqueEspecial,contadorAtaqueEspecial,contadorMira,contadorExplosion,derechaJefe,izquierdaJefe,balas

    def movimientoJefe(antagonista,derechaJefe,izquierdaJefe,vidaJefe):
        if(vidaJefe<101 and vidaJefe>=60 and derechaJefe==1):
            antagonista.rect.x+=2
        if(vidaJefe<60 and vidaJefe>=30 and derechaJefe==1):
            antagonista.rect.x+=3
        if(vidaJefe<30 and vidaJefe>0 and derechaJefe==1):
            antagonista.rect.x+=4
        if(vidaJefe<101 and vidaJefe>=60 and izquierdaJefe==1):
            antagonista.rect.x-=2
        if(vidaJefe<60 and vidaJefe>=30 and izquierdaJefe==1):
            antagonista.rect.x-=3
        if(vidaJefe<30 and vidaJefe>0 and izquierdaJefe==1):
            antagonista.rect.x-=4

    def entrarNavePluton(screen,protagonista,pluton1,volverNave,escenaNave1):
        teclaPulsada = pygame.key.get_pressed()
        if(protagonista.rect.y>635 and protagonista.rect.y<670 and protagonista.rect.x>335 and protagonista.rect.x<415 and pluton1==True and volverNave==False):
            if(teclaPulsada[pygame.K_e]):
                protagonista.rect.y = 700
                volverNave=True
        if(protagonista.rect.x > 280 and protagonista.rect.x <390 and protagonista.rect.y < 110 and escenaNave1==True and volverNave==True):
            if(teclaPulsada[pygame.K_e]):
                protagonista.rect.y = 120
                volverNave=False
        Texto.mensajesNavePluton(screen,protagonista,volverNave,escenaNave1,pluton1)
        return volverNave