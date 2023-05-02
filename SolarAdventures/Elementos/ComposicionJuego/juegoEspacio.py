import pygame

import random

import time
#Funcion que determina la historia
def HISTORIA():
    
    tiempo = 2000
    while(tiempo>0):
        tiempo-=100
        pygame.display.flip()
    tiempo = 8000
    while(tiempo>0):
        tiempo-=100
        comienzo = "AÑO 2075"
        transmitir = historia.render(comienzo,1,blanco)
        screen.blit(transmitir,(355,280))
        pygame.display.flip()
    screen.fill(negro)
    tiempo = 3000
    while(tiempo>0):
        tiempo-=100
        pygame.display.flip()
    tiempo = 20000
    while(tiempo>0):
        tiempo-=100
        comienzo = "EL CAMBIO CLIMATICO DESATÓ EL CAOS EN LA HUMANIDAD"
        transmitir = frases.render(comienzo,1,blanco)
        screen.blit(transmitir,(100,200))
        mitad = "FALTABAN RECURSOS Y LOS PAÍSES RICOS SE PELEABAN POR ELLOS"
        transmitir2 = frases.render(mitad,1,blanco)
        screen.blit(transmitir2,(20,250))
        final = "LAS TEMPERATURAS ERAN INFERNALES O MUY GÉLIDAS"
        transmitir3 = frases.render(final,1,blanco)
        screen.blit(transmitir3,(110,300))
        acabar = "ESTABAMOS DESTINADOS A DESAPARECER POR COMPLETO"
        transmitir4 = frases.render(acabar,1,blanco)
        screen.blit(transmitir4,(100,350))
        pygame.display.flip()
    screen.fill(negro)
    tiempo = 3000
    while(tiempo>0):
        tiempo-=100
        pygame.display.flip()
    tiempo = 20000
    while(tiempo>0):
        tiempo-=100
        comienzo = "LA ESPERANZA ESTABA PERDIDA PERO HUBO GENTE QUE NO SE RINDIO"
        transmitir = fraseLarga.render(comienzo,1,blanco)
        screen.blit(transmitir,(80,200))
        mitad = "LA NASA CONSTRUYO UNA NAVE ESPACIAL CAPAZ DE IR A LA VELOCIDAD DE LA LUZ"
        transmitir2 = fraseLarga.render(mitad,1,blanco)
        screen.blit(transmitir2,(10,250))
        pygame.display.flip()
    tiempo = 3000
    screen.fill(negro)
    while(tiempo>0):
        tiempo-=100
        pygame.display.flip()
    
    tiempo = 10000
    while(tiempo>0):
        tiempo-=100
        comienzo = "TE NECESITAMOS MÁS QUE NUNCA"
        transmitir = historia.render(comienzo,1,blanco)
        screen.blit(transmitir,(135,280))
        pygame.display.flip()
#Funcion para crear las estadisticas 
def stats(x,y,ancho):
    stats = pygame.sprite.Sprite()

    stats.image = pygame.Surface([ancho,20])
    stats.rect = stats.image.get_rect()

    stats.rect.x = x
    stats.rect.y = y

    return stats
#Funcion  para darla forma, color y posicionar las estadisticas
def colocarStats(spritesJuego,gasolina,arreglo,vida,balas,bidones,piezas):
    estadisticas = pygame.sprite.Group()

    estadisticas_1 = stats(900,120,gasolina*2)
    estadisticas_1.image.fill(naranja)

    estadisticas.add(estadisticas_1)
    spritesJuego.add(estadisticas_1)

    estadisticas_2 = stats(900,180,arreglo*2)
    estadisticas_2.image.fill(blanco)

    estadisticas.add(estadisticas_2)
    spritesJuego.add(estadisticas_2)

    estadisticas_3 = stats(900,330,vida*2)
    estadisticas_3.image.fill(rojo)

    estadisticas.add(estadisticas_3)
    spritesJuego.add(estadisticas_3)

    estadisticas_4 = stats(900,400,balas*2)
    estadisticas_4.image.fill(dorado)

    estadisticas.add(estadisticas_4)
    spritesJuego.add(estadisticas_4)

    estadisticas_5 = stats(900,470,bidones*66)
    estadisticas_5.image.fill(bidonGasofa)

    estadisticas.add(estadisticas_5)
    spritesJuego.add(estadisticas_5)

    estadisticas_6 = stats(900,540,piezas*20)
    estadisticas_6.image.fill(gris)

    estadisticas.add(estadisticas_6)
    spritesJuego.add(estadisticas_6)

    return estadisticas  
#Funcion para crear la escena central de la nave  
def escenaNave1(spritesJuego):
    InteriorNave = pygame.sprite.Sprite()

    InteriorNave.image = pygame.image.load("InteriorNave1.png")
    InteriorNave.rect = InteriorNave.image.get_rect()

    InteriorNave.rect.x = 0
    InteriorNave.rect.y = 0

    spritesJuego.add(InteriorNave)

    return InteriorNave
#Funcion para crear la escena de la izquierda de la nave
def escenaNave2(spritesJuego):
    InteriorNave = pygame.sprite.Sprite()

    InteriorNave.image = pygame.image.load("InteriorNave2.png")
    InteriorNave.rect = InteriorNave.image.get_rect()

    InteriorNave.rect.x = 0
    InteriorNave.rect.y = 0

    spritesJuego.add(InteriorNave)

    return InteriorNave
#Funcion para crear la escena de abajo de la nave
def escenaNave3(spritesJuego):
    InteriorNave = pygame.sprite.Sprite()

    InteriorNave.image = pygame.image.load("InteriorNave3.png")
    InteriorNave.rect = InteriorNave.image.get_rect()

    InteriorNave.rect.x = 0
    InteriorNave.rect.y = 0

    spritesJuego.add(InteriorNave)

    return InteriorNave
#Funcion para crear el mapa estelar
def mapa(spritesJuego):

    mapaEspacio = pygame.sprite.Sprite()

    mapaEspacio.image = pygame.image.load("MapaPlanetas.png")
    mapaEspacio.rect = mapaEspacio.image.get_rect()

    mapaEspacio.rect.x = 0
    mapaEspacio.rect.y = 0

    spritesJuego.add(mapaEspacio)

    return mapaEspacio
#Funcion para crear el selector de destino
def flecha (spritesJuego):
    flechaSeleccion = pygame.sprite.Sprite()

    flechaSeleccion.image = pygame.image.load("flechaSeleccion.png")
    flechaSeleccion.rect = flechaSeleccion.image.get_rect()

    flechaSeleccion.rect.x=790
    flechaSeleccion.rect.y=480

    spritesJuego.add(flechaSeleccion)

    return flechaSeleccion
#Funcion para crear la información del sol
def infoSol(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("infoSol.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Funcion para crear la información de mercurio
def infoMercurio(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("infoMercurio.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Funcion para crear la información de venus
def infoVenus(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("infoVenus.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Funcion para crear la información de la tierra
def infoTierra(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("infoTierra.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Funcion para crear la información de marte 
def infoMarte(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("infoMarte.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Función para crear la información de júpiter
def infoJupiter(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("infoJupiter.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Funcion para crear la información de saturno
def infoSaturno(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("InfoSaturno.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Función para crear la información de urano
def infoUrano(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("InfoUrano.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Función para crear la información de neptuno
def infoNeptuno(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("InfoNeptuno.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Función para crear la información de plutón
def infoPluton(spritesJuego):
    info = pygame.sprite.Sprite()
    
    info.image = pygame.image.load("infoPluton.png")
    info.rect = info.image.get_rect()

    info.rect.x = 100
    info.rect. y = 100

    spritesJuego.add(info)

    return info
#Funcion para crear el protagonista
def crearAstronauta(spritesJuego):

    protagonista = pygame.sprite.Sprite()

    protagonista.spriteSheet = pygame.image.load("Astronauta.png").convert()
      
    cargarFramesDerecha(protagonista)
    cargarFramesIzquierda(protagonista)
    cargarFramesAbajo(protagonista)
    cargarFramesArriba(protagonista)
    protagonista.rect.x = 50
    protagonista.rect.y = 50
    protagonista.velocidad_x = 0
    protagonista.velocidad_y = 0

    spritesJuego.add(protagonista)

    return protagonista
#Funcion para crear el astronauta en los planetas
def crearAstronautaPlaneta(spritesJuego):
    astronauta = pygame.sprite.Sprite()

    astronauta.spriteSheet = pygame.image.load("AstronautaEnPlaneta.png").convert()

    cargarFramesDerechaAChico(astronauta)
    cargarFramesIzquierdaAChico(astronauta)
    cargarFramesAbajoAChico(astronauta)
    cargarFramesArribaAChico(astronauta)

    astronauta.rect.x = 50
    astronauta.rect.y = 50

    astronauta.velocidad_x = 0
    astronauta.velocidad_y = 0

    spritesJuego.add(astronauta)

    return astronauta
#Funcion para crear la nave en movimiento
def crearNaveEnMovimiento(spritesJuego):
    naveMov = pygame.sprite.Sprite()

    naveMov.spriteSheet = pygame.image.load("spriteSheetNave.png")
    cargarFramesNaveDerecha(naveMov)
    cargarFramesNaveIzquierda(naveMov)
    cargarFramesNaveArriba(naveMov)
    cargarFramesNaveAbajo(naveMov)

    naveMov.rect.x= 700
    naveMov.rect.y = 400

    naveMov.velocidad_x = 0
    naveMov.velocidad_y = 0

    spritesJuego.add(naveMov)
    return naveMov
#Funcion para crear la nave 
def crearNave(spritesJuego):
    nave = pygame.sprite.Sprite()

    nave.image = pygame.image.load("Nave.png")
    nave.rect = nave.image.get_rect()

    nave.rect.x = 450
    nave.rect.y = 200

    spritesJuego.add(nave)

    return nave
#Funcion para crear el bidon de gasolina
def crearBidonGasofa(spritesJuego):
    bidon = pygame.sprite.Sprite()

    bidon.image = pygame.image.load("BidonGasofa.png")
    bidon.rect = bidon.image.get_rect()

    bidon.rect.x = 0
    bidon.rect.y = 0

    spritesJuego.add(bidon)

    return bidon
#Funcion para crear las piezas
def crearPiezas(spritesJuego):
    pieza = pygame.sprite.Sprite()

    pieza.image = pygame.image.load("Pieza.png")
    pieza.rect = pieza.image.get_rect()

    pieza.rect.x = 0
    pieza.rect.y = 0
    
    spritesJuego.add(pieza)
    return pieza
#Funcion para crear el objeto de la primera mision de la luna
def propulsorLuz(spritesJuego):
    propulsor = pygame.sprite.Sprite()

    propulsor.image = pygame.image.load("PropulsorDeLuz.png")
    propulsor.rect = propulsor.image.get_rect()

    propulsor.rect.x = 0
    propulsor.rect.y = 0

    spritesJuego.add(propulsor)
    return propulsor
#Funcion para crear la escena central de la luna
def escenaLuna1(spritesJuego):
    escenaLuna = pygame.sprite.Sprite()

    escenaLuna.image = pygame.image.load("EscenaLuna1.png")
    escenaLuna.rect = escenaLuna.image.get_rect()

    escenaLuna.rect.x = 0
    escenaLuna.rect.y = 0

    spritesJuego.add(escenaLuna)
    return escenaLuna
#Funcion para crear la escena de la izquierda de la luna
def escenaLuna2(spritesJuego):
    escenaLuna = pygame.sprite.Sprite()

    escenaLuna.image = pygame.image.load("EscenaLunaIzquierda.png")
    escenaLuna.rect = escenaLuna.image.get_rect()

    escenaLuna.rect.x = 0
    escenaLuna.rect.y = 0

    spritesJuego.add(escenaLuna)
    return escenaLuna
#Funcion para crear la escena de arriba de la luna
def escenaLuna3(spritesJuego):
    escenaLuna = pygame.sprite.Sprite()

    escenaLuna.image = pygame.image.load("EscenaLunaArriba.png")
    escenaLuna.rect = escenaLuna.image.get_rect()

    escenaLuna.rect.x = 0
    escenaLuna.rect.y = 0

    spritesJuego.add(escenaLuna)
    return escenaLuna
#Funcion para crear la escena de abajo de la luna
def escenaLuna4(spritesJuego):
    escenaLuna = pygame.sprite.Sprite()

    escenaLuna.image = pygame.image.load("EscenaLunaAbajo.png")
    escenaLuna.rect = escenaLuna.image.get_rect()

    escenaLuna.rect.x = 0
    escenaLuna.rect.y = 0

    spritesJuego.add(escenaLuna)
    return escenaLuna
#Funcion para crear la escena de arriba izquierda de la luna
def escenaLuna5(spritesJuego):
    escenaLuna = pygame.sprite.Sprite()

    escenaLuna.image = pygame.image.load("EscenaLunaArribaIzquierda.png")
    escenaLuna.rect = escenaLuna.image.get_rect()

    escenaLuna.rect.x = 0
    escenaLuna.rect.y = 0

    spritesJuego.add(escenaLuna)
    return escenaLuna
#Funcion para crear la escena de arriba derecha de la luna
def escenaLuna6(spritesJuego):
    escenaLuna = pygame.sprite.Sprite()

    escenaLuna.image = pygame.image.load("EscenaLunaArribaDerecha.png")
    escenaLuna.rect = escenaLuna.image.get_rect()

    escenaLuna.rect.x = 0
    escenaLuna.rect.y = 0

    spritesJuego.add(escenaLuna)
    return escenaLuna
#Funcion para crear la recompensa del secreto de la luna
def crearInyector(spritesJuego):
    inyector = pygame.sprite.Sprite()

    inyector.image=pygame.image.load("InyectorCuantico.png")
    inyector.rect = inyector.image.get_rect()

    inyector.rect.x = 100
    inyector.rect.y = 100

    spritesJuego.add(inyector)
    return inyector
#Funcion para crear la primera fila de escenas de marte
def crearEscenaMarte1_1(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte1_1.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
def crearEscenaMarte1_2(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte1_2.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
def crearEscenaMarte1_3(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte1_3.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
def crearEscenaMarte1_4(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte1_4.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
#Funcion para crear la segunda fila de escenas de marte
def crearEscenaMarte2_1(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte2_1.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
def crearEscenaMarteCentro(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarteCentro.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
def crearEscenaMarte2_3(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte2_3.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
def crearEscenaMarte2_4(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte2_4.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
#Funcion para crear la tercera fila de escenas de marte
def crearEscenaMarte3_1(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte3_1.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
def crearEscenaMarte3_2(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte3_2.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
def crearEscenaMarte3_3(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaMarte3_3.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)
    return escena
#Funcion para crear el generador de agua de la mision
def crearGeneradorAgua(spritesJuego):
    generador = pygame.sprite.Sprite()

    generador.image = pygame.image.load("GeneradorDeAgua.png")
    generador.rect = generador.image.get_rect()

    generador.rect.x = 100
    generador.rect.y = 100

    spritesJuego.add(generador)

    return generador
#Funcion para la primera pista secreta de marte
def CrearCartaSecretaMarte(spritesJuego):
    carta = pygame.sprite.Sprite()

    carta.image = pygame.image.load("cartaSecretaMarte.png")
    carta.rect = carta.image.get_rect()

    carta.rect.x = 200
    carta.rect.y = 150

    spritesJuego.add(carta)
    return carta
#Funcion para crear la segunda pista secreta de marte
def CrearCartaSecretaMarte2(spritesJuego):
    carta = pygame.sprite.Sprite()

    carta.image = pygame.image.load("cartaSecretaMarte2.png")
    carta.rect = carta.image.get_rect()

    carta.rect.x = 200
    carta.rect.y = 150

    spritesJuego.add(carta)
    return carta
#Funcion para crear la primera escena del paraiso
def CrearPrimeraEscenaParaiso(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("entradaParaiso.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear la escena del paraiso
def CrearElParaiso(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("ElParaiso.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear el primer mensaje dentro del paraiso
def crearPrimerMensajeParaiso(spritesJuego):
    mensaje = pygame.sprite.Sprite()

    mensaje.image = pygame.image.load("elParaisoMensaje1.png")
    mensaje.rect = mensaje.image.get_rect()

    mensaje.rect.x = 100
    mensaje.rect.y = 50

    spritesJuego.add(mensaje)
    return mensaje
#Funcion para crear el segundo menssaje dentro del paraiso
def crearSegundoMensajeParaiso(spritesJuego):
    mensaje = pygame.sprite.Sprite()

    mensaje.image = pygame.image.load("elParaisoMensaje2.png")
    mensaje.rect = mensaje.image.get_rect()

    mensaje.rect.x = 100
    mensaje.rect.y = 50

    spritesJuego.add(mensaje)
    return mensaje
#Funcion para crear el soporte vital
def crearSoporteVital (spritesJuego):
    soporte = pygame.sprite.Sprite()

    soporte.image = pygame.image.load("soporteVital.png")
    soporte.rect = soporte.image.get_rect()

    soporte.rect.x = 100
    soporte.rect.y = 100

    spritesJuego.add(soporte)

    return soporte
#funcion para crear la decision en jupiter
def crearDecisionJupiter(spritesJuego):
    decision = pygame.sprite.Sprite()

    decision.image = pygame.image.load("decidirEnJupiter.png")
    decision.rect = decision.image.get_rect()
    
    decision.rect.x = 100
    decision.rect.y = 100

    spritesJuego.add(decision)

    return decision
#Funcion para crear el cristal de atmosfera
def crearCristal(spritesJuego):
    cristal = pygame.sprite.Sprite()

    cristal.image = pygame.image.load("CristalDeAtmosfera.png")
    cristal.rect = cristal.image.get_rect()

    cristal.rect.x = 100
    cristal.rect.y = 100

    spritesJuego.add(cristal)

    return cristal
#Funcion para crear el distribuidor de energia
def crearDistribuidor(spritesJuego):
    distribuidor = pygame.sprite.Sprite()

    distribuidor.image = pygame.image.load("distribuidorDeEnergia.png")
    distribuidor.rect = distribuidor.image.get_rect()

    distribuidor.rect.x = 100
    distribuidor.rect.y = 100

    spritesJuego.add(distribuidor)

    return distribuidor
#Funcion para crear la primera escena en el espacio
def crearEscenaEspacio (spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escena1Meteoritos.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear la segunda escena en el espacio
def crearEscenaEspacio2 (spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escena2Meteoritos.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear la escena de la zona de jupiter
def crearEscenaEspacioJupiter(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("decisionJupiter.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear la escena central de urano
def crearEscenaCentralUrano(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaUranoCentral.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear la escena cruce de urano
def crearEscenaUranoCruce(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaUranoCruce.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear la escena de arriba de urano
def crearEscenaUranoArriba(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaUranoArriba.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear la escena de abajo de urano
def crearEscenaUranoAbajo(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaUranoAbajo.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
#Funcion para crear las bolas de hidrogeno
def crearBolaHidrogeno(spritesJuego):
    bola = pygame.sprite.Sprite()

    bola.image = pygame.image.load("simboloHidrogeno.png")
    bola.rect = bola.image.get_rect()

    bola.rect.x = 0
    bola.rect.y = 0

    spritesJuego.add(bola)

    return bola
#Funcion para crear el traje antipresion
def crearTrajeAntiPresion(spritesJuego):
    traje = pygame.sprite.Sprite()

    traje.image = pygame.image.load("trajeAntiPresion.png")
    traje.rect = traje.image.get_rect()

    traje.rect.x = 100
    traje.rect.y = 100

    spritesJuego.add(traje)

    return traje

    nivel = pygame.sprite.Sprite()

    nivel.image = pygame.image.load("nivelPluton.png")
    nivel.rect = nivel.image.get_rect()

    nivel.rect.x = 100
    nivel.rect.y = 100

    spritesJuego.add(nivel)

    return nivel
#Funcion para crear el gameover por vida
def crearGameOverVida(spritesJuego):
    fin = pygame.sprite.Sprite()

    fin.image = pygame.image.load("finJuegoVida.png")
    fin.rect = fin.image.get_rect()

    fin.rect.x = 100
    fin.rect.y = 100

    spritesJuego.add(fin)

    return fin 
#Funcion para crear el gameover por gasolina
def crearGameOverGasolina(spritesJuego):
    fin = pygame.sprite.Sprite()

    fin.image = pygame.image.load("finJuegoGasolina.png")
    fin.rect = fin.image.get_rect()

    fin.rect.x = 100
    fin.rect.y = 100

    spritesJuego.add(fin)

    return fin 
#Funcion para crear el gameover por meteoritos
def crearGameOverMeteoritos(spritesJuego):
    fin = pygame.sprite.Sprite()

    fin.image = pygame.image.load("finJuegoMeteoritos.png")
    fin.rect = fin.image.get_rect()

    fin.rect.x = 100
    fin.rect.y = 100

    spritesJuego.add(fin)

    return fin 
#Funcion para crear el gameover por entrar a jupiter
def crearGameOverEntrarJupiter(spritesJuego):
    fin = pygame.sprite.Sprite()

    fin.image = pygame.image.load("finJuegoEntrarJupiter.png")
    fin.rect = fin.image.get_rect()

    fin.rect.x = 100
    fin.rect.y = 100

    spritesJuego.add(fin)

    return fin
#Funcion para crear el gameover por el jefe final
def crearGameOverJefeFinal(spritesJuego):
    fin = pygame.sprite.Sprite()

    fin.image = pygame.image.load("finJuegoJefeFinal.png")
    fin.rect = fin.image.get_rect()

    fin.rect.x = 100
    fin.rect.y = 100

    spritesJuego.add(fin)

    return fin 
#Funcion para crear las balas
def crearBala(spritesJuego):
    bala = pygame.sprite.Sprite()

    bala.image = pygame.image.load("bala.png")
    bala.rect = bala.image.get_rect() 

    bala.rect.x = protagonistaEnPlaneta.rect.x
    bala.rect.y = protagonistaEnPlaneta.rect.y

    spritesJuego.add(bala)

    return bala
#Funcion para crear medicamentos de combate
def crearMedicamento(spritesJuego):
    medicamento = pygame.sprite.Sprite()

    medicamento.image = pygame.image.load("medicamento.png")
    medicamento.rect = medicamento.image.get_rect()

    medicamento.rect.x = 0
    medicamento.rect.y = 0

    spritesJuego.add(medicamento)
    return medicamento
def crearMira(spritesJuego):
    mira = pygame.sprite.Sprite()

    mira.image = pygame.image.load("mira.png")
    mira.rect = mira.image.get_rect()

    mira.rect.x = 0
    mira.rect.y = 0

    spritesJuego.add(mira)
    return mira
def crearExplosion(spritesJuego):
    explosion = pygame.sprite.Sprite()

    explosion.image = pygame.image.load("explosion.png")
    explosion.rect = explosion.image.get_rect()

    explosion.rect.x = 0
    explosion.rect.y = 0

    spritesJuego.add(explosion)
    return explosion
#Funcion para crear la escena central de pluton
def crearEscenaCentralPluton(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaPlutonCentral.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
def crearEscenaJefePluton(spritesJuego):
    escena = pygame.sprite.Sprite()

    escena.image = pygame.image.load("escenaBossPluton.png")
    escena.rect = escena.image.get_rect()

    escena.rect.x = 0
    escena.rect.y = 0

    spritesJuego.add(escena)

    return escena
def crearBalaMaligna(spritesJuego):
    bala = pygame.sprite.Sprite()

    bala.image = pygame.image.load("proyectilOscuro.png")
    bala.rect = bala.image.get_rect()

    bala.rect.x = 0
    bala.rect.y = 0

    spritesJuego.add(bala)

    return bala
def crearJefeFinal(spritesJuego):
    jefe = pygame.sprite.Sprite()

    jefe.spriteSheet = pygame.image.load("bossFinal.png").convert()
    cargarFramesJefeDerecha(jefe)
    cargarFramesJefeIzquierda(jefe)
    cargarFramesJefeAbajo(jefe)

    jefe.velocidad_x = 1
    spritesJuego.add(jefe)

    return jefe
def cargarFramesJefeDerecha(jefe):
    jefe.framesDerecha = []
    frame = obtenerFrame(jefe.spriteSheet,0,284.66,133.3,142.33)
    jefe.framesDerecha.append(frame)

    frame = obtenerFrame(jefe.spriteSheet,133.3,284.66,133.3,142.33)
    jefe.framesDerecha.append(frame)

    frame = obtenerFrame(jefe.spriteSheet,266.6,284.66,133.3,142.33)
    jefe.framesDerecha.append(frame)
def cargarFramesJefeIzquierda(jefe):
    jefe.framesIzquierda = []
    frame = obtenerFrame(jefe.spriteSheet,0,142.33,133.3,142.33)
    jefe.framesIzquierda.append(frame)

    frame = obtenerFrame(jefe.spriteSheet,133.3,142.33,133.3,142.33)
    jefe.framesIzquierda.append(frame)

    frame = obtenerFrame(jefe.spriteSheet,266.6,142.33,133.3,142.33)
    jefe.framesIzquierda.append(frame)
def cargarFramesJefeAbajo(jefe):
    jefe.framesAbajo = []
    frame = obtenerFrame(jefe.spriteSheet,0,0,133.3,142.33)
    jefe.framesAbajo.append(frame)

    frame = obtenerFrame(jefe.spriteSheet,133.3,0,133.3,142.33)
    jefe.framesAbajo.append(frame)

    frame = obtenerFrame(jefe.spriteSheet,266.6,0,133.3,142.33)
    jefe.framesAbajo.append(frame)

    jefe.image = jefe.framesAbajo[0]

    jefe.rect = jefe.image.get_rect()
def actualizarFrameJefe(jefe):
    if jefe.velocidad_x > 0:

        frame = (jefe.rect.x // 50) % len(jefe.framesDerecha)
        jefe.image = jefe.framesDerecha [frame]
    
    elif jefe.velocidad_x < 0 :

        frame = (jefe.rect.x  // 50) % len(jefe.framesIzquierda)
        jefe.image = jefe.framesIzquierda [frame]
    
    elif jefe.velocidad_x == 0:

        frame = (jefe.rect.x  // 50) % len(jefe.framesIzquierda)
        jefe.image = jefe.framesAbajo [frame]
def updateJefe(jefe):
    actualizarFrameJefe(jefe)

    jefe.rect.x+= jefe.velocidad_x
#Funcion para obtener los frames del spritesheet del protagonista
def obtenerFrame(spriteSheet,x,y,ancho,largo):
    frame = pygame.Surface([ancho,largo]).convert()

    frame.blit(spriteSheet,(0,0),(x,y,ancho,largo))

    frame.set_colorkey(negro)

    return frame
#Funcion para cargar los frames de la derecha del protagonista
def cargarFramesDerecha(protagonista):
    protagonista.framesDerecha = []
    frame = obtenerFrame(protagonista.spriteSheet,0,170,85,85)
    protagonista.framesDerecha.append(frame)

    frame = obtenerFrame(protagonista.spriteSheet,85,170,85,85)
    protagonista.framesDerecha.append(frame)

    frame = obtenerFrame(protagonista.spriteSheet,170,170,85,85)
    protagonista.framesDerecha.append(frame)
#Funcion para cargar los frames de la izquierda del protagonista
def cargarFramesIzquierda(protagonista):
    protagonista.framesIzquierda = []

    frame = obtenerFrame(protagonista.spriteSheet,0,85,85,85)
    
    protagonista.framesIzquierda.append(frame)

    frame = obtenerFrame(protagonista.spriteSheet,85,85,85,85)
    
    protagonista.framesIzquierda.append(frame)

    frame = obtenerFrame(protagonista.spriteSheet,170,85,85,85)
    
    protagonista.framesIzquierda.append(frame)
#Funcion para cargar los frames de abajo del protagonista
def cargarFramesAbajo(protagonista):
    protagonista.framesAbajo = []
    frame = obtenerFrame(protagonista.spriteSheet,0,0,85,85)
    
    protagonista.framesAbajo.append(frame)

    frame = obtenerFrame(protagonista.spriteSheet,85,0,85,85)
    
    protagonista.framesAbajo.append(frame)
    
    frame = obtenerFrame(protagonista.spriteSheet,170,0,85,85)
    
    protagonista.framesAbajo.append(frame)
    protagonista.image = protagonista.framesAbajo[0]

    protagonista.rect = protagonista.image.get_rect()
#Funcion para cargar los frames de arriba derecha del protagonista
def cargarFramesArriba(protagonista):
    protagonista.framesArriba = []
    frame = obtenerFrame(protagonista.spriteSheet,0,255,85,85)
    
    protagonista.framesArriba.append(frame)

    frame = obtenerFrame(protagonista.spriteSheet,85,255,85,85)
    
    protagonista.framesArriba.append(frame)

    frame = obtenerFrame(protagonista.spriteSheet,170,255,85,85)
    
    protagonista.framesArriba.append(frame)
#Funcion para actualizar los frames escogidos del protagonista
def actualizarFrame (protagonista):

    if protagonista.velocidad_x > 0:

        frame = (protagonista.rect.x // 50) % len(protagonista.framesDerecha)
        protagonista.image = protagonista.framesDerecha [frame]
    
    elif protagonista.velocidad_x < 0 :

        frame = (protagonista.rect.x  // 50) % len(protagonista.framesIzquierda)
        protagonista.image = protagonista.framesIzquierda [frame]
    
    elif protagonista.velocidad_y < 0:

        frame = (protagonista.rect.y // 50) % len(protagonista.framesArriba)
        protagonista.image = protagonista.framesArriba [frame]
    elif protagonista.velocidad_y >0:
        frame = (protagonista.rect.y  // 50) % len(protagonista.framesAbajo)
        protagonista.image = protagonista.framesAbajo [frame]

#Funcion para cargar los frames de la derecha del astronauta en el planeta
def cargarFramesDerechaAChico(astronauta):
    astronauta.framesDerecha = []
    frame = obtenerFrame(astronauta.spriteSheet,0,113,56.6,56.5)
    astronauta.framesDerecha.append(frame)

    frame = obtenerFrame(astronauta.spriteSheet,56.6,113,56.6,56.5)
    astronauta.framesDerecha.append(frame)

    frame = obtenerFrame(astronauta.spriteSheet,113.2,113,56.6,56.5)
    astronauta.framesDerecha.append(frame)
#Funcion para cargar los frames de la izquierda del astronauta en el planeta
def cargarFramesIzquierdaAChico (astronauta):
    astronauta.framesIzquierda = []

    frame = obtenerFrame(astronauta.spriteSheet,0,56.5,56.6,56.5)
    
    astronauta.framesIzquierda.append(frame)

    frame = obtenerFrame(astronauta.spriteSheet,56.6,56.5,56.6,56.5)
    
    astronauta.framesIzquierda.append(frame)

    frame = obtenerFrame(astronauta.spriteSheet,113.2,56.5,56.6,56.5)
    
    astronauta.framesIzquierda.append(frame)
#Funcion para cargar los frames de abajo del astronauta en el planeta
def cargarFramesAbajoAChico(astronauta):
    astronauta.framesAbajo = []
    frame = obtenerFrame(astronauta.spriteSheet,0,0,56.6,56.5)
    
    astronauta.framesAbajo.append(frame)

    frame = obtenerFrame(astronauta.spriteSheet,56.6,0,56.6,56.5)
    
    astronauta.framesAbajo.append(frame)

    frame = obtenerFrame(astronauta.spriteSheet,113.2,0,56.6,56.5)
    
    astronauta.framesAbajo.append(frame)
    astronauta.image = astronauta.framesAbajo[0]

    astronauta.rect = astronauta.image.get_rect()
#Funcion para cargar los frames de arriba del astronauta en el planeta
def cargarFramesArribaAChico(astronauta):
    astronauta.framesArriba = []
    frame = obtenerFrame(astronauta.spriteSheet,0,169.5,56.6,56.5)
    
    astronauta.framesArriba.append(frame)

    frame = obtenerFrame(astronauta.spriteSheet,56.6,169.5,56.6,56.5)
    
    astronauta.framesArriba.append(frame)

    frame = obtenerFrame(astronauta.spriteSheet,113.2,169.5,56.6,56.5)
    
    astronauta.framesArriba.append(frame)
#Funcion para cargar los frames de la derecha de la nave
def cargarFramesNaveDerecha(naveMov):
    naveMov.framesDerecha = []
    frame = obtenerFrame(naveMov.spriteSheet,0,103,64,61)
    naveMov.framesDerecha.append(frame)
#Funcion para cargar los frames de la izquierda de la nave
def cargarFramesNaveIzquierda(naveMov):
    naveMov.framesIzquierda = []
    frame = obtenerFrame(naveMov.spriteSheet,0,175,64,58.5)
    naveMov.framesIzquierda.append(frame)
    naveMov.image = naveMov.framesIzquierda[0]

    naveMov.rect = naveMov.image.get_rect()
#Funcion para cargar los frames de arriba de la nave
def cargarFramesNaveArriba(naveMov):
    naveMov.framesArriba = []
    frame = obtenerFrame(naveMov.spriteSheet,0,0,64,52)
    naveMov.framesArriba.append(frame)
#Funcion pata cargar los frames de abajo de la nave
def cargarFramesNaveAbajo(naveMov):
    naveMov.framesAbajo = []
    frame = obtenerFrame(naveMov.spriteSheet,0,52,64,52)
    naveMov.framesAbajo.append(frame)
#Funcion que gestiona la movilidad del protagonista y la interacción con objetos
def gestionarEventos(protagonista,funcionando,interactuar,volver):
    hacer = False
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            funcionando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w: 
                if(trajeAP==True):
                    protagonista.velocidad_y = -2
                else:
                    protagonista.velocidad_y = -1
            if evento.key == pygame.K_s:
                if(trajeAP==True):
                    protagonista.velocidad_y = 2
                else:
                    protagonista.velocidad_y = 1
            if evento.key  == pygame.K_a:
                if(trajeAP==True):
                    protagonista.velocidad_x = -2
                else:
                    protagonista.velocidad_x = -1
            if evento.key == pygame.K_d:
                if(trajeAP==True):
                    protagonista.velocidad_x = 2
                else:
                    protagonista.velocidad_x = 1
            if evento.key == pygame.K_e and interactuar==True:
                hacer=True
        elif (evento.type == pygame.KEYUP):

            if (evento.key == pygame.K_w) and (protagonista.velocidad_y < 0):

                protagonista.velocidad_y = 0

            if (evento.key == pygame.K_s) and (protagonista.velocidad_y > 0):

                protagonista.velocidad_y = 0

            if (evento.key  == pygame.K_a) and (protagonista.velocidad_x < 0):

                protagonista.velocidad_x = 0

            if (evento.key == pygame.K_d) and (protagonista.velocidad_x > 0):

                protagonista.velocidad_x = 0
            
            if (evento.key == pygame.K_e):
                hacer = False

    return funcionando,hacer,volver
#Funcion que gestiona la interacción del mapa 
def gestionarEventosMapa(pintarFlecha,volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton):             
    teclaPulsada = pygame.key.get_pressed()
    if(teclaPulsada[pygame.K_ESCAPE]):
        volver=True
    if(teclaPulsada[pygame.K_LEFT]):
        pintarFlecha.rect.x -= 1
    if(teclaPulsada[pygame.K_RIGHT]):
        pintarFlecha.rect.x +=1 
    if(teclaPulsada[pygame.K_RETURN]):
        if(pintarFlecha.rect.x>500 and pintarFlecha.rect.x<515 and luna==True):
            estadoInicial=False
        if(pintarFlecha.rect.x>450 and pintarFlecha.rect.x<480 and marte==True):
            estadoInicial=False
            luna = False
        if(pintarFlecha.rect.x>290 and pintarFlecha.rect.x<350 and jupiter==True):
            estadoInicial=False
            marte=False
        if(pintarFlecha.rect.x>110 and pintarFlecha.rect.x<130 and urano==True):
            estadoInicial=False
            jupiter=False
        if(pintarFlecha.rect.x>5 and pintarFlecha.rect.x<17):
            estadoInicial=False
            urano=False
    else:
        pintarFlecha.rect.x+=0
     
    
    return volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton       
#Funcion destinada a las colisiones de la escena central de la nave
def colisionNave1(protagonista):
    #paredes
    if(protagonista.rect.x<50 and protagonista.rect.y>301 and protagonista.rect.y<800):
        protagonista.rect.x=60
    if(protagonista.rect.x<50 and protagonista.rect.y>90 and protagonista.rect.y<149):
        protagonista.rect.x=60
    if(protagonista.rect.x>680 and protagonista.rect.y>90 and protagonista.rect.y<800):
        protagonista.rect.x=670
    if(protagonista.rect.y<90 and protagonista.rect.x>20 and protagonista.rect.x<750):
        protagonista.rect.y=100
#Funcion destinada a las colisiones de la escena de la izquierda de la nave
def colisionNave2(protagonista):
    #paredes
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
#Funcion destinada a las colisiones de la escena de la derecha de la nave
def colisionNave3(protagonista):
    #Paredes
    if(protagonista.rect.x<60 and protagonista.rect.y>90 and protagonista.rect.y<800):
        protagonista.rect.x=70
    if(protagonista.rect.x>660 and protagonista.rect.y>0 and protagonista.rect.y<800):
        protagonista.rect.x=650
    if(protagonista.rect.y>580 and protagonista.rect.x>160 and protagonista.rect.x<660):
        protagonista.rect.y = 570
    #bidon de gasolina
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
#Funcion para actualizar el movimiento del protagonista
def udapte (protagonista):

    actualizarFrame(protagonista)

    protagonista.rect.x = protagonista.rect.x + protagonista.velocidad_x

    protagonista.rect.y = protagonista.rect.y + protagonista.velocidad_y
#Funcion para cambiar de escena en la nave
def cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo):
    posicion = False
    if(protagonista.rect.x<10 and (protagonista.rect.y>150 and protagonista.rect.y<300) and escenaNaveIzquierda==False):
        escenaNaveCentro = False
        escenaNaveIzquierda = True
        posicion = True
        if(posicion):
            protagonista.rect.x = 690
    elif(protagonista.rect.x>690 and (protagonista.rect.y>50 and protagonista.rect.y<250) and escenaNaveCentro==False):
        escenaNaveIzquierda = False
        escenaNaveCentro = True
        posicion = True
        if(posicion):
            protagonista.rect.x = 60
    elif(protagonista.rect.y>770 and (protagonista.rect.x>60 and protagonista.rect.x<740) and escenaNaveAbajo==False):
        escenaNaveCentro=False
        escenaNaveAbajo=True
        posicion=True
        if(posicion):
            protagonista.rect.y = 10
    elif(protagonista.rect.y<-30 and (protagonista.rect.x>60 and protagonista.rect.x<740) and escenaNaveCentro==False):
        escenaNaveAbajo=False
        escenaNaveCentro=True
        posicion=True
        if(posicion):
            protagonista.rect.y=740

    return escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo
#Funcion para las interacciones con la nave
def interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion):
    #Caja de balas
    if(protagonista.rect.x>540 and protagonista.rect.x<580 and protagonista.rect.y>100 and protagonista.rect.y<360 and escenaNaveAbajo==True):
        Interaccion = "Pulse e para recoger balas"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(830,760))
        if(balas<100):
            interactuar = True
        else:
            interactuar=False
        if(hacer==True and balas<100):
            balas = 100
            interactuar=False
    #Caja de gasolina
    elif(protagonista.rect.x>60 and protagonista.rect.x<190 and protagonista.rect.y>500 and protagonista.rect.y<570 and escenaNaveAbajo==True):
        Interaccion = "Pulse e para rellenar gasolina"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(830,760))
        if(gasolina<=100):
            interactuar = True
        else:
            interactuar=False
        if(gasolina>100):
            gasolina=100
        
        if(hacer==True and bidones>0):
            bidones-=1
            if(distribuidorDeEnergia==True):
                gasolina+=45
            else:
                gasolina+=33
            interactuar=False
        
    #Caja de herramientas de arreglo
    elif(protagonista.rect.x>500 and protagonista.rect.x<760 and protagonista.rect.y>540 and escenaNaveAbajo==True):
        Interaccion = "Pulse e para arreglar la nave"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(830,760))
        if(arreglos<=100):
            interactuar = True
        else:
            interactuar=False
        if(arreglos>100):
            arreglos=100
        if(hacer==True and piezas>0):
            piezas-=1
            if(distribuidorDeEnergia==True):
                arreglos+=25
            else:
                arreglos+=10
            interactuar=False
    #Curacion
    elif(protagonista.rect.x>660  and protagonista.rect.y>120 and protagonista.rect.y<210 and escenaNaveCentro==True):
        Interaccion = "Pulse e para curarse"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(830,760))
        if(vida<=100):
            interactuar = True
        else:
            interactuar=False
        if(hacer==True):
            vida = 100
            interactuar=False
    #Sala de mandos
    elif(protagonista.rect.x>310 and protagonista.rect.x<410 and protagonista.rect.y>590 and escenaNaveIzquierda==True):
        Interaccion = "Pulse e para pilotar la nave"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(830,760))
        interactuar = True
        if(hacer==True):
            cambiarMapa = True
    elif(protagonista.rect.x>300 and protagonista.rect.x<400 and protagonista.rect.y<150 and escenaNaveCentro == True and estadoInicial==True and (luna==True or marte==True or urano==True or pluton==True)):
        Interaccion = "Pulse e para salir de la nave"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(830,760))
        interactuar=True
        if(hacer == True):
            estadoInicial=False
            interactuar=False
    elif(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540 and escenaNaveAbajo==True and reunirPiezas==True and terminarMarte==False):
        Interaccion = "Pulse e para crear el generador"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(820,760))
        interactuar = True
        if(hacer==True):
            generadorAgua=True
            piezas-=4
    elif(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540 and escenaNaveAbajo==True and cogerCristal==True and distribuidorDeEnergia==False):
        Interaccion = "Pulse e para crear el distribuidor"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(820,760))
        interactuar=True
        if(hacer==True):
            cogerDistribuidor=True
    elif(protagonista.rect.x>191 and protagonista.rect.x<499 and protagonista.rect.y>540 and escenaNaveAbajo==True and trajeAP==False and reunirHidrogeno==True):
        Interaccion = "Pulse e para crear el traje"
        transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(transmitir,(820,760))
        interactuar=True
        if(hacer==True):
            cogerTrajeAntiPresion=True
    else:
        interactuar = False
        
    
    
    return interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion
#Funcion para mostrar los mensajes del estado de la nave y el personaje       
def mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas):
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
#Funcion para mostrar las opciones en el mapa estelar
def mensajesMapa(cambiarMapa,pintarFlecha,informacionSol,informacionMercurio,informacionVenus,informacionTierra,informacionMarte,informacionJupiter,informacionSaturno,informacionUrano,informacionNeptuno,informacionPluton):
    mensajeEscape = "PULSA ESC PARA SALIR DEL MAPA"
    transmitirEscape = fraseMapa.render(mensajeEscape,1,blanco)
    screen.blit(transmitirEscape,(10,10))
    mensajeEnter = "PULSA ENTER PARA VIAJAR A UN PLANETA"
    transmitirEnter = fraseMapa.render(mensajeEnter,1,blanco)
    screen.blit(transmitirEnter,(10,40))
    mensajeFDerecha = "PULSA --> PARA MOVERTE A LA DERECHA"
    transmitirFDerecha = fraseMapa.render(mensajeFDerecha,1,blanco)
    screen.blit(transmitirFDerecha,(10,70))
    mensajeFIzquierda = "PULSA <-- PARA MOVERTE A LA IZQUIERDA"
    transmitirFIzquierda = fraseMapa.render(mensajeFIzquierda,1,blanco)
    screen.blit(transmitirFIzquierda,(10,100))
    if(pintarFlecha.rect.x>680 and pintarFlecha.rect.x<760):
        informacionSol.draw(screen)
    if(pintarFlecha.rect.x>630 and pintarFlecha.rect.x<650):
        informacionMercurio.draw(screen)
    if(pintarFlecha.rect.x>580 and pintarFlecha.rect.x<610):
        informacionVenus.draw(screen)
    if(pintarFlecha.rect.x>530 and pintarFlecha.rect.x<560):
        informacionTierra.draw(screen)
    if(pintarFlecha.rect.x>450 and pintarFlecha.rect.x<480):
        informacionMarte.draw(screen)
    if(pintarFlecha.rect.x>290 and pintarFlecha.rect.x<350):
        informacionJupiter.draw(screen)
    if(pintarFlecha.rect.x>200 and pintarFlecha.rect.x<260):
        informacionSaturno.draw(screen)
    if(pintarFlecha.rect.x>110 and pintarFlecha.rect.x<130):
        informacionUrano.draw(screen)
    if(pintarFlecha.rect.x>50 and pintarFlecha.rect.x<70):
        informacionNeptuno.draw(screen)
    if(pintarFlecha.rect.x>5 and pintarFlecha.rect.x<17):
        informacionPluton.draw(screen)
#Funcion que gestiona y comenta las misiones
def misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton):
    if(estadoInicial==True and luna==False and marte==False and jupiter==False and saturno==False and urano==False and neptuno==False and pluton==False):
        mision = "Ve a la sala de mandos"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(865,640))
    if(cambiarMapa==True and luna==True and marte==False):
        mision = "Ve a la luna"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(910,640)) 
    if(luna==True and cogerPropulsor==False and estadoInicial==False):
        mision = "Coge el propulsor de luz"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(855,640)) 
    if(luna==True and cogerPropulsor==False and estadoInicial==True):
        mision = "Sal de la nave"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(910,640)) 
    if(luna==True and cogerPropulsor==True and estadoInicial==False):
        mision = "Vuelve a la nave"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(900,640)) 
    if(luna==True and cogerPropulsor==True and estadoInicial==True and cambiarMapa==False):
        mision = "Ve a la sala de mandos"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(865,640)) 
    if(cambiarMapa==True and marte==True and jupiter==False):
        mision="Ve a marte"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(910,640))
    if(marte==True and reunirPiezas==False and estadoInicial==False):
        mision="Reune "+str(4-piezas)+" piezas"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(910,640))
    if(marte==True and reunirPiezas==False and estadoInicial==True):
        mision="Sal de la nave"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(910,640))
    if(marte==True and reunirPiezas==True and estadoInicial==False):
        if(paraiso==True and soporteVital==False):
            mision="Vuelve a la nave o ve al paraiso"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(810,640))
        else:
            mision="Vuelve a la nave"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(910,640))
    if(marte==True and reunirPiezas==True and estadoInicial==True and escenaNaveAbajo==False and terminarMarte==False):
        mision="Ve a la sala de recursos"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(865,640))
    if(marte==True and reunirPiezas==True and estadoInicial==True and escenaNaveAbajo==True and terminarMarte==False):
        mision="Construye el generador de agua"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(810,640))
    if(marte==True and terminarMarte==True and estadoInicial==True and cambiarMapa==False):
        mision="Ve a la sala de mandos"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))
    if(cambiarMapa==True and jupiter==True and urano==False):
        mision="Ve a jupiter"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))
    if(jupiter==True and escenaEspacio==True or escenaEspacio2==True):
        mision="Avanza por el espacio"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))
    if(jupiter==True and escenaZonaJupiter==True and decidir==False):
        if(pintarNaveMovimiento.rect.x<340):
            mision="Toma una decision"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(880,640))
        else:
            mision="Acercate a jupiter"
            transmitir = fraseIteraccion.render(mision,1,blanco)
            screen.blit(transmitir,(880,640))
    if(jupiter==True and cogerCristal==True and distribuidorDeEnergia==False and escenaNaveAbajo==False and decision==2):
        mision="Ve a la sala de recursos"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))
    if(jupiter==True and distribuidorDeEnergia==False and escenaNaveAbajo==True and decision==2):
        mision="Construye el distribuidor"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(810,640))
    if(jupiter==True and terminarJupiter==True and cambiarMapa==False):
        mision="Ve a la sala de mandos"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))    
    if(cambiarMapa==True and urano==True and pluton==False):
        mision="Ve a urano"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640)) 
    if(urano==True and reunirHidrogeno==False):
        mision="Reune "+str(5-hidrogeno)+" de hidrogeno"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))  
    if(urano==True and reunirHidrogeno==False and estadoInicial==True):
        mision="Sal de la nave"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))
    if(urano==True and reunirHidrogeno==True and estadoInicial==False):
        mision="Vuelve a la nave"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))  
    if(urano==True and reunirHidrogeno==True and escenaNaveAbajo==False and estadoInicial==True and trajeAP==False):
        mision="Ve a la sala de recursos"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(880,640))
    if(urano==True and reunirHidrogeno==True and escenaNaveAbajo==True and estadoInicial==True and trajeAP==False):
        mision="Construye el traje Antipresion"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(810,640))
    if(urano==True and terminarUrano==True and estadoInicial==True and cambiarMapa==False):
        mision="Ve a la sala de mandos"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(810,640))
    if(cambiarMapa==True and pluton==True):
        mision="Ve a pluton"
        transmitir = fraseIteraccion.render(mision,1,blanco)
        screen.blit(transmitir,(810,640))
#Funcion para cambiar de escena en la luna
def cambiarEscenaLuna(protagonista,escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha):
    if(protagonista.rect.x<0 and escenaLunaCentro==True):
        escenaLunaCentro=False
        escenaLunaIzquierda = True
        protagonista.rect.x=700
    elif(protagonista.rect.y>790 and escenaLunaCentro==True):
        escenaLunaCentro=False
        escenaLunaAbajo = True
        protagonista.rect.y=30
    elif(protagonista.rect.y<-10 and escenaLunaCentro==True):
        escenaLunaCentro=False
        escenaLunaArriba=True
        protagonista.rect.y=780
    elif(protagonista.rect.x>730 and escenaLunaIzquierda==True):
        escenaLunaIzquierda=False
        escenaLunaCentro=True
        protagonista.rect.x=30
    elif(protagonista.rect.y<-10 and escenaLunaIzquierda==True):
        escenaLunaArribaIzquierda=True
        escenaLunaIzquierda=False
        protagonista.rect.y=780
    elif(protagonista.rect.y<-10 and escenaLunaAbajo==True):
        escenaLunaCentro=True
        escenaLunaAbajo=False
        protagonista.rect.y=780
    elif(protagonista.rect.y>790 and escenaLunaArriba==True):
        escenaLunaCentro=True
        escenaLunaArriba=False
        protagonista.rect.y=20
    elif(protagonista.rect.x<10 and escenaLunaArriba==True):
        escenaLunaArribaIzquierda=True
        escenaLunaArriba=False
        protagonista.rect.x=700
    elif(protagonista.rect.x>730 and escenaLunaArriba==True):
        escenaLunaArribaDerecha=True
        escenaLunaArriba=False
        protagonista.rect.x=30
    elif(protagonista.rect.x<10 and escenaLunaArribaDerecha==True):
        escenaLunaArriba=True
        escenaLunaArribaDerecha=False
        protagonista.rect.x=700
    elif(protagonista.rect.x>730 and escenaLunaArribaIzquierda==True):
        escenaLunaArriba=True
        escenaLunaArribaIzquierda=False
        protagonista.rect.x=30
    elif(protagonista.rect.y>790 and escenaLunaArribaIzquierda==True):
        escenaLunaIzquierda=True
        escenaLunaArribaIzquierda=False
        protagonista.rect.y=30
    return escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha
#Colisiones escena central
def colisionLuna1(protagonista):
    if(protagonista.rect.x>680):
        protagonista.rect.x=670
#Colisiones escena izquierda
def colisionLuna2(protagonista):
    if(protagonista.rect.x<45):
        protagonista.rect.x=55
    if(protagonista.rect.y>675):
        protagonista.rect.y=665
#Colisiones escena abajo
def colisionLuna3(protagonista):
    if(protagonista.rect.x>675):
        protagonista.rect.x=665
    if(protagonista.rect.x<45):
        protagonista.rect.x=55
    if(protagonista.rect.y>675):
        protagonista.rect.y=665
#Colisiones escena abajo
def colisionLuna4(protagonista):
    if(protagonista.rect.y<40):
        protagonista.rect.y=50
#Colisiones escena arriba izquierda
def colisionLuna5(protagonista):
    if(protagonista.rect.x<45):
        protagonista.rect.x=55
    if(protagonista.rect.y<40):
        protagonista.rect.y=50
#Colisiones escena arriba derecha
def colisionLuna6(protagonista):
    if(protagonista.rect.x>670):
        protagonista.rect.x=660
    if(protagonista.rect.y<40):
        protagonista.rect.y=50
    if(protagonista.rect.y>675):
        protagonista.rect.y=665   
#Colision con la nave en los planetas
def colisionConNave(protagonista,nave):
    if(protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x-40) and protagonista.rect.y>(nave.rect.y-20) and protagonista.rect.y<(nave.rect.y+237)):
        protagonista.rect.x = nave.rect.x - 60
    if (protagonista.rect.y>(nave.rect.y-50) and protagonista.rect.y<(nave.rect.y-40) and protagonista.rect.x>(nave.rect.x-20) and protagonista.rect.x<(nave.rect.x+310)):
        protagonista.rect.y = nave.rect.y - 60
    if(protagonista.rect.x>(nave.rect.x+295) and protagonista.rect.x<(nave.rect.x+300) and protagonista.rect.y>(nave.rect.y-10) and protagonista.rect.y<(nave.rect.y+227)):
        protagonista.rect.x = nave.rect.x +310
    if(protagonista.rect.y>(nave.rect.y+227) and protagonista.rect.y<(nave.rect.y+237) and protagonista.rect.x>(nave.rect.x-50) and protagonista.rect.x<(nave.rect.x+310)):
        protagonista.rect.y = nave.rect.y + 247
#Funcion para las interacciones en la luna
def interaccionesLuna(protagonista,interactuar,hacer,escenaLunaCentro,escenaLunaIzquierda,escenaLunaArriba,escenaLunaAbajo,escenaLunaArribaIzquierda,escenaLunaArribaDerecha,estadoInicial,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna):
    if(protagonista.rect.y>430 and protagonista.rect.y<470 and protagonista.rect.x>530 and protagonista.rect.x<620 and escenaLunaCentro==True):
        Interaccion = "Pulse e para entrar a la nave"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True and escenaLunaCentro==True):
            estadoInicial=True
            escenaNaveCentro=True
            escenaLunaCentro=False
            interactuar=False
    if(protagonista.rect.x>320 and protagonista.rect.x<480 and protagonista.rect.y>540 and protagonista.rect.y<665 and escenaLunaAbajo==True and cogerPieza==False):
        Interaccion = "Pulse e para recoger la pieza"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            cogerPieza=True
            piezas+=1
    if(protagonista.rect.x>445 and protagonista.rect.x<645 and protagonista.rect.y>600 and protagonista.rect.y<700 and escenaLunaArriba==True and cogerBidon==False):
        Interaccion = "Pulse e para recoger el bidon"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar = True
        if(hacer == True):
            cogerBidon=True
            bidones+=1
    if(protagonista.rect.x>220 and protagonista.rect.x<520 and protagonista.rect.y>330 and protagonista.rect.y<592 and escenaLunaArribaIzquierda==True and cogerPropulsor==False):
        Interaccion = "Pulse e para recoger el propulsor"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer == True):
            cogerPropulsor=True
    if(protagonista.rect.x>365 and protagonista.rect.x<495 and protagonista.rect.y>230 and protagonista.rect.y<375 and escenaLunaArribaDerecha==True):
        Interaccion = "???"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(975,760))
        interactuar = True
        if(hacer == True):
            encontrarSecretoLuna=True
    
    return interactuar,estadoInicial,escenaLunaCentro,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna
#Funcion para revelar el secreto de la luna
def secretoLuna(inyector,encontrarSecretoLuna,inyectorGasolina):
    teclaPulsada = pygame.key.get_pressed()
    if(encontrarSecretoLuna==True):
        inyector.draw(screen)
        inyectorGasolina=True
        if(teclaPulsada[pygame.K_RETURN]):
            encontrarSecretoLuna=False
    return encontrarSecretoLuna,inyectorGasolina
#Funcion para cambiar de escena en marte de la primera fila
def cambiarEscenaMarteFila1(protagonista,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3):
    #Escena de la izquierda
    if(protagonista.rect.x>760 and escenaMarte1_1==True):
        escenaMarte1_2=True
        escenaMarte1_1=False
        protagonista.rect.x = 20
    if(protagonista.rect.y>790 and escenaMarte1_1==True):
        escenaMarte2_1=True
        escenaMarte1_1=False
        protagonista.rect.y = 20
    #Escena central
    if(protagonista.rect.x>760 and escenaMarte1_2==True):
        escenaMarte1_3=True
        escenaMarte1_2=False
        protagonista.rect.x = 20
    if(protagonista.rect.x<10 and escenaMarte1_2==True):
        escenaMarte1_1=True
        escenaMarte1_2=False
        protagonista.rect.x = 750
    if(protagonista.rect.y>790 and escenaMarte1_2==True):
        escenaMarteCentro=True
        escenaMarte1_2=False
        protagonista.rect.y = 20
    #Escena de la derecha
    if(protagonista.rect.x<10 and escenaMarte1_3==True):
        escenaMarte1_2=True
        escenaMarte1_3=False
        protagonista.rect.x = 750
    if(protagonista.rect.y>790 and escenaMarte1_3==True):
        escenaMarte2_3=True
        escenaMarte1_3=False
        protagonista.rect.y = 20
    if(protagonista.rect.y<-10 and escenaMarte1_3==True):
        escenaMarte1_4=True
        escenaMarte1_3=False
        protagonista.rect.y = 780
    #Escena especial
    if(protagonista.rect.y>790 and escenaMarte1_4==True):
        escenaMarte1_3=True
        escenaMarte1_4=False
        protagonista.rect.y = 20

    return escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3 
#Funcion para cambiar de escena en marte de la segunda fila
def cambiarEscenaMarteFila2(protagonista,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3):
    #Escena centro
    if(protagonista.rect.x>760 and escenaMarteCentro==True):
        escenaMarte2_3=True
        escenaMarteCentro=False
        protagonista.rect.x = 20
    if(protagonista.rect.x<10 and escenaMarteCentro==True):
        escenaMarte2_1=True
        escenaMarteCentro=False
        protagonista.rect.x = 750
    if(protagonista.rect.y>790 and escenaMarteCentro==True):
        escenaMarte3_2=True
        escenaMarteCentro=False
        protagonista.rect.y = 20
    if(protagonista.rect.y<-10 and escenaMarteCentro==True):
        escenaMarte1_2=True
        escenaMarteCentro=False
        protagonista.rect.y = 770
    #Escena derecha
    if(protagonista.rect.x>760 and escenaMarte2_3==True):
        escenaMarte2_4=True
        escenaMarte2_3=False
        protagonista.rect.x = 20
    if(protagonista.rect.x<10 and escenaMarte2_3==True):
        escenaMarteCentro=True
        escenaMarte2_3=False
        protagonista.rect.x = 750
    if(protagonista.rect.y>790 and escenaMarte2_3==True):
        escenaMarte3_3=True
        escenaMarte2_3=False
        protagonista.rect.y = 20
    if(protagonista.rect.y<-10 and escenaMarte2_3==True):
        escenaMarte1_3=True
        escenaMarte2_3=False
        protagonista.rect.y = 780
    #Escena izquierda
    if(protagonista.rect.x>760 and escenaMarte2_1==True):
        escenaMarteCentro=True
        escenaMarte2_1=False
        protagonista.rect.x = 20
    if(protagonista.rect.y>790 and escenaMarte2_1==True):
        escenaMarte3_1=True
        escenaMarte2_1=False
        protagonista.rect.y = 20
    if(protagonista.rect.y<-10 and escenaMarte2_1==True):
        escenaMarte1_1=True
        escenaMarte2_1=False
        protagonista.rect.y = 780
    #Escena especial
    if(protagonista.rect.x<10 and escenaMarte2_4==True):
        escenaMarte2_3=True
        escenaMarte2_4=False
        protagonista.rect.x = 750


    return escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3
#Funcion para cambiar de escena en marte de la tercera fila
def cambiarEscenaMarteFila3(protagonista,escenaMarteCentro,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,escenaMarte2_1,escenaMarte2_3):
    #Escena de la izquierda
    if(protagonista.rect.x>760 and escenaMarte3_1==True):
        escenaMarte3_2=True
        escenaMarte3_1=False
        protagonista.rect.x = 20
    if(protagonista.rect.y<-10 and escenaMarte3_1==True):
        escenaMarte2_1=True
        escenaMarte3_1=False
        protagonista.rect.y = 780
    #Escena central
    if(protagonista.rect.x>760 and escenaMarte3_2==True):
        escenaMarte3_3=True
        escenaMarte3_2=False
        protagonista.rect.x = 20
    if(protagonista.rect.x<10 and escenaMarte3_2==True):
        escenaMarte3_1=True
        escenaMarte3_2=False
        protagonista.rect.x = 750
    if(protagonista.rect.y<-10 and escenaMarte3_2==True):
        escenaMarteCentro=True
        escenaMarte3_2=False
        protagonista.rect.y = 780
    #Escena de la derecha
    if(protagonista.rect.x<10 and escenaMarte3_3==True):
        escenaMarte3_2=True
        escenaMarte3_3=False
        protagonista.rect.x = 750
    if(protagonista.rect.y<-10 and escenaMarte3_3==True):
        escenaMarte2_3=True
        escenaMarte3_3=False
        protagonista.rect.y = 780
    
    return escenaMarteCentro,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,escenaMarte2_1,escenaMarte2_3
#Funcion para las colisiones de la fila de arriba de marte
def colisionesMarteFilaArriba(protagonista,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4):
    if(escenaMarte1_1==True):
        if(protagonista.rect.y<35):
            protagonista.rect.y=45
        if(protagonista.rect.x<30):
            protagonista.rect.x=40
    elif(escenaMarte1_2==True):
        if(protagonista.rect.y<35):
            protagonista.rect.y=45
    elif(escenaMarte1_3==True):
        if(protagonista.rect.x>710):
            protagonista.rect.x=700
    elif(escenaMarte1_4==True):
        if(protagonista.rect.x>710):
            protagonista.rect.x=700
        if(protagonista.rect.x<30):
            protagonista.rect.x=40
        if(protagonista.rect.y<35):
            protagonista.rect.y=45
    #Colision con cueva
        if(protagonista.rect.x>270 and protagonista.rect.x<275 and protagonista.rect.y>30 and protagonista.rect.y<230):
            protagonista.rect.x=260
        if(protagonista.rect.x>490 and protagonista.rect.x<495 and protagonista.rect.y>30 and protagonista.rect.y<230):
            protagonista.rect.x=500
        if(protagonista.rect.y>30 and protagonista.rect.y<40 and protagonista.rect.x>270 and protagonista.rect.x<490):
            protagonista.rect.y = 20
        if(protagonista.rect.y>220 and protagonista.rect.y<230 and protagonista.rect.x>270 and protagonista.rect.x<490):
            protagonista.rect.y = 230
#Funcion para las colisiones de la fila central de marte
def colisionesMarteFilaCentral(protagonista,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4):
    if(escenaMarte2_1==True):
        if(protagonista.rect.x<30):
            protagonista.rect.x=40
    elif(escenaMarte2_4==True):
        if(protagonista.rect.x>710):
            protagonista.rect.x=700
        if(protagonista.rect.y>705):
            protagonista.rect.y=695
        if(protagonista.rect.y<35):
            protagonista.rect.y=45
#Funcion para las colisiones de la fila inferior de marte
def colisionesMarteFilaAbajo(protagonista,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3):
    if(escenaMarte3_1==True):
        if(protagonista.rect.x<30):
            protagonista.rect.x = 40
        if(protagonista.rect.y>705):
            protagonista.rect.y = 695
    elif(escenaMarte3_2==True):
        if(protagonista.rect.y>705):
            protagonista.rect.y = 695
    elif(escenaMarte3_3==True):
        if(protagonista.rect.x>710):
            protagonista.rect.x = 700
        if(protagonista.rect.y>705):
            protagonista.rect.y = 695
#Funcion para gestionar las interacciones en marte en la fila de arriba
def interaccionesMarteArriba(protagonista,interactuar,hacer,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,bidones,vida,pieza,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso):
    if(protagonista.rect.x>130 and protagonista.rect.x<270 and protagonista.rect.y>520 and protagonista.rect.y<680 and escenaMarte1_1==True and cogerBidon==False):
        Interaccion = "Pulse e para coger el bidon"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            bidones+=1
            cogerBidon=True

    if(protagonista.rect.x>65 and protagonista.rect.x<145 and protagonista.rect.y>60 and protagonista.rect.y<130 and escenaMarte1_1==True):
        Interaccion = "Pulse e para recuperar vida"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(vida>100):
            vida=100
        if(hacer==True and vida<100):
            if(generadorAgua==True):
                vida+=20
            else:
                vida+=10
    if(protagonista.rect.x>530 and protagonista.rect.x<610 and protagonista.rect.y>100 and protagonista.rect.y<190 and escenaMarte1_2==True):
        Interaccion = "???"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(975,760))
        interactuar = True
        if(hacer==True):
            cartaMarte1=True

    if(protagonista.rect.x>505 and protagonista.rect.x<590 and protagonista.rect.y>465 and protagonista.rect.y<540 and escenaMarte1_3==True and cogerPieza==False):
        Interaccion = "Pulse e para coger la pieza"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            pieza+=1
            cogerPieza=True

    if(protagonista.rect.x>325 and protagonista.rect.x<385 and protagonista.rect.y>235 and protagonista.rect.y<300 and escenaMarte1_4==True):
        if(paraiso==True):
            Interaccion = "???"
            Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(Transmitir,(975,760))
            interactuar=True
            if(hacer==True):
                cartaMarte2=True

    if(protagonista.rect.x>240 and protagonista.rect.x<510 and protagonista.rect.y>10 and protagonista.rect.y<250 and escenaMarte1_4==True):
        if(paraiso==True):
            Interaccion = "Pulse e para entrar a la cueva"
            Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(Transmitir,(830,760))
            interactuar=True
            if(hacer==True):
                entrarParaiso=True 

        else:
            Interaccion = "No deberias de entrar"
            Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(Transmitir,(870,760))
    return interactuar,bidones,vida,pieza,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso
#Funcion para gestionar las interacciones en marte en la fila central
def interaccionesMarteCentro(protagonista,interactuar,hacer,escenaMarte2_1,escenaMarteCentro,escenaMarte2_4,vida,piezas,cogerPiezaExtra1,cogerPiezaExtra2,estadoInicial):
    if(protagonista.rect.x>65 and protagonista.rect.x<155 and protagonista.rect.y>535 and protagonista.rect.y<635 and escenaMarte2_1==True and cogerPiezaExtra1==False):
        Interaccion = "Pulse e para coger la pieza"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar = True
        if(hacer==True):
            piezas+=1
            cogerPiezaExtra1 = True
    if(protagonista.rect.x>35 and protagonista.rect.x<115 and protagonista.rect.y>380 and protagonista.rect.y<460 and escenaMarteCentro==True):
        Interaccion = "Pulse e para recuperar vida"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(vida>100):
            vida = 100
        if(hacer==True and vida<100):
            if(generadorAgua==True):
                vida+=20
            else:
                vida+=10

    if(protagonista.rect.x>475 and protagonista.rect.x<540 and protagonista.rect.y>550 and protagonista.rect.y<580 and escenaMarteCentro==True):
        Interaccion = "Pulse e para entrar a la nave"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            estadoInicial=True
            escenaMarteCentro=False
            interactuar = False

    if(protagonista.rect.x>95 and protagonista.rect.x<205 and protagonista.rect.y>575 and protagonista.rect.y<665 and escenaMarte2_4==True and cogerPiezaExtra2==False):
        Interaccion = "Pulse e para coger la pieza"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            piezas+=1
            cogerPiezaExtra2 = True

    if(protagonista.rect.x>665 and protagonista.rect.x<720 and protagonista.rect.y>305 and protagonista.rect.y<365 and escenaMarte2_4==True):
        Interaccion = "Pulse e para recuperar vida"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        if(vida>100):
            vida=100
        interactuar=True
        if(hacer==True):
            if(generadorAgua==True):
                vida+=20
            else:
                vida+=10
                
    return interactuar,vida,piezas,cogerPiezaExtra1,cogerPiezaExtra2,estadoInicial,escenaMarteCentro
#Funcion para gestionar las interacciones de la fila de abajo de marte
def interaccionesMarteAbajo(protagonista,interactuar,hacer,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,vida,piezas,cogerPiezaExtra3):
    
    if(protagonista.rect.x>80 and protagonista.rect.x<180 and protagonista.rect.y>605 and protagonista.rect.y<665 and escenaMarte3_1==True):
        Interaccion = "Pulse e para recuperar vida"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(vida>100):
            vida=100
        if(hacer==True and vida<100):
            if(generadorAgua==True):
                vida+=20
            else:
                vida+=10
    
    if(protagonista.rect.x>550 and protagonista.rect.x<640 and protagonista.rect.y>355 and protagonista.rect.y<445 and escenaMarte3_2==True and cogerPiezaExtra3==False):
        Interaccion = "Pulse e para coger la pieza"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar = True
        if(hacer==True):
            piezas+=1
            cogerPiezaExtra3=True

    return interactuar,vida,piezas,cogerPiezaExtra3
#Funcion encargada del fin del planeta marte
def TerminarMisionMarte(generadorAgua,terminarMarte,generadorDeAgua):
    if(generadorAgua==True and terminarMarte==False):
        teclaPulsada = pygame.key.get_pressed()
        generadorDeAgua.draw(screen)
        if(teclaPulsada[pygame.K_RETURN]):
            terminarMarte=True
    return terminarMarte,generadorAgua
#Funcion encargada del primer secreto de marte
def primeraCarta(cartaMarte1,cartaSecretaMarte,paraiso,vida,soporteVital):
    teclaPulsada = pygame.key.get_pressed()
    if(cartaMarte1==True):
        paraiso=True
        cartaSecretaMarte.draw(screen)
        if(soporteVital==True):
            vida+=0.003
        else:
            vida+=0.01
        if(teclaPulsada[pygame.K_RETURN]):
            cartaMarte1=False
    return cartaMarte1,paraiso,vida
#Funcion encargada del segundo secreto de marte
def segundaCarta(cartaMarte2,cartaSecretaMarte2,vida,soporteVital):
    teclaPulsada = pygame.key.get_pressed()
    if(cartaMarte2==True):
        cartaSecretaMarte2.draw(screen)
        if(soporteVital==True):
            vida+=0.003
        else:
            vida+=0.01
        if(teclaPulsada[pygame.K_RETURN]):
            cartaMarte2=False
    return cartaMarte2,vida
#Funcion para cambiar de escena en el paraiso
def cambiarEscenaParaiso(protagonista,entradaParaiso,paraisoCentral):
    if(protagonista.rect.y<-10 and entradaParaiso == True):
        paraisoCentral=True
        entradaParaiso=False
        protagonista.rect.y = 780
    if(protagonista.rect.y>790 and paraisoCentral == True):
        entradaParaiso=True
        paraisoCentral=False
        protagonista.rect.y = 10
    return entradaParaiso,paraisoCentral
#Funcion para las colisiones en el paraiso
def colisionesParaiso(protagonista,entradaParaiso,ParaisoCentral):
    if(entradaParaiso==True):
        if(protagonista.rect.x>750):
            protagonista.rect.x=740
        if(protagonista.rect.x<0):
            protagonista.rect.x=10
        if(protagonista.rect.y>750):
            protagonista.rect.y=740
    if(ParaisoCentral==True):
        if(protagonista.rect.x>750):
            protagonista.rect.x=740
        if(protagonista.rect.x<0):
            protagonista.rect.x=10
        if(protagonista.rect.y<0):
            protagonista.rect.y=10
        if(protagonista.rect.x>250 and protagonista.rect.x<255 and protagonista.rect.y>0 and protagonista.rect.y<100):
            protagonista.rect.x=240
        if(protagonista.rect.x>450 and protagonista.rect.x<455 and protagonista.rect.y>0 and protagonista.rect.y<100):
            protagonista.rect.x=460
        if(protagonista.rect.y>95 and protagonista.rect.y<100 and protagonista.rect.x>250 and protagonista.rect.x<450):
            protagonista.rect.y=110
#Funcion para gestionar las interacciones en el paraiso
def interaccionesParaiso(protagonista,interactuar,hacer,cogerPrimerMensajeParaiso,cogerSegundoMensajeParaiso,pase,cogerSoporteVital,entrarParaiso,entradaParaiso,ParaisoCentral,vida,soporteVital):
    if(protagonista.rect.x>460 and protagonista.rect.x<540 and protagonista.rect.y>130 and protagonista.rect.y<210 and entradaParaiso==True):
        Interaccion = "???"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            cogerPrimerMensajeParaiso=True
    if(protagonista.rect.x>290 and protagonista.rect.x<475 and protagonista.rect.y>580 and protagonista.rect.y<750 and entradaParaiso==True):
        Interaccion = "Pulse e para salir del paraiso"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar = True
        if(hacer==True):
            entrarParaiso=False
    if(protagonista.rect.x>240 and protagonista.rect.x<320 and protagonista.rect.y>50 and protagonista.rect.y<140 and ParaisoCentral==True):
        Interaccion = "???"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            cogerSegundoMensajeParaiso=True
            pase = True
    if(soporteVital==False):
        if(protagonista.rect.x>230 and protagonista.rect.x<480 and protagonista.rect.y>0 and protagonista.rect.y<120 and ParaisoCentral==True and pase==True):
            Interaccion = "Pulse e para registrar el cadaver"
            Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
            screen.blit(Transmitir,(830,760))
            interactuar=True
            if(hacer==True and pase==True):
                cogerSoporteVital=True
                pase = False
    if(protagonista.rect.x>90 and protagonista.rect.x<190 and protagonista.rect.y>250 and protagonista.rect.y<315 and ParaisoCentral==True):
        Interaccion = "Pulse e para recuperar vida"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(vida>100):
            vida=100
        if(hacer==True and vida<100):
            vida+=10
    return interactuar,cogerPrimerMensajeParaiso,cogerSegundoMensajeParaiso,cogerSoporteVital,entrarParaiso,vida,pase,soporteVital
#Funcion para mostrar el primer mensaje del paraiso
def primerMensajeParaiso(mensaje1Paraiso,cogerPrimerMensajeParaiso,vida,soporteVital):
    if(cogerPrimerMensajeParaiso==True):
        teclaPulsada = pygame.key.get_pressed()
        mensaje1Paraiso.draw(screen)
        if(soporteVital==True):
            vida+=0.003
        else:
            vida+=0.01
        if(teclaPulsada[pygame.K_RETURN]):
            cogerPrimerMensajeParaiso=False
    return cogerPrimerMensajeParaiso,vida
#Funcion para mostrar el segundo mensaje del paraiso
def segundoMensajeParaiso(mensaje2Paraiso,cogerSegundoMensajeParaiso,vida,soporteVital):
    if(cogerSegundoMensajeParaiso==True):
        teclaPulsada = pygame.key.get_pressed()
        mensaje2Paraiso.draw(screen)
        if(soporteVital==True):
            vida+=0.003
        else:
            vida+=0.01
        if(teclaPulsada[pygame.K_RETURN]):
            cogerSegundoMensajeParaiso=False
    return cogerSegundoMensajeParaiso,vida
#Funcion para mostrar y adquirir el soporte vital
def adquirirSoporteVital(mensajeSoporteVital,cogerSoporteVital,soporteVital,piezas):
    if(cogerSoporteVital==True and soporteVital==False):
        teclaPulsada = pygame.key.get_pressed()
        mensajeSoporteVital.draw(screen)
        if(teclaPulsada[pygame.K_RETURN]):
            cogerSoporteVital=False
            soporteVital=True
            piezas+=2
    return soporteVital,cogerSoporteVital,piezas  
#Funcion para cambiar de escena en jupiter
def cambiarEscenaJupiter(naveMov,escenaEspacio,escenaEspacio2,escenaZonaJupiter):
    if(naveMov.rect.x<20 and escenaEspacio==True):
        escenaEspacio2=True
        escenaEspacio=False
        naveMov.rect.x = 750
    if(naveMov.rect.x>760 and escenaEspacio2==True):
        escenaEspacio=True
        escenaEspacio2=False
        naveMov.rect.x=30
    if(naveMov.rect.x<20 and escenaEspacio2==True):
        escenaZonaJupiter=True
        escenaEspacio2=False
        naveMov.rect.x=750
    if(naveMov.rect.x>760 and escenaZonaJupiter==True):
        escenaEspacio2=True
        escenaZonaJupiter=False
        naveMov.rect.x=30
    return escenaEspacio,escenaEspacio2,escenaZonaJupiter
#Funcion para crear el primer meteorito
def crearMeteoritoSimple(spritesJuego):
    meteorito = pygame.sprite.Sprite()

    meteorito.image = pygame.image.load("meteorito1.png")
    meteorito.rect = meteorito.image.get_rect()

    meteorito.rect.x = 550
    meteorito.rect.y=0

    spritesJuego.add(meteorito)

    return meteorito
#Funcion para crear el segundo meteorito
def crearMeteoritoAlargado(spritesJuego):
    meteorito = pygame.sprite.Sprite()

    meteorito.image = pygame.image.load("meteorito2.png")
    meteorito.rect = meteorito.image.get_rect()

    meteorito.rect.x = 350
    meteorito.rect.y=0

    spritesJuego.add(meteorito)

    return meteorito
#Funcion para crear el tercer meteorito
def crearMeteoritoAncho(spritesJuego):
    meteorito = pygame.sprite.Sprite()

    meteorito.image = pygame.image.load("meteorito3.png")
    meteorito.rect = meteorito.image.get_rect()

    meteorito.rect.x = 150
    meteorito.rect.y=0

    spritesJuego.add(meteorito)

    return meteorito
#Funcion para crear el cuarto meteorito
def crearMeteoritoGrande(spritesJuego):
    meteorito = pygame.sprite.Sprite()

    meteorito.image = pygame.image.load("meteoritoGrande.png")
    meteorito.rect = meteorito.image.get_rect()

    meteorito.rect.x = 200
    meteorito.rect.y=0

    spritesJuego.add(meteorito)

    return meteorito
#Funcion que controla el movimiento de los meteoritos
def movimientoMeteorito(meteoritoSimple,meteoritoLargo,meteoritoAncho,meteoritoGrande):
    if(escenaEspacio==True):
        meteoritoSimple.rect.y+=4
        meteoritoLargo.rect.y+=3
        meteoritoAncho.rect.y+=2
    if(escenaEspacio2==True):
        meteoritoGrande.rect.y+=2
    if(meteoritoSimple.rect.y>790):
        meteoritoSimple.rect.y=-40
    if(meteoritoLargo.rect.y>790):
        meteoritoLargo.rect.y=-40
    if(meteoritoAncho.rect.y>790):
        meteoritoAncho.rect.y=-40
    if(meteoritoGrande.rect.y>790):
        meteoritoGrande.rect.y=-40
#Funcion que gestiona las colisiones de los meteoritos y la nave
def colisionesConMeteorito(pintarNaveMovimiento,meteoritoSimple,meteoritoAlargado,meteoritoGrande,arreglos):
    if(escenaEspacio==True):
        if(pintarNaveMovimiento.rect.y>meteoritoSimple.rect.y-20 and pintarNaveMovimiento.rect.y<(meteoritoSimple.rect.y+60) and pintarNaveMovimiento.rect.x>510 and pintarNaveMovimiento.rect.x<630):
            arreglos-=15
            meteoritoSimple.rect.y = -40
        if(pintarNaveMovimiento.rect.y>meteoritoAlargado.rect.y-20 and pintarNaveMovimiento.rect.y<(meteoritoAlargado.rect.y+105) and pintarNaveMovimiento.rect.x>295 and pintarNaveMovimiento.rect.x<405):
            arreglos-=25
            meteoritoAlargado.rect.y = -40
        if(pintarNaveMovimiento.rect.y>meteoritoAncho.rect.y-20 and pintarNaveMovimiento.rect.y<(meteoritoAncho.rect.y+85) and pintarNaveMovimiento.rect.x>80 and pintarNaveMovimiento.rect.x<240):
            arreglos-=40
            meteoritoAncho.rect.y = -40
    if(escenaEspacio2==True):
        if(pintarNaveMovimiento.rect.y>meteoritoGrande.rect.y-20 and pintarNaveMovimiento.rect.y<(meteoritoGrande.rect.y+300) and pintarNaveMovimiento.rect.x>200 and pintarNaveMovimiento.rect.x<500):
            arreglos-=60
            meteoritoGrande.rect.y = -40
    return arreglos
#Funcion para las colisiones de la nave con los bordes
def colisionesNave(pintarNaveMovimiento):
    if(escenaEspacio==True):
        if(pintarNaveMovimiento.rect.x>736):
            pintarNaveMovimiento.rect.x = 726
    if(escenaZonaJupiter==True):
        if(pintarNaveMovimiento.rect.x<300):
            pintarNaveMovimiento.rect.x = 310
    if(pintarNaveMovimiento.rect.y<0):
        pintarNaveMovimiento.rect.y = 10
    if(pintarNaveMovimiento.rect.y>736):
        pintarNaveMovimiento.rect.y = 726
#Funcion para mostrar la decision en jupiter
def pintarDecisionJupiter(escenaZonaJupiter,pintarNaveMovimiento,decisionJupiter,decidir,decision):
    if(decision==False):
        if(pintarNaveMovimiento.rect.x<340 and escenaZonaJupiter==True):
            teclaPulsada = pygame.key.get_pressed()
            decisionJupiter.draw(screen)
            if(teclaPulsada[pygame.K_1] or teclaPulsada[pygame.K_KP1]):
                decision=1
                decidir=True
            elif(teclaPulsada[pygame.K_2] or teclaPulsada[pygame.K_KP2]):
                decision=2
                decidir=True
            elif(teclaPulsada[pygame.K_3] or teclaPulsada[pygame.K_KP3]):
                decision=3
                decidir=True
    return decidir,decision
#Funcion para recoger el cristal si se ha elejido la opcion correcta
def pintarCristalAtmosfera(cristalAtmosfera,cogerCristal,decision):
    if(decision==2 and cogerCristal==False):
        cristalAtmosfera.draw(screen)
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            cogerCristal=True
    return cogerCristal
#Funcion para recoger el distribuidor de energia si se ha elegido la opcion correcta
def pintarDistribuidorEnergia(distribuidorEnergia,cogerCristal,cogerDistribuidor,distribuidorDeEnergia,terminarJupiter):
    if(cogerDistribuidor==True and distribuidorDeEnergia==False):
        distribuidorEnergia.draw(screen)
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            cogerDistribuidor = False
            distribuidorDeEnergia = True
            terminarJupiter=True
            cogerCristal=False
    return cogerDistribuidor,distribuidorDeEnergia,cogerCristal,terminarJupiter
#Funcion para cambiar de escena en urano
def cambiarEscenaUrano(protagonista,escenaUranoCentro,escenaUranoInterseccion,escenaUranoArriba,escenaUranoAbajo):
    #Cambios escena central
    if(protagonista.rect.x>760 and escenaUranoCentro==True):
        escenaUranoInterseccion=True
        escenaUranoCentro=False
        protagonista.rect.x=20
    #Cambios escena cruce
    if(protagonista.rect.x<20 and escenaUranoInterseccion==True):
        escenaUranoCentro=True
        escenaUranoInterseccion=False
        protagonista.rect.x = 750
    if(protagonista.rect.y>760 and escenaUranoInterseccion==True):
        escenaUranoAbajo=True
        escenaUranoInterseccion=False
        protagonista.rect.y = 20
    if(protagonista.rect.y<10 and escenaUranoInterseccion==True):
        escenaUranoArriba=True
        escenaUranoInterseccion=False
        protagonista.rect.y = 750
    #Cambios escena arriba
    if(protagonista.rect.y>760 and escenaUranoArriba==True):
        escenaUranoInterseccion = True
        escenaUranoArriba = False
        protagonista.rect.y = 20
    #Cambios escena abajo
    if(protagonista.rect.y<10 and escenaUranoAbajo==True):
        escenaUranoInterseccion = True
        escenaUranoAbajo=False
        protagonista.rect.y = 750
    return escenaUranoCentro,escenaUranoInterseccion,escenaUranoArriba,escenaUranoAbajo
#Funcion que gestiona las colisiones con los bordes de urano
def colisionesUrano(protagonista,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior):
    if(escenaUranoCentro==True):
        if(protagonista.rect.y<25):
            protagonista.rect.y = 35
        if(protagonista.rect.y>710):
            protagonista.rect.y = 700
        if(protagonista.rect.x<25):
            protagonista.rect.x = 35
    if(escenaUranoInterseccion==True):
        if(protagonista.rect.x>710):
            protagonista.rect.x = 700
    if(escenaUranoInferior==True):
        if(protagonista.rect.x>710):
            protagonista.rect.x = 700
        if(protagonista.rect.x<25):
            protagonista.rect.x = 35
        if(protagonista.rect.y>710):
            protagonista.rect.y = 700
    if(escenaUranoSuperior==True):
        if(protagonista.rect.x>710):
            protagonista.rect.x = 700
        if(protagonista.rect.x<25):
            protagonista.rect.x = 35
        if(protagonista.rect.y<25):
            protagonista.rect.y = 35 
#Funcion que gestiona las interacciones en urano 
def interaccionesUrano(protagonista,interactuar,hacer,escenaUranoCentro,escenaUranoInterseccion,escenaUranoInferior,EscenaUranoSuperior,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial):
    #Escena centro
    if(protagonista.rect.x>120 and protagonista.rect.x<190  and protagonista.rect.y<285 and escenaUranoCentro==True):
        Interaccion = "Pulse e para entrar a la nave"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            estadoInicial=True
            escenaUranoCentro=False

    if(protagonista.rect.x>55 and protagonista.rect.x<140 and protagonista.rect.y>520 and protagonista.rect.y<595 and escenaUranoCentro==True):
        Interaccion = "Pulse e para entrar en calor"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar = True
        if(vida>100):
            vida = 100
        if(hacer==True and vida<100):
            if(generadorAgua==True):
                vida+=20
            else:
                vida+=10

    #Escena cruce
    if(protagonista.rect.x>540 and protagonista.rect.x<625 and protagonista.rect.y>160 and protagonista.rect.y<230 and escenaUranoInterseccion==True and cogerPieza==False):
        Interaccion = "Pulse e para coger la pieza"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar = True
        if(hacer==True):
            piezas+=1
            cogerPieza=True

    if(protagonista.rect.x>(pintarBolaHidrogeno.rect.x-70) and protagonista.rect.x<(pintarBolaHidrogeno.rect.x+70) and protagonista.rect.y>pintarBolaHidrogeno.rect.y-70 and protagonista.rect.y<pintarBolaHidrogeno.rect.y+70 and escenaUranoInterseccion==True and contadorEspera<=0):
        Interaccion = "Pulse e para coger hidrogeno"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            cogerHidrogeno=True
            hidrogeno+=1

    #Escena arriba
    if(protagonista.rect.x>325 and protagonista.rect.x<430 and protagonista.rect.y>115 and protagonista.rect.y<195 and EscenaUranoSuperior==True and cogerBidon==False):
        Interaccion = "Pulse e para coger el bidon"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            bidones+=1
            cogerBidon=True

    if(protagonista.rect.x>(pintarBolaHidrogeno.rect.x-70) and protagonista.rect.x<(pintarBolaHidrogeno.rect.x+70) and protagonista.rect.y>pintarBolaHidrogeno.rect.y-70 and protagonista.rect.y<pintarBolaHidrogeno.rect.y+70 and escenaUranoInferior==True and contadorEspera<=0):
        Interaccion = "Pulse e para coger hidrogeno"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            cogerHidrogeno=True
            hidrogeno+=1

    #Escena abajo
    if(protagonista.rect.x>315 and protagonista.rect.x<430 and protagonista.rect.y>480 and protagonista.rect.y<570 and escenaUranoInferior==True):
        Interaccion = "Pulse e para entrar en calor"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(vida>100):
            vida = 100
        if(hacer==True and vida<100):
            if(generadorAgua==True):
                vida+=20
            else:
                vida+=10

    if(protagonista.rect.x>(pintarBolaHidrogeno.rect.x-70) and protagonista.rect.x<(pintarBolaHidrogeno.rect.x+70) and protagonista.rect.y>pintarBolaHidrogeno.rect.y-70 and protagonista.rect.y<pintarBolaHidrogeno.rect.y+70 and escenaUranoSuperior==True and contadorEspera<=0):
        Interaccion = "Pulse e para coger hidrogeno"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(hacer==True):
            cogerHidrogeno=True
            hidrogeno+=1

    return interactuar,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial,escenaUranoCentro
#Funcion que gestiona l aparicion de los globos de hidrogeno
def mostrarHidrogeno(bolaHidrogeno,pintarBolaHidrogeno,cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior):
    if(cogerHidrogeno==True):
        pintarBolaHidrogeno.rect.x = random.randint(100,600)
        pintarBolaHidrogeno.rect.y = random.randint(100,600)
        contadorHidrogeno=5000
        contadorEspera=10000
        cogerHidrogeno=False
    if(contadorEspera>=0):
        contadorEspera-=9

    else:
        contadorHidrogeno-=9
        bolaHidrogeno.draw(screen)
    if(contadorHidrogeno<=0):
        pintarBolaHidrogeno.rect.x = random.randint(100,600)
        pintarBolaHidrogeno.rect.y = random.randint(100,600)
        contadorHidrogeno=5000
        contadorEspera=7000
    return cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera
#Funcion para mostrar el traje antipresion
def mostrarTrajeAP(trajeAntiPresion,cogerTrajeAntiPresion,trajeAP):
    if(cogerTrajeAntiPresion==True and trajeAP==False):
        trajeAntiPresion.draw(screen)
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            trajeAP = True
            cogerTrajeAntiPresion = False
    return cogerTrajeAntiPresion,trajeAP
#Funcion encargada de disparar
def disparar(protagonista,cargador,dispararBala,disparo,balas):
    teclaPulsada = pygame.key.get_pressed()
    if(disparo==False):
        if(balas>0):
            if(teclaPulsada[pygame.K_q] or teclaPulsada[pygame.K_SPACE]):
                dispararBala.rect.x=protagonista.rect.x
                dispararBala.rect.y=protagonista.rect.y
                disparo=True
                balas-=1
    if(disparo==True):
        cargador.draw(screen)
        dispararBala.rect.y-=10
        if(dispararBala.rect.y<0):
            disparo=False
    return disparo,balas
#Funcion para cambiar de escena en pluton
def cambiarEscenaPluton(protagonista,escenaPlutonCentral,escenaPlutonJefeFinal):
    if(protagonista.rect.y<-10 and escenaPlutonCentral==True):
        escenaPlutonJefeFinal=True
        escenaPlutonCentral=False
        protagonista.rect.y = 750
    if(protagonista.rect.y>760 and escenaPlutonJefeFinal==True):
        protagonista.rect.y=750
    return escenaPlutonCentral,escenaPlutonJefeFinal

def combate(protagonista,antagonista,vidaJefe,dispararBala,disparo,contadorDisparo,disparoMaligno,balaOscura,pintarBalaOscura,vida,miraEspecial,explosionEspecial,pintarMira,pintarExplosion,ataqueEspecial,contadorAtaqueEspecial,contadorMira,contadorExplosion):
    if(contadorDisparo<=0):
        if(vidaJefe<=101 and vidaJefe>60):
            if(antagonista.rect.x<10):
                antagonista.velocidad_x=1
            elif(antagonista.rect.x>667):
                antagonista.velocidad_x=-1
            elif(antagonista.rect.x>protagonista.rect.x-56 and antagonista.rect.x<protagonista.rect.x+56):
                antagonista.velocidad_x=0
                contadorDisparo=2000
        if(vidaJefe<60 and vidaJefe>30):
            if(antagonista.rect.x<10):
                antagonista.velocidad_x=1
            elif(antagonista.rect.x>667):
                antagonista.velocidad_x=-1
            elif(antagonista.rect.x>protagonista.rect.x-56 and antagonista.rect.x<protagonista.rect.x+56):
                antagonista.velocidad_x=0
                contadorDisparo=1500
        if(vidaJefe>=0 and vidaJefe<30):
            if(antagonista.rect.x<10):
                antagonista.velocidad_x=1
            elif(antagonista.rect.x>667):
                antagonista.velocidad_x=-1
            elif(antagonista.rect.x>protagonista.rect.x-56 and antagonista.rect.x<protagonista.rect.x+56):
                antagonista.velocidad_x=0
                contadorDisparo=1300
            
            
    else:
        contadorDisparo-=9
        if(contadorDisparo>1000 and contadorDisparo<1200 and disparoMaligno==False):
                disparoMaligno=True
                pintarBalaOscura.rect.x=protagonista.rect.x+20
                pintarBalaOscura.rect.y=antagonista.rect.y
        if(contadorDisparo<=0):
            numero = random.randint(1,2)
            
            if(numero==1):
                    antagonista.velocidad_x = 1
            else:
                
                    antagonista.velocidad_x = -1
            
    if(disparoMaligno==True):
        balaOscura.draw(screen)
        if(vidaJefe<30):
            pintarBalaOscura.rect.y+=30
        else:
            pintarBalaOscura.rect.y+=20
        if(pintarBalaOscura.rect.y>790):
            disparoMaligno=False
            pintarBalaOscura.rect.y = 1000
    if(dispararBala.rect.y>(antagonista.rect.y) and dispararBala.rect.y<(antagonista.rect.y+145) and dispararBala.rect.x>(antagonista.rect.x-10) and dispararBala.rect.x<(antagonista.rect.x+143)):
        disparo=False
        vidaJefe-=1
        dispararBala.rect.y = -50
    if(pintarBalaOscura.rect.y>(protagonista.rect.y) and pintarBalaOscura.rect.y<(protagonista.rect.y+56) and pintarBalaOscura.rect.x>(protagonista.rect.x-20) and pintarBalaOscura.rect.x<(protagonista.rect.x+40)):
        vida-=15
        pintarBalaOscura.rect.y = 1000
    if(vidaJefe<60 and vidaJefe>30):
        
        if(contadorAtaqueEspecial<=0):
            ataqueEspecial=True
        else:
            contadorAtaqueEspecial-=9
        if(ataqueEspecial==True):
            contadorMira=4000
            contadorExplosion=2000
            ataqueEspecial=False
            contadorAtaqueEspecial=20000
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
                if(pintarExplosion.rect.x>(protagonista.rect.x-56) and pintarExplosion.rect.x<(protagonista.rect.x+56) and pintarExplosion.rect.y>(protagonista.rect.y-56)and pintarExplosion.rect.y<(protagonista.rect.y+56)):
                    vida-=50
    if(vidaJefe<30):
        if(contadorAtaqueEspecial<=0):
            ataqueEspecial=True
        else:
            contadorAtaqueEspecial-=9
        if(ataqueEspecial==True):
            contadorMira=3000
            contadorExplosion=1500
            ataqueEspecial=False
            contadorAtaqueEspecial=10000
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
                if(pintarExplosion.rect.x>(protagonista.rect.x-56) and pintarExplosion.rect.x<(protagonista.rect.x+56) and pintarExplosion.rect.y>(protagonista.rect.y-56)and pintarExplosion.rect.y<(protagonista.rect.y+56)):
                    vida-=50
                    pintarExplosion.rect.y=1000
    
    Interaccion = "Vida jefe "+str(vidaJefe)
    Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
    screen.blit(Transmitir,(830,760))
        


    return contadorDisparo,disparoMaligno,vidaJefe,disparo,vida,ataqueEspecial,contadorAtaqueEspecial,contadorMira,contadorExplosion

def suministrosEmergencia(protagonista,vida,balas,interactuar,hacer,pintarMedicamentos,medicamentosEspeciales):
    if(vida<50):
        pintarMedicamentos.rect.x = 400
        pintarMedicamentos.rect.y = 400
        medicamentosEspeciales.draw(screen)
    if(protagonista.rect.x>350 and protagonista.rect.x<480 and protagonista.rect.y>350 and protagonista.rect.y<480 and vida<50):
        Interaccion = "Pulsa e para abastecerte"
        Transmitir = fraseIteraccion.render(Interaccion,1,blanco)
        screen.blit(Transmitir,(830,760))
        interactuar=True
        if(vida>100):
            vida=100
        if(balas>100):
            balas=100
        if(hacer==True):
            vida+=40
            balas+=30
    return interactuar,vida,balas
       
#Variables exclusivas para la ventana de juego
ancho = 900
largo = 600
#Colores
negro = pygame.Color(0,0,0)
blanco = pygame.Color(255,255,255)
rojo = pygame.Color(255,0,0)
verde = pygame.Color(0,255,0)
azul = pygame.Color(0,0,255)
naranja = pygame.Color(255,120,0)
dorado = pygame.Color(212,175,55)
bidonGasofa = pygame.Color(149,49,21)
gris = pygame.Color(155,155,155)
#Inicializamos pygame
pygame.init()
screen = pygame.display.set_mode((ancho,largo))
pygame.display.set_caption('Solar Adventures')
contador = 5000
omitir = False
cambio = False
#Escena nave
escenaNaveCentro = True
escenaNaveIzquierda = False
escenaNaveAbajo = False
#Escenas luna
escenaLunaCentro = False
escenaLunaIzquierda = False
escenaLunaArriba = False
escenaLunaAbajo = False
escenaLunaArribaIzquierda = False
escenaLunaArribaDerecha = False
#Escenas marte
escenaMarteCentro = False
escenaMarte1_1 = False
escenaMarte1_2 = False
escenaMarte1_3 = False
escenaMarte1_4 = False
escenaMarte2_1 = False
escenaMarte2_3 = False
escenaMarte3_1 = False
escenaMarte3_2 = False
escenaMarte3_3 = False
escenaMarte2_4 = False
#Escenas jupiter
escenaEspacio = False
escenaEspacio2 = False
escenaZonaJupiter = False
decidir = False
decision = 0
#Escenas Urano
escenaUranoCentro = False
escenaUranoInterseccion = False
escenaUranoInferior = False
escenaUranoSuperior = False
hidrogeno = 0
cogerHidrogeno = False
contadorHidrogeno = 0
contadorEspera = 0
#escenas Pluton
escenaPlutonCentral = False
escenaPlutonJefeFinal = False
vidaJefe = 100
entrar = True
contadorDisparo = 0
contadorAtaqueEspecial = 0
ataqueEspecial = False
contadorMira = 0
contadorExplosion = 0
disparoMaligno = False
#Interacciones 
interactuar = False
hacer = False
cogerBidon = False
cogerBidonExtra = False
cogerPieza = False
cogerPiezaExtra1 = False
cogerPiezaExtra2 = False
cogerPiezaExtra3 = False
balas = 0
disparo=False
gasolina = 500
arreglos = 100
bidones = 0
piezas = 0
vida = 100
cambiarMapa = False
volver = False
cambiarNave = False
#Requisitos misiones
cogerPropulsor = True
reunirPiezas = False
generadorAgua = False
terminarMarte = False
cogerCristal = False
cogerDistribuidor = False
distribuidorDeEnergia = False
terminarJupiter = False 
reunirHidrogeno = False
cogerTrajeAntiPresion = False
trajeAP = False
terminarUrano = False
#Secretos
encontrarSecretoLuna = False
inyectorGasolina = False
cartaMarte1 = False
cartaMarte2 = False
paraiso=False
entrarParaiso = False
entradaParaiso = False
ParaisoCentral = False
soporteVital = False
cogerSoporteVital = False
cogerPrimerMensajeParaiso = False
cogerSegundoMensajeParaiso = False
pase = False
#Planetas disponibles
estadoInicial = False
luna = False
marte = False
jupiter = False
saturno = False
urano = False
neptuno = False
pluton = False
infoNivel = False
#Fin de juego 
gameOverVida=False
gameOverGasolina=False
gameOverArreglos=False
gameOverBossFinal=False
gameOverJupiter=False
#Sprites
estadisticas = pygame.sprite.Group()
SpriteNave1 = pygame.sprite.Group()
SpriteNave2 = pygame.sprite.Group()
SpriteNave3 = pygame.sprite.Group()
astronauta = pygame.sprite.Group()
astronautaEnPlaneta = pygame.sprite.Group()
naveMovimiento = pygame.sprite.Group()
nave = pygame.sprite.Group()
bidon = pygame.sprite.Group()
pieza = pygame.sprite.Group()
cargador = pygame.sprite.Group()
propulsorLuzLuna = pygame.sprite.Group()
mapaEspacio = pygame.sprite.Group()
flechaSeleccion = pygame.sprite.Group()
#Sprites zona luna
escenaLunaPrincipal = pygame.sprite.Group()
escenaLunaPrincipalIzquierda = pygame.sprite.Group()
escenaLunaPrincipalAbajo = pygame.sprite.Group()
escenaLunaPrincipalArriba = pygame.sprite.Group()
escenaLunaPrincipalArribaIzquierda = pygame.sprite.Group()
escenaLunaSecundariaArribaDerecha = pygame.sprite.Group()
inyector = pygame.sprite.Group()
#Sprites zona marte
escenaMartePrincipal1_1 = pygame.sprite.Group()
escenaMartePrincipal1_2 = pygame.sprite.Group()
escenaMartePrincipal1_3 = pygame.sprite.Group()
escenaMartePrincipal1_4 = pygame.sprite.Group()
escenaMartePrincipal2_1 = pygame.sprite.Group()
escenaMartePrincipalCentro = pygame.sprite.Group()
escenaMartePrincipal2_3 = pygame.sprite.Group()
escenaMartePrincipal2_4 = pygame.sprite.Group()
escenaMartePrincipal3_1 = pygame.sprite.Group()
escenaMartePrincipal3_2 = pygame.sprite.Group()
escenaMartePrincipal3_3 = pygame.sprite.Group()
generadorDeAgua = pygame.sprite.Group()
cartaSecretaMarte = pygame.sprite.Group()
cartaSecretaMarte2 = pygame.sprite.Group()
entradaDelParaiso = pygame.sprite.Group()
ElParaiso = pygame.sprite.Group()
mensaje1Paraiso = pygame.sprite.Group()
mensaje2Paraiso = pygame.sprite.Group()
mensajeSoporteVital = pygame.sprite.Group()
#Sprites zona Jupiter
escenaMeteoritos = pygame.sprite.Group()
escenaMeteoritos2 = pygame.sprite.Group()
escenaJupiter = pygame.sprite.Group()
meteoritos = pygame.sprite.Group()
meteoritoGrande = pygame.sprite.Group()
decisionJupiter = pygame.sprite.Group()
cristalAtmosfera = pygame.sprite.Group()
distribuidorEnergia = pygame.sprite.Group()
#Sprites zona Urano
escenaUranoCentral = pygame.sprite.Group()
escenaUranoCruce = pygame.sprite.Group()
escenaUranoArriba = pygame.sprite.Group()
escenaUranoAbajo = pygame.sprite.Group()
bolaHidrogeno = pygame.sprite.Group()
trajeAntiPresion = pygame.sprite.Group()
#Sprites zona pluton
escenaPlutonCentro = pygame.sprite.Group()
escenaPlutonJefe = pygame.sprite.Group()
jefeFinal = pygame.sprite.Group()
balaOscura = pygame.sprite.Group()
miraEspecial = pygame.sprite.Group()
explosionEspecial = pygame.sprite.Group()
medicamentosEspeciales = pygame.sprite.Group()
#Sprites información 
informacionSol = pygame.sprite.Group()
informacionMercurio = pygame.sprite.Group()
informacionVenus = pygame.sprite.Group()
informacionTierra = pygame.sprite.Group()
informacionMarte = pygame.sprite.Group()
informacionJupiter = pygame.sprite.Group()
informacionSaturno = pygame.sprite.Group()
informacionUrano = pygame.sprite.Group()
informacionNeptuno = pygame.sprite.Group()
informacionPluton = pygame.sprite.Group()
#Fin de juego 
gameOverPorVida =pygame.sprite.Group()
gameOverPorGasolina =pygame.sprite.Group()
gameOverPorJefe =pygame.sprite.Group()
gameOverPorArreglos =pygame.sprite.Group()
gameOverPorJupiter =pygame.sprite.Group()

#Inicialización sprite
#Estadisticas - protagonista - objetos
colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
protagonista = crearAstronauta(astronauta)
protagonistaEnPlaneta = crearAstronautaPlaneta(astronautaEnPlaneta)
pintarNave = crearNave(nave)
pintarNaveMovimiento = crearNaveEnMovimiento(naveMovimiento)
pintarBidon = crearBidonGasofa(bidon)
pintarPieza = crearPiezas(pieza)
pintarPropulsor = propulsorLuz(propulsorLuzLuna)
dispararBala = crearBala(cargador)
#Escenas nave
interiorNave1 = escenaNave1(SpriteNave1)
interiorNave2 = escenaNave2(SpriteNave2)
interiorNave3 = escenaNave3(SpriteNave3)
#Escena mapa
pintarMapa = mapa(mapaEspacio)
pintarFlecha = flecha(flechaSeleccion)
#Informacion planetas
infSol = infoSol(informacionSol)
infMercurio = infoMercurio(informacionMercurio)
infVenus = infoVenus(informacionVenus)
infTierra = infoTierra(informacionTierra)
infMarte = infoMarte(informacionMarte)
infJupiter = infoJupiter(informacionJupiter)
infSaturno = infoSaturno(informacionSaturno)
infUrano = infoUrano(informacionUrano)
infNeptuno = infoNeptuno(informacionNeptuno)
infPluton = infoPluton(informacionPluton)
#Escenas luna
luna1 = escenaLuna1(escenaLunaPrincipal)
luna2 = escenaLuna2(escenaLunaPrincipalIzquierda)
luna3 = escenaLuna3(escenaLunaPrincipalArriba)
luna4 = escenaLuna4(escenaLunaPrincipalAbajo)
luna5 = escenaLuna5(escenaLunaPrincipalArribaIzquierda)
luna6 = escenaLuna6(escenaLunaSecundariaArribaDerecha)
pintarInyector = crearInyector(inyector)
#Escenas marte
#Primera fila
marte1 = crearEscenaMarte1_1(escenaMartePrincipal1_1)
marte2 = crearEscenaMarte1_2(escenaMartePrincipal1_2)
marte3 = crearEscenaMarte1_3(escenaMartePrincipal1_3)
marte4 = crearEscenaMarte1_4(escenaMartePrincipal1_4)
#Segunda fila
marte5 = crearEscenaMarte2_1(escenaMartePrincipal2_1)
marte6 = crearEscenaMarteCentro(escenaMartePrincipalCentro)
marte7 = crearEscenaMarte2_3(escenaMartePrincipal2_3)
marte8 = crearEscenaMarte2_4(escenaMartePrincipal2_4)
#Tercera fila
marte9 = crearEscenaMarte3_1(escenaMartePrincipal3_1)
marte10 = crearEscenaMarte3_2(escenaMartePrincipal3_2)
marte11 = crearEscenaMarte3_3(escenaMartePrincipal3_3)
pintarGenerador = crearGeneradorAgua(generadorDeAgua)
#Secretos marte
cartaSecreta = CrearCartaSecretaMarte(cartaSecretaMarte)
cartaSecreta2 = CrearCartaSecretaMarte2(cartaSecretaMarte2)
pintarEntradaParaiso = CrearPrimeraEscenaParaiso(entradaDelParaiso)
pintarParaiso = CrearElParaiso(ElParaiso)
pintarMensaje1Paraiso = crearPrimerMensajeParaiso(mensaje1Paraiso)
pintarMensaje2Paraiso = crearSegundoMensajeParaiso(mensaje2Paraiso)
pintarSoporteVital = crearSoporteVital(mensajeSoporteVital)
#Escenas jupiter
pintarEscenaMeteoritos = crearEscenaEspacio(escenaMeteoritos)
pintarEscenaMeteoritos2 = crearEscenaEspacio2(escenaMeteoritos2)
pintarEscenaJupiter = crearEscenaEspacioJupiter(escenaJupiter)
meteoritoSimple = crearMeteoritoSimple(meteoritos)
meteoritoAlargado = crearMeteoritoAlargado(meteoritos)
meteoritoAncho = crearMeteoritoAncho(meteoritos)
meteoroGrande = crearMeteoritoGrande(meteoritoGrande)
pintarDecision = crearDecisionJupiter(decisionJupiter)
pintarCristal = crearCristal(cristalAtmosfera)
pintarDistribuidor = crearDistribuidor(distribuidorEnergia)
#Escenas urano
pintarEscenaUranoCentral = crearEscenaCentralUrano(escenaUranoCentral)
pintarEscenaUranoCruce = crearEscenaUranoCruce(escenaUranoCruce)
pintarEscenaUranoArriba = crearEscenaUranoArriba(escenaUranoArriba)
pintarEscenaUranoAbajo = crearEscenaUranoAbajo(escenaUranoAbajo)
pintarBolaHidrogeno = crearBolaHidrogeno(bolaHidrogeno)
pintarTrajeAntiPresion = crearTrajeAntiPresion(trajeAntiPresion)
#Escenas pluton
pintarEscenaCentro = crearEscenaCentralPluton(escenaPlutonCentro)
pintarEscenaJefe = crearEscenaJefePluton(escenaPlutonJefe)
antagonista = crearJefeFinal(jefeFinal)
pintarBalaOscura = crearBalaMaligna(balaOscura)
pintarMira = crearMira(miraEspecial)
pintarExplosion = crearExplosion(explosionEspecial)
pintarMedicamentos = crearMedicamento(medicamentosEspeciales)
#Fin juego
pintarGameOverVida = crearGameOverVida(gameOverPorVida)
pintarGameOverNave = crearGameOverMeteoritos(gameOverPorArreglos)
pintarGameOverGasolina = crearGameOverGasolina(gameOverPorGasolina)
pintarGameOverJupiter = crearGameOverVida(gameOverPorJupiter)
pintarGameOverJefe = crearGameOverJefeFinal(gameOverPorJefe)
#Mensajes
historia = pygame.font.Font(None,50)
frases = pygame.font.Font(None,35)
fraseLarga = pygame.font.Font(None,30)
fraseInteractuar = pygame.font.Font(None,50)
fraseIteraccion = pygame.font.Font(None,35)
fraseMapa = pygame.font.Font(None,30)
#Creamos el booleano que permite que el juego arranque
funcionando = True
#Bucle de la nave principal
while funcionando and estadoInicial==True:
    screen.fill(negro)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            funcionando = False
    #Inicio de la historia
    if(cambio==False):
        HISTORIA()
        cambio = True
        ancho = 1200
        largo = 800
        screen = pygame.display.set_mode((ancho,largo))
    
    #Cambio de la escena de historia a la escena de la nave
    if(cambio==True and cambiarMapa==False):
        #Escena central de la nave
        if(escenaNaveCentro==True and escenaNaveIzquierda==False):
            time.sleep(0.007)
            SpriteNave1.draw(screen)
            escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
            funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
            interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
            colisionNave1(protagonista)
        #Escena de la izquierda de la nave  
        if(escenaNaveIzquierda==True and escenaNaveCentro==False):
            time.sleep(0.007)
            SpriteNave2.draw(screen)
            escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
            funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
            interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
            colisionNave2(protagonista)
        #Escena de abajo de la nave
        if(escenaNaveAbajo==True and escenaNaveCentro==False):
            time.sleep(0.007)
            SpriteNave3.draw(screen)
            escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
            funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
            interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
            colisionNave3(protagonista)
        
        
        #Dibujamos el protagonista, lo actualizamos y dibujamos los mensajes
        astronauta.draw(screen)
        colocarEstadisticas.draw(screen)
        colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
        udapte(protagonista)
        mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
        misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
        pygame.display.flip()
    #Cambio de escena del mapa a la nave
    if(volver == True):
            escenaNaveIzquierda=True
            cambiarMapa=False
            luna=False
            volver=False 
    #Cambio de escena de la nave al mapa 
    elif(cambiarMapa==True):
            mapaEspacio.draw(screen)
            flechaSeleccion.draw(screen)
            escenaNaveAbajo=False
            escenaNaveCentro=False
            escenaNaveIzquierda=False
            time.sleep(0.007)
            luna = True
            volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton  = gestionarEventosMapa(pintarFlecha,volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton)
            colocarEstadisticas.draw(screen)
            colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
            mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
            mensajesMapa(cambiarMapa,pintarFlecha,informacionSol,informacionMercurio,informacionVenus,informacionTierra,informacionMarte,informacionJupiter,informacionSaturno,informacionUrano,informacionNeptuno,informacionPluton)
            misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
            pygame.display.flip()
    

infoNivel=True
cambiarMapa=False
cogerPropulsor = False
gasolina-=15
ancho = 1200
largo = 800
screen = pygame.display.set_mode((ancho,largo))
escenaLunaCentro=True
cambiarNave = True
protagonistaEnPlaneta.rect.x = 575
protagonistaEnPlaneta.rect.y = 470
while funcionando and luna:
    screen.fill(negro)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            funcionando = False
    if(estadoInicial==True):
        if(cambiarMapa==False):
            if(escenaNaveCentro==True and escenaNaveIzquierda==False):
                time.sleep(0.007)
                SpriteNave1.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                colisionNave1(protagonista)
            #Escena de la izquierda de la nave  
            if(escenaNaveIzquierda==True and escenaNaveCentro==False):
                time.sleep(0.007)
                SpriteNave2.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                if(cogerPropulsor==False):
                    cambiarMapa=False
                colisionNave2(protagonista)
            #Escena de abajo de la nave
            if(escenaNaveAbajo==True and escenaNaveCentro==False):
                time.sleep(0.007)
                SpriteNave3.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                colisionNave3(protagonista)
            misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
            astronauta.draw(screen)
            udapte(protagonista)
            colocarEstadisticas.draw(screen)
            colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
            mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
            pygame.display.flip()
        if(volver == True):
            escenaNaveIzquierda=True
            cambiarMapa=False
            luna=True
            marte=False
            volver=False 
        #Cambio de escena de la nave al mapa 
        elif(cambiarMapa==True and cogerPropulsor==True):
            mapaEspacio.draw(screen)
            flechaSeleccion.draw(screen)
            escenaNaveAbajo=False
            escenaNaveCentro=False
            escenaNaveIzquierda=False
            time.sleep(0.007)
            marte = True
            volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton  = gestionarEventosMapa(pintarFlecha,volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton)
            colocarEstadisticas.draw(screen)
            colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
            mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
            misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
            mensajesMapa(cambiarMapa,pintarFlecha,informacionSol,informacionMercurio,informacionVenus,informacionTierra,informacionMarte,informacionJupiter,informacionSaturno,informacionUrano,informacionNeptuno,informacionPluton)
            pygame.display.flip()
        if(estadoInicial==False):
            protagonistaEnPlaneta.rect.x = 575
            protagonistaEnPlaneta.rect.y = 470
            escenaLunaCentro=True
    else:
        #Escena central de la luna
        if(escenaLunaCentro==True):
            time.sleep(0.007)
            escenaLunaPrincipal.draw(screen)
            nave.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionLuna1(protagonistaEnPlaneta)
            colisionConNave(protagonistaEnPlaneta,pintarNave)
            interactuar,estadoInicial,escenaLunaCentro,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna = interaccionesLuna(protagonistaEnPlaneta,interactuar,hacer,escenaLunaCentro,escenaLunaIzquierda,escenaLunaArriba,escenaLunaAbajo,escenaLunaArribaIzquierda,escenaLunaArribaDerecha,estadoInicial,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna)
            escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha=cambiarEscenaLuna(protagonistaEnPlaneta,escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha)
            if(estadoInicial==True):
                protagonista.rect.x=365
                protagonista.rect.y=150
        #Escena izquierda de la luna
        elif(escenaLunaIzquierda==True):
            time.sleep(0.007)
            escenaLunaPrincipalIzquierda.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionLuna2(protagonistaEnPlaneta)
            escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha=cambiarEscenaLuna(protagonistaEnPlaneta,escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha)
        #Escena de abajo de la luna
        elif(escenaLunaAbajo==True):
            time.sleep(0.007)
            escenaLunaPrincipalAbajo.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionLuna3(protagonistaEnPlaneta)
            interactuar,estadoInicial,escenaLunaCentro,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna = interaccionesLuna(protagonistaEnPlaneta,interactuar,hacer,escenaLunaCentro,escenaLunaIzquierda,escenaLunaArriba,escenaLunaAbajo,escenaLunaArribaIzquierda,escenaLunaArribaDerecha,estadoInicial,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna)
            escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha=cambiarEscenaLuna(protagonistaEnPlaneta,escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha)
            if(cogerPieza==False):
                pintarPieza.rect.x = 380
                pintarPieza.rect.y = 605
                pieza.draw(screen)
        #Escena de arriba de la luna
        elif(escenaLunaArriba==True):
            time.sleep(0.007)
            escenaLunaPrincipalArriba.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionLuna4(protagonistaEnPlaneta)
            interactuar,estadoInicial,escenaLunaCentro,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna = interaccionesLuna(protagonistaEnPlaneta,interactuar,hacer,escenaLunaCentro,escenaLunaIzquierda,escenaLunaArriba,escenaLunaAbajo,escenaLunaArribaIzquierda,escenaLunaArribaDerecha,estadoInicial,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna)
            escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha=cambiarEscenaLuna(protagonistaEnPlaneta,escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha)
            if(cogerBidon==False):
                pintarBidon.rect.x = 565
                pintarBidon.rect.y = 620
                bidon.draw(screen)
        #Escena de arriba izquierda de la luna
        elif(escenaLunaArribaIzquierda==True):
            time.sleep(0.007)
            escenaLunaPrincipalArribaIzquierda.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionLuna5(protagonistaEnPlaneta)
            interactuar,estadoInicial,escenaLunaCentro,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna = interaccionesLuna(protagonistaEnPlaneta,interactuar,hacer,escenaLunaCentro,escenaLunaIzquierda,escenaLunaArriba,escenaLunaAbajo,escenaLunaArribaIzquierda,escenaLunaArribaDerecha,estadoInicial,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna)
            escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha=cambiarEscenaLuna(protagonistaEnPlaneta,escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha)
            if(cogerPropulsor == False):
                pintarPropulsor.rect.x = 270
                pintarPropulsor.rect.y = 380
                propulsorLuzLuna.draw(screen)
        #Escena de arriba derecha de la luna
        elif(escenaLunaArribaDerecha==True):
            time.sleep(0.007)
            escenaLunaSecundariaArribaDerecha.draw(screen)
            if(inyectorGasolina==False):
                interactuar,estadoInicial,escenaLunaCentro,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna = interaccionesLuna(protagonistaEnPlaneta,interactuar,hacer,escenaLunaCentro,escenaLunaIzquierda,escenaLunaArriba,escenaLunaAbajo,escenaLunaArribaIzquierda,escenaLunaArribaDerecha,estadoInicial,escenaNaveCentro,cogerPieza,cogerBidon,piezas,bidones,cogerPropulsor,encontrarSecretoLuna)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionLuna6(protagonistaEnPlaneta)
            escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha=cambiarEscenaLuna(protagonistaEnPlaneta,escenaLunaCentro,escenaLunaIzquierda,escenaLunaAbajo,escenaLunaArriba,escenaLunaArribaIzquierda,escenaLunaArribaDerecha)
        #Dibujamos el protagonista, lo actualizamos y cargamos los mensajes 
        astronautaEnPlaneta.draw(screen)
        udapte(protagonistaEnPlaneta)
        disparo,balas = disparar(protagonistaEnPlaneta,cargador,dispararBala,disparo,balas)
        colocarEstadisticas.draw(screen)
        mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
        colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas) 
        encontrarSecretoLuna,inyectorGasolina=secretoLuna(inyector,encontrarSecretoLuna,inyectorGasolina)
        misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
        pygame.display.flip()
    
infoNivel=True
cambiarMapa = False 
estadoInicial = False
volver = False
cogerBidon = False
cogerPieza = False
if(inyectorGasolina==True):
    gasolina-=8
else:
    gasolina-=20
ancho = 1200
largo = 800
screen = pygame.display.set_mode((ancho,largo))
pintarNave.rect.x = 385
pintarNave.rect.y = 320 
protagonistaEnPlaneta.rect.x = 510
protagonistaEnPlaneta.rect.y = 590
cambiarNave = True
escenaMarteCentro = True
while funcionando and marte:
    screen.fill(negro)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            funcionando = False
    if(estadoInicial==True):
        if(cambiarMapa==False):
            if(escenaNaveCentro==True and escenaNaveIzquierda==False):
                time.sleep(0.007)
                SpriteNave1.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                colisionNave1(protagonista)
            #Escena de la izquierda de la nave  
            if(escenaNaveIzquierda==True and escenaNaveCentro==False):
                time.sleep(0.007)
                SpriteNave2.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                colisionNave2(protagonista)
            #Escena de abajo de la nave
            if(escenaNaveAbajo==True and escenaNaveCentro==False):
                time.sleep(0.007)
                SpriteNave3.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                colisionNave3(protagonista)
            misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
            astronauta.draw(screen)
            udapte(protagonista)
            colocarEstadisticas.draw(screen)
            terminarMarte,generadorAgua = TerminarMisionMarte(generadorAgua,terminarMarte,generadorDeAgua)
            colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
            mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
            if(terminarMarte==False):
                cambiarMapa=False 
            pygame.display.flip()
        elif(volver == True):
            escenaNaveIzquierda=True
            cambiarMapa=False
            marte=True
            jupiter=False
            volver=False 
        #Cambio de escena de la nave al mapa 
        elif(cambiarMapa==True and terminarMarte==True):
            mapaEspacio.draw(screen)
            flechaSeleccion.draw(screen)
            escenaNaveAbajo=False
            escenaNaveCentro=False
            escenaNaveIzquierda=False
            time.sleep(0.007)
            jupiter = True
            volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton  = gestionarEventosMapa(pintarFlecha,volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton)
            colocarEstadisticas.draw(screen)
            colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
            mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
            misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
            mensajesMapa(cambiarMapa,pintarFlecha,informacionSol,informacionMercurio,informacionVenus,informacionTierra,informacionMarte,informacionJupiter,informacionSaturno,informacionUrano,informacionNeptuno,informacionPluton)
            pygame.display.flip()
        if(estadoInicial==False):
            protagonistaEnPlaneta.rect.x = 505
            protagonistaEnPlaneta.rect.y = 590
            escenaMarteCentro=True
    elif(entrarParaiso==True):
        if(soporteVital==True):
            vida-=0.005
        else:
            vida-=0.015
        if(entradaParaiso==True):
            time.sleep(0.007)
            entradaDelParaiso.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesParaiso(protagonistaEnPlaneta,entradaParaiso,ParaisoCentral)
            interactuar,cogerPrimerMensajeParaiso,cogerSegundoMensajeParaiso,cogerSoporteVital,entrarParaiso,vida,pase,soporteVital = interaccionesParaiso(protagonistaEnPlaneta,interactuar,hacer,cogerPrimerMensajeParaiso,cogerSegundoMensajeParaiso,pase,cogerSoporteVital,entrarParaiso,entradaParaiso,ParaisoCentral,vida,soporteVital)
            entradaParaiso,ParaisoCentral = cambiarEscenaParaiso(protagonistaEnPlaneta,entradaParaiso,ParaisoCentral)
            if(entrarParaiso==False):
                escenaMarte1_4 = True
                protagonistaEnPlaneta.rect.x=400
                protagonistaEnPlaneta.rect.y=230
        elif(ParaisoCentral==True):
            time.sleep(0.007)
            ElParaiso.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesParaiso(protagonistaEnPlaneta,entradaParaiso,ParaisoCentral)
            interactuar,cogerPrimerMensajeParaiso,cogerSegundoMensajeParaiso,cogerSoporteVital,entrarParaiso,vida,pase,soporteVital = interaccionesParaiso(protagonistaEnPlaneta,interactuar,hacer,cogerPrimerMensajeParaiso,cogerSegundoMensajeParaiso,pase,cogerSoporteVital,entrarParaiso,entradaParaiso,ParaisoCentral,vida,soporteVital)
            entradaParaiso,ParaisoCentral = cambiarEscenaParaiso(protagonistaEnPlaneta,entradaParaiso,ParaisoCentral)
        if(soporteVital==True):
            pase = False
        astronautaEnPlaneta.draw(screen)
        udapte(protagonistaEnPlaneta)
        colocarEstadisticas.draw(screen)
        cogerPrimerMensajeParaiso,vida = primerMensajeParaiso(mensaje1Paraiso,cogerPrimerMensajeParaiso,vida,soporteVital)
        cogerSegundoMensajeParaiso,vida = segundoMensajeParaiso(mensaje2Paraiso,cogerSegundoMensajeParaiso,vida,soporteVital)
        soporteVital,cogerSoporteVital,piezas = adquirirSoporteVital(mensajeSoporteVital,cogerSoporteVital,soporteVital,piezas)
        mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
        colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas) 
        pygame.display.flip()
    else:
        if(soporteVital==True):
            vida-=0.005
        else:
            vida-=0.015
        #Escena fila arriba izquierda
        if(escenaMarte1_1 == True):
            time.sleep(0.007)
            escenaMartePrincipal1_1.draw(screen)
            if(cogerBidon==False):
                bidon.draw(screen)
                pintarBidon.rect.x =190
                pintarBidon.rect.y =620
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaArriba(protagonistaEnPlaneta,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4)
            interactuar,bidones,vida,piezas,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso = interaccionesMarteArriba(protagonistaEnPlaneta,interactuar,hacer,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,bidones,vida,piezas,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso)
            escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3 = cambiarEscenaMarteFila1(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3)
        #Escena fila arriba centro
        elif(escenaMarte1_2 == True):
            time.sleep(0.007)
            escenaMartePrincipal1_2.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaArriba(protagonistaEnPlaneta,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4)
            interactuar,bidones,vida,piezas,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso = interaccionesMarteArriba(protagonistaEnPlaneta,interactuar,hacer,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,bidones,vida,piezas,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso)
            escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3 = cambiarEscenaMarteFila1(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3)
        #Escena fila arriba derecha
        elif(escenaMarte1_3 == True):
            time.sleep(0.007)
            escenaMartePrincipal1_3.draw(screen)
            if(cogerPieza==False):
                pieza.draw(screen)
                pintarPieza.rect.x = 570
                pintarPieza.rect.y = 540 
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaArriba(protagonistaEnPlaneta,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4)
            interactuar,bidones,vida,piezas,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso = interaccionesMarteArriba(protagonistaEnPlaneta,interactuar,hacer,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,bidones,vida,piezas,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso)
            escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3 = cambiarEscenaMarteFila1(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3)
        #Escena arriba especial
        elif(escenaMarte1_4 == True):
            time.sleep(0.007)
            escenaMartePrincipal1_4.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaArriba(protagonistaEnPlaneta,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4)
            interactuar,bidones,vida,piezas,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso = interaccionesMarteArriba(protagonistaEnPlaneta,interactuar,hacer,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,bidones,vida,piezas,cogerBidon,cogerPieza,cartaMarte1,cartaMarte2,entrarParaiso)
            escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3 = cambiarEscenaMarteFila1(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte1_4,escenaMarte2_1,escenaMarte2_3)
            if(entrarParaiso==True):
                escenaMarte1_4=False
                entradaParaiso=True
                protagonistaEnPlaneta.rect.x = 400
                protagonistaEnPlaneta.rect.y = 500 
        #Escena fila central izquierda
        elif(escenaMarte2_1 == True):
            time.sleep(0.007)
            escenaMartePrincipal2_1.draw(screen)
            if(cogerPiezaExtra1==False):
                pieza.draw(screen)
                pintarPieza.rect.x = 125
                pintarPieza.rect.y = 615
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaCentral(protagonistaEnPlaneta,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4)
            interactuar,vida,piezas,cogerPiezaExtra1,cogerPiezaExtra2,estadoInicial,escenaMarteCentro = interaccionesMarteCentro(protagonistaEnPlaneta,interactuar,hacer,escenaMarte2_1,escenaMarteCentro,escenaMarte2_4,vida,piezas,cogerPiezaExtra1,cogerPiezaExtra2,estadoInicial)
            escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3=cambiarEscenaMarteFila2(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3)
        #Escena fila central centro
        elif(escenaMarteCentro==True):
            time.sleep(0.007)
            escenaMartePrincipalCentro.draw(screen)
            nave.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionConNave(protagonistaEnPlaneta,pintarNave)
            interactuar,vida,piezas,cogerPiezaExtra1,cogerPiezaExtra2,estadoInicial,escenaMarteCentro = interaccionesMarteCentro(protagonistaEnPlaneta,interactuar,hacer,escenaMarte2_1,escenaMarteCentro,escenaMarte2_4,vida,piezas,cogerPiezaExtra1,cogerPiezaExtra2,estadoInicial)
            if(escenaMarteCentro==False):
                escenaNaveCentro = True
                protagonista.rect.x = 365
                protagonista.rect.y = 170
            escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3=cambiarEscenaMarteFila2(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3)
        #Escena fila central derecha
        elif(escenaMarte2_3 == True):
            time.sleep(0.007)
            escenaMartePrincipal2_3.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaCentral(protagonistaEnPlaneta,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4)
            escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3=cambiarEscenaMarteFila2(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3)
        #Escena fila central especial
        elif(escenaMarte2_4 == True):
            time.sleep(0.007)
            escenaMartePrincipal2_4.draw(screen)
            if(cogerPiezaExtra2==False):
                pieza.draw(screen)
                pintarPieza.rect.x = 170
                pintarPieza.rect.y = 660
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaCentral(protagonistaEnPlaneta,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4)
            interactuar,vida,piezas,cogerPiezaExtra1,cogerPiezaExtra2,estadoInicial,escenaMarteCentro = interaccionesMarteCentro(protagonistaEnPlaneta,interactuar,hacer,escenaMarte2_1,escenaMarteCentro,escenaMarte2_4,vida,piezas,cogerPiezaExtra1,cogerPiezaExtra2,estadoInicial)
            escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3=cambiarEscenaMarteFila2(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte1_1,escenaMarte1_2,escenaMarte1_3,escenaMarte2_1,escenaMarte2_3,escenaMarte2_4,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3)
        #Escena fila abajo izquierda
        elif(escenaMarte3_1 == True):
            time.sleep(0.007)
            escenaMartePrincipal3_1.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaAbajo(protagonistaEnPlaneta,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3)
            interactuar,vida,piezas,cogerPieza3 = interaccionesMarteAbajo(protagonistaEnPlaneta,interactuar,hacer,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,vida,piezas,cogerPiezaExtra3)
            escenaMarteCentro,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,escenaMarte2_1,escenaMarte2_3 = cambiarEscenaMarteFila3(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,escenaMarte2_1,escenaMarte2_3)
        #Escena fila abajo central
        elif(escenaMarte3_2 == True):
            time.sleep(0.007)
            escenaMartePrincipal3_2.draw(screen)
            if(cogerPiezaExtra3==False):
                pieza.draw(screen)
                pintarPieza.rect.x = 615 
                pintarPieza.rect.y = 435
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaAbajo(protagonistaEnPlaneta,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3)
            interactuar,vida,piezas,cogerPiezaExtra3 = interaccionesMarteAbajo(protagonistaEnPlaneta,interactuar,hacer,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,vida,piezas,cogerPiezaExtra3)
            escenaMarteCentro,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,escenaMarte2_1,escenaMarte2_3 = cambiarEscenaMarteFila3(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,escenaMarte2_1,escenaMarte2_3)
        #Escena fila abajo derecha
        elif(escenaMarte3_3 == True):
            time.sleep(0.007)
            escenaMartePrincipal3_3.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesMarteFilaAbajo(protagonistaEnPlaneta,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3)
            escenaMarteCentro,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,escenaMarte2_1,escenaMarte2_3 = cambiarEscenaMarteFila3(protagonistaEnPlaneta,escenaMarteCentro,escenaMarte3_1,escenaMarte3_2,escenaMarte3_3,escenaMarte2_1,escenaMarte2_3)
        
        if(piezas==4 or piezas>4 or terminarMarte==True):
            reunirPiezas=True  
        else:
            reunirPiezas=False
        if(vida<0):
            vida=1
            funcionando=False
            gameOverVida=True
        astronautaEnPlaneta.draw(screen)
        udapte(protagonistaEnPlaneta)
        colocarEstadisticas.draw(screen)
        disparo,balas = disparar(protagonistaEnPlaneta,cargador,dispararBala,disparo,balas)
        cartaMarte1,paraiso,vida = primeraCarta(cartaMarte1,cartaSecretaMarte,paraiso,vida,soporteVital)
        cartaMarte2,vida = segundaCarta(cartaMarte2,cartaSecretaMarte2,vida,soporteVital)
        mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
        colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas) 
        misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
        pygame.display.flip()
cambiarMapa = False
estadoInicial = False
escenaEspacio = True
volver = False
if(inyectorGasolina==True):
    gasolina-=20
else:
    gasolina-=30
ancho = 1200
largo = 800
screen = pygame.display.set_mode((ancho,largo))
protagonista.rect.x = 370
protagonista.rect.y = 140
pintarNave.rect.x = 30
pintarNave.rect.y = 30
if(gasolina<0):
    gasolina = 1
    funcionando=False
    gameOverGasolina=True
escenaNaveCentro = True
while funcionando and jupiter:
    screen.fill(negro)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            funcionando = False
    if(decidir==False):
        if(escenaEspacio==True):
            time.sleep(0.02)
            escenaMeteoritos.draw(screen)
            meteoritos.draw(screen)
            movimientoMeteorito(meteoritoSimple,meteoritoAlargado,meteoritoAncho,meteoroGrande)
            funcionando,hacer,volver = gestionarEventos(pintarNaveMovimiento,funcionando,interactuar,volver)
            colisionesNave(pintarNaveMovimiento)
            arreglos = colisionesConMeteorito(pintarNaveMovimiento,meteoritoSimple,meteoritoAlargado,meteoroGrande,arreglos)
            escenaEspacio,escenaEspacio2,escenaZonaJupiter = cambiarEscenaJupiter(pintarNaveMovimiento,escenaEspacio,escenaEspacio2,escenaZonaJupiter)
        elif(escenaEspacio2==True):
            time.sleep(0.02)
            escenaMeteoritos2.draw(screen)
            meteoritoGrande.draw(screen)
            movimientoMeteorito(meteoritoSimple,meteoritoAlargado,meteoritoAncho,meteoroGrande)
            funcionando,hacer,volver = gestionarEventos(pintarNaveMovimiento,funcionando,interactuar,volver)
            colisionesNave(pintarNaveMovimiento)
            arreglos = colisionesConMeteorito(pintarNaveMovimiento,meteoritoSimple,meteoritoAlargado,meteoroGrande,arreglos)
            escenaEspacio,escenaEspacio2,escenaZonaJupiter = cambiarEscenaJupiter(pintarNaveMovimiento,escenaEspacio,escenaEspacio2,escenaZonaJupiter)
        elif(escenaZonaJupiter==True):
            time.sleep(0.02)
            escenaJupiter.draw(screen)
            funcionando,hacer,volver = gestionarEventos(pintarNaveMovimiento,funcionando,interactuar,volver)
            colisionesNave(pintarNaveMovimiento)
            escenaEspacio,escenaEspacio2,escenaZonaJupiter = cambiarEscenaJupiter(pintarNaveMovimiento,escenaEspacio,escenaEspacio2,escenaZonaJupiter)
        if(arreglos<0):
            arreglos=1
            funcionando=False
            gameOverArreglos=True
        naveMovimiento.draw(screen)
        udapte(pintarNaveMovimiento)
        decidir,decision = pintarDecisionJupiter(escenaZonaJupiter,pintarNaveMovimiento,decisionJupiter,decidir,decision)
        colocarEstadisticas.draw(screen)
        mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
        colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
        misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton) 
        pygame.display.flip()
    if(decidir==True):
        if(decision==1):
            jupiter=False
            funcionando=False
            gameOverJupiter=True 
        elif(decision==2):
            if(cambiarMapa==False):
                if(escenaNaveCentro==True and escenaNaveIzquierda==False):
                    time.sleep(0.007)
                    SpriteNave1.draw(screen)
                    escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                    funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                    interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                    colisionNave1(protagonista)
                #Escena de la izquierda de la nave  
                if(escenaNaveIzquierda==True and escenaNaveCentro==False):
                    time.sleep(0.007)
                    SpriteNave2.draw(screen)
                    escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                    funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                    interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                    colisionNave2(protagonista)
                #Escena de abajo de la nave
                if(escenaNaveAbajo==True and escenaNaveCentro==False):
                    time.sleep(0.007)
                    SpriteNave3.draw(screen)
                    escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                    funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                    interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                    colisionNave3(protagonista)
                misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
                astronauta.draw(screen)
                udapte(protagonista)
                cogerCristal = pintarCristalAtmosfera(cristalAtmosfera,cogerCristal,decision)
                cogerDistribuidor,distribuidorDeEnergia,cogerCristal,terminarJupiter = pintarDistribuidorEnergia(distribuidorEnergia,cogerCristal,cogerDistribuidor,distribuidorDeEnergia,terminarJupiter)
                colocarEstadisticas.draw(screen)
                colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
                mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
                pygame.display.flip()
                if(terminarJupiter==False):
                    cambiarMapa=False
            elif(volver == True):
                escenaNaveIzquierda=True
                cambiarMapa=False
                jupiter=True
                urano=False
                volver=False 
            #Cambio de escena de la nave al mapa 
            elif(cambiarMapa==True and terminarJupiter==True):
                mapaEspacio.draw(screen)
                flechaSeleccion.draw(screen)
                escenaNaveAbajo=False
                escenaNaveCentro=False
                escenaNaveIzquierda=False
                time.sleep(0.007)
                urano = True
                volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton  = gestionarEventosMapa(pintarFlecha,volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton)
                colocarEstadisticas.draw(screen)
                colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
                mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
                misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
                mensajesMapa(cambiarMapa,pintarFlecha,informacionSol,informacionMercurio,informacionVenus,informacionTierra,informacionMarte,informacionJupiter,informacionSaturno,informacionUrano,informacionNeptuno,informacionPluton)
                pygame.display.flip()
        elif(decision==3):
            terminarJupiter=True
            if(cambiarMapa==False):
                if(escenaNaveCentro==True and escenaNaveIzquierda==False):
                    time.sleep(0.007)
                    SpriteNave1.draw(screen)
                    escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                    funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                    interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                    colisionNave1(protagonista)
                #Escena de la izquierda de la nave  
                if(escenaNaveIzquierda==True and escenaNaveCentro==False):
                    time.sleep(0.007)
                    SpriteNave2.draw(screen)
                    escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                    funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                    interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                    colisionNave2(protagonista)
                #Escena de abajo de la nave
                if(escenaNaveAbajo==True and escenaNaveCentro==False):
                    time.sleep(0.007)
                    SpriteNave3.draw(screen)
                    escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                    funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                    interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                    colisionNave3(protagonista)
                misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
                astronauta.draw(screen)
                udapte(protagonista)
                colocarEstadisticas.draw(screen)
                colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
                mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
                pygame.display.flip()
                if(terminarJupiter==False):
                    cambiarMapa=False
            elif(volver == True):
                escenaNaveIzquierda=True
                cambiarMapa=False
                jupiter=True
                urano=False
                volver=False 
            #Cambio de escena de la nave al mapa 
            elif(cambiarMapa==True and terminarJupiter==True):
                mapaEspacio.draw(screen)
                flechaSeleccion.draw(screen)
                escenaNaveAbajo=False
                escenaNaveCentro=False
                escenaNaveIzquierda=False
                time.sleep(0.007)
                urano = True
                volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton  = gestionarEventosMapa(pintarFlecha,volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton)
                colocarEstadisticas.draw(screen)
                colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
                mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
                misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
                mensajesMapa(cambiarMapa,pintarFlecha,informacionSol,informacionMercurio,informacionVenus,informacionTierra,informacionMarte,informacionJupiter,informacionSaturno,informacionUrano,informacionNeptuno,informacionPluton)
                pygame.display.flip() 
cambiarMapa = False
estadoInicial = False
escenaUranoCentro = True
volver = False
cogerPieza = False
cogerBidon = False
if(inyectorGasolina==True):
    gasolina-=25
else:
    gasolina-=40
if(gasolina<0):
    gasolina=1
    funcionando=False
    gameOverGasolina=True
ancho = 1200
largo = 800
screen = pygame.display.set_mode((ancho,largo))
protagonistaEnPlaneta.rect.x = 150
protagonistaEnPlaneta.rect.y = 280
escenaNaveCentro = True 
while funcionando and urano:
    screen.fill(negro)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            funcionando = False
    if(estadoInicial==True):
        if(cambiarMapa==False):
            if(escenaNaveCentro==True and escenaNaveIzquierda==False):
                time.sleep(0.007)
                SpriteNave1.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                colisionNave1(protagonista)
                if(estadoInicial==False):
                    escenaUranoCentro=True
                    protagonistaEnPlaneta.rect.x = 150
                    protagonistaEnPlaneta.rect.y = 280
            #Escena de la izquierda de la nave  
            if(escenaNaveIzquierda==True and escenaNaveCentro==False):
                time.sleep(0.007)
                SpriteNave2.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                colisionNave2(protagonista)
                if(terminarUrano==False):
                    cambiarMapa=False
            #Escena de abajo de la nave
            if(escenaNaveAbajo==True and escenaNaveCentro==False):
                time.sleep(0.007)
                SpriteNave3.draw(screen)
                escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo = cambiarEscenaNave(protagonista,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo)
                funcionando,hacer,volver = gestionarEventos(protagonista,funcionando,interactuar,volver)
                interactuar,balas,gasolina,arreglos,vida,bidones,piezas,cambiarMapa,estadoInicial,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion = interaccionesNave(protagonista,interactuar,escenaNaveCentro,escenaNaveIzquierda,escenaNaveAbajo,gasolina,arreglos,vida,balas,bidones,piezas,hacer,cambiarMapa,estadoInicial,cambiarNave,reunirPiezas,generadorAgua,cogerDistribuidor,cogerTrajeAntiPresion)
                colisionNave3(protagonista)
            misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
            astronauta.draw(screen)
            udapte(protagonista)
            cogerTrajeAntiPresion,trajeAP = mostrarTrajeAP(trajeAntiPresion,cogerTrajeAntiPresion,trajeAP)
            colocarEstadisticas.draw(screen)
            colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
            mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
            pygame.display.flip()
            if(trajeAP==True):
                terminarUrano=True
            
            pygame.display.flip()
            
        if(volver == True):
            escenaNaveIzquierda=True
            cambiarMapa=False
            urano=True
            pluton=False
            volver=False 
        #Cambio de escena de la nave al mapa 
        elif(cambiarMapa==True):
            mapaEspacio.draw(screen)
            flechaSeleccion.draw(screen)
            escenaNaveAbajo=False
            escenaNaveCentro=False
            escenaNaveIzquierda=False
            time.sleep(0.007)
            pluton = True
            volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton  = gestionarEventosMapa(pintarFlecha,volver,funcionando,estadoInicial,luna,marte,jupiter,saturno,urano,neptuno,pluton)
            colocarEstadisticas.draw(screen)
            colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
            mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
            misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton)
            mensajesMapa(cambiarMapa,pintarFlecha,informacionSol,informacionMercurio,informacionVenus,informacionTierra,informacionMarte,informacionJupiter,informacionSaturno,informacionUrano,informacionNeptuno,informacionPluton)
            pygame.display.flip() 
    else:
        if(soporteVital==True):
            vida-=0.0095
        else:
            vida-=0.02
        if(escenaUranoCentro==True):
            time.sleep(0.007)
            escenaUranoCentral.draw(screen)
            nave.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesUrano(protagonistaEnPlaneta,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
            colisionConNave(protagonistaEnPlaneta,pintarNave)
            interactuar,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial,escenaUranoCentro = interaccionesUrano(protagonistaEnPlaneta,interactuar,hacer,escenaUranoCentro,escenaUranoInterseccion,escenaUranoInferior,escenaUranoSuperior,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial)
            escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior = cambiarEscenaUrano(protagonistaEnPlaneta,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
            
        elif(escenaUranoInterseccion==True):
            time.sleep(0.007)
            escenaUranoCruce.draw(screen)
            cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera = mostrarHidrogeno(bolaHidrogeno,pintarBolaHidrogeno,cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
            if(cogerPieza==False):
                pieza.draw(screen)
                pintarPieza.rect.x = 600
                pintarPieza.rect.y = 225
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesUrano(protagonistaEnPlaneta,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
            interactuar,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial,escenaUranoCentro = interaccionesUrano(protagonistaEnPlaneta,interactuar,hacer,escenaUranoCentro,escenaUranoInterseccion,escenaUranoInferior,escenaUranoSuperior,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial)
            escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior = cambiarEscenaUrano(protagonistaEnPlaneta,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
        elif(escenaUranoInferior==True):
            time.sleep(0.007)
            escenaUranoAbajo.draw(screen)
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesUrano(protagonistaEnPlaneta,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
            interactuar,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial,escenaUranoCentro = interaccionesUrano(protagonistaEnPlaneta,interactuar,hacer,escenaUranoCentro,escenaUranoInterseccion,escenaUranoInferior,escenaUranoSuperior,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial)
            escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior = cambiarEscenaUrano(protagonistaEnPlaneta,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
        elif(escenaUranoSuperior==True):
            time.sleep(0.007)
            escenaUranoArriba.draw(screen)
            cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera = mostrarHidrogeno(bolaHidrogeno,pintarBolaHidrogeno,cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
            if(cogerBidon==False):
                bidon.draw(screen)
                pintarBidon.rect.x = 372
                pintarBidon.rect.y = 170
            funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
            colisionesUrano(protagonistaEnPlaneta,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
            interactuar,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial,escenaUranoCentro = interaccionesUrano(protagonistaEnPlaneta,interactuar,hacer,escenaUranoCentro,escenaUranoInterseccion,escenaUranoInferior,escenaUranoSuperior,cogerPieza,piezas,cogerBidon,bidones,vida,hidrogeno,cogerHidrogeno,estadoInicial)
            escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior = cambiarEscenaUrano(protagonistaEnPlaneta,escenaUranoCentro,escenaUranoInterseccion,escenaUranoSuperior,escenaUranoInferior)
        if(hidrogeno==5):
            reunirHidrogeno=True
        if(vida<0):
            vida=1
            funcionando=False
            gameOverVida=True
        astronautaEnPlaneta.draw(screen)
        udapte(protagonistaEnPlaneta)
        disparo,balas = disparar(protagonistaEnPlaneta,cargador,dispararBala,disparo,balas)
        colocarEstadisticas.draw(screen)
        mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
        colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
        misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton) 
        pygame.display.flip()
cambiarMapa = False
estadoInicial = False
escenaPlutonCentral = True
volver = False
if(inyectorGasolina==True):
    gasolina-=20
else:
    gasolina-=30
if(gasolina<0):
    gasolina=1
    funcionando=False
    gameOverGasolina=True
ancho = 1200
largo = 800
screen = pygame.display.set_mode((ancho,largo))
protagonistaEnPlaneta.rect.x = 400
protagonistaEnPlaneta.rect.y = 720
antagonista.rect.x = 400
antagonista.rect.y = 20
while funcionando and pluton:
    screen.fill(negro)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            funcionando = False
            
    if(escenaPlutonCentral==True):
        time.sleep(0.007)
        escenaPlutonCentro.draw(screen)
        nave.draw(screen)
        funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
        colisionConNave(protagonistaEnPlaneta,pintarNave)
        escenaPlutonCentral,escenaPlutonJefeFinal = cambiarEscenaPluton(protagonistaEnPlaneta,escenaPlutonCentral,escenaPlutonJefeFinal)
    elif(escenaPlutonJefeFinal==True):
        time.sleep(0.007)
        escenaPlutonJefe.draw(screen)
        jefeFinal.draw(screen)
        contadorDisparo,disparoMaligno,vidaJefe,disparo,vida,ataqueEspecial,contadorAtaqueEspecial,contadorMira,contadorExplosion=combate(protagonistaEnPlaneta,antagonista,vidaJefe,dispararBala,disparo,contadorDisparo,disparoMaligno,balaOscura,pintarBalaOscura,vida,miraEspecial,explosionEspecial,pintarMira,pintarExplosion,ataqueEspecial,contadorAtaqueEspecial,contadorMira,contadorExplosion)
        interactuar,vida,balas = suministrosEmergencia(protagonistaEnPlaneta,vida,balas,interactuar,hacer,pintarMedicamentos,medicamentosEspeciales)
        updateJefe(antagonista)
        funcionando,hacer,volver = gestionarEventos(protagonistaEnPlaneta,funcionando,interactuar,volver)
        escenaPlutonCentral,escenaPlutonJefeFinal = cambiarEscenaPluton(protagonistaEnPlaneta,escenaPlutonCentral,escenaPlutonJefeFinal)
    if(vida<0):
        vida=1
        funcionando=False
        gameOverBossFinal=True
    if(vidaJefe<0):
        funcionando=False
    
    astronautaEnPlaneta.draw(screen)
    udapte(protagonistaEnPlaneta)
    disparo,balas = disparar(protagonistaEnPlaneta,cargador,dispararBala,disparo,balas)
    colocarEstadisticas.draw(screen)
    mensajesHUD(gasolina,arreglos,vida,balas,bidones,piezas)
    colocarEstadisticas = colocarStats(estadisticas,gasolina,arreglos,vida,balas,bidones,piezas)
    misiones(estadoInicial,cambiarMapa,luna,cogerPropulsor,marte,reunirPiezas,jupiter,saturno,urano,neptuno,pluton) 
    pygame.display.flip()    

ancho = 800
largo = 800
screen = pygame.display.set_mode((ancho,largo))
while gameOverVida or gameOverJupiter or gameOverGasolina or gameOverBossFinal or gameOverArreglos:
    screen.fill(negro)
    for event in pygame.event.get():
        if(event == pygame.QUIT):
            gameOverVida = False
            gameOverJupiter = False 
            gameOverGasolina = False 
            gameOverBossFinal =False 
            gameOverArreglos = False
    if(gameOverVida):
        gameOverPorVida.draw(screen)
    if(gameOverJupiter):
        gameOverPorJupiter.draw(screen)
    if(gameOverArreglos):
        gameOverPorArreglos.draw(screen)
    if(gameOverGasolina):
        gameOverPorGasolina.draw(screen)
    if(gameOverBossFinal):
        gameOverPorJefe.draw(screen)
    pygame.display.flip()

pygame.quit() 