import pygame
from framesPersonaje import Frames
class cargarImagen:
    #Funcion para crear el astronauta
    def crearAstronauta(spritesJuego):
        protagonista = pygame.sprite.Sprite()

        protagonista.spriteSheet = pygame.image.load("Astronauta.png").convert()
        
        Frames.cargarFramesDerecha(protagonista)
        Frames.cargarFramesIzquierda(protagonista)
        Frames.cargarFramesAbajo(protagonista)
        Frames.cargarFramesArriba(protagonista)

        protagonista.rect.x = 340
        protagonista.rect.y = 120
        protagonista.velocidad_x = 0
        protagonista.velocidad_y = 0

        spritesJuego.add(protagonista)

        return protagonista
    #Funcion para crear las estadisticas
    def stats(x,y,ancho):
        stats = pygame.sprite.Sprite()

        stats.image = pygame.Surface([ancho,20])
        stats.rect = stats.image.get_rect()

        stats.rect.x = x
        stats.rect.y = y

        return stats
    #Funcion para pintar las estadisticas
    def colocarStats(spritesJuego,gasolina,arreglo,vida,balas,bidones,piezas):
        naranja = pygame.Color(255,120,0)
        dorado = pygame.Color(212,175,55)
        bidonGasofa = pygame.Color(149,49,21)
        gris = pygame.Color(155,155,155)
        blanco = pygame.Color(255,255,255)
        rojo = pygame.Color(255,0,0)
        
        estadisticas = pygame.sprite.Group()

        estadisticas_1 = cargarImagen.stats(900,120,gasolina*2)
        estadisticas_1.image.fill(naranja)

        estadisticas.add(estadisticas_1)
        spritesJuego.add(estadisticas_1)

        estadisticas_2 = cargarImagen.stats(900,180,arreglo*2)
        estadisticas_2.image.fill(blanco)

        estadisticas.add(estadisticas_2)
        spritesJuego.add(estadisticas_2)

        estadisticas_3 = cargarImagen.stats(900,330,vida*2)
        estadisticas_3.image.fill(rojo)

        estadisticas.add(estadisticas_3)
        spritesJuego.add(estadisticas_3)

        estadisticas_4 = cargarImagen.stats(900,400,balas*2)
        estadisticas_4.image.fill(dorado)

        estadisticas.add(estadisticas_4)
        spritesJuego.add(estadisticas_4)

        estadisticas_5 = cargarImagen.stats(900,470,bidones*66)
        estadisticas_5.image.fill(bidonGasofa)

        estadisticas.add(estadisticas_5)
        spritesJuego.add(estadisticas_5)

        estadisticas_6 = cargarImagen.stats(900,540,piezas*20)
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
    #Funcion para crear el astronauta en los planetas
    def crearAstronautaPlaneta(spritesJuego):
        astronauta = pygame.sprite.Sprite()

        astronauta.spriteSheet = pygame.image.load("AstronautaEnPlaneta.png").convert()

        Frames.cargarFramesDerechaAChico(astronauta)
        Frames.cargarFramesIzquierdaAChico(astronauta)
        Frames.cargarFramesAbajoAChico(astronauta)
        Frames.cargarFramesArribaAChico(astronauta)

        astronauta.rect.x = 50
        astronauta.rect.y = 50

        astronauta.velocidad_x = 0
        astronauta.velocidad_y = 0

        spritesJuego.add(astronauta)

        return astronauta
    #Funcion para crear las balas 
    def crearBalas(sprites):
        bala = pygame.sprite.Sprite()

        bala.image = pygame.image.load("bala.png")
        bala.rect = bala.image.get_rect()

        bala.rect.x = 0
        bala.rect.y = 0

        sprites.add(bala)
        return bala
    #Funcion para crear el folleto del comienzo
    def crearComienzo(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("comienzo.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 100
        escena.rect.y = 100

        sprites.add(escena)

        return escena 
    #Funcion para crear el mapa
    def crearMapa(sprites):
        mapa = pygame.sprite.Sprite()

        mapa.image = pygame.image.load("MapaPlanetas.png")
        mapa.rect = mapa.image.get_rect()

        mapa.rect.x = 0
        mapa.rect.y = 0

        sprites.add(mapa)
        return mapa
    #Funcion para crear la flecha
    def crearFlecha(sprites):
        flecha = pygame.sprite.Sprite()

        flecha.image = pygame.image.load("flechaSeleccion.png")
        flecha.rect = flecha.image.get_rect() 

        flecha.rect.x = 790
        flecha.rect.y = 480

        sprites.add(flecha)

        return flecha
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
    #Funcion para crear la info del nivel de la luna
    def nivelLuna(sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("nivelLuna.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
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

        bidon.rect.x = 565
        bidon.rect.y = 620

        spritesJuego.add(bidon)

        return bidon
    #Funcion para crear las piezas
    def crearPiezas(spritesJuego):
        pieza = pygame.sprite.Sprite()

        pieza.image = pygame.image.load("Pieza.png")
        pieza.rect = pieza.image.get_rect()

        pieza.rect.x = 380
        pieza.rect.y = 605
        
        spritesJuego.add(pieza)
        return pieza
    #Funcion para crear el objeto de la primera mision de la luna
    def propulsorLuz(spritesJuego):
        propulsor = pygame.sprite.Sprite()

        propulsor.image = pygame.image.load("PropulsorDeLuz.png")
        propulsor.rect = propulsor.image.get_rect()

        propulsor.rect.x = 270
        propulsor.rect.y = 380

        spritesJuego.add(propulsor)
        return propulsor
    #Funcion para crear el nivel
    def nivelMarte(sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("nivelMarte.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
    #Funcion para crear la primera escena de marte
    def escenaMarte1(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte1_1.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte2(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte1_2.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte3(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte1_3.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte4(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte1_4.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte5(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte2_1.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte6(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarteCentro.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte7(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte2_3.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte8(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte2_4.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte9(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte3_1.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte10(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte3_2.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte11(sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("escenaMarte3_3.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
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
    
    def crearGeneradorAgua(spritesJuego):
        generador = pygame.sprite.Sprite()

        generador.image = pygame.image.load("GeneradorDeAgua.png")
        generador.rect = generador.image.get_rect()

        generador.rect.x = 100
        generador.rect.y = 100

        spritesJuego.add(generador)

        return generador
    
    def gameOverVida(sprites):
        
        gameOver = pygame.sprite.Sprite()

        gameOver.image = pygame.image.load("finJuegoVida.png")
        gameOver.rect = gameOver.image.get_rect()

        gameOver.rect.x = 100
        gameOver.rect.y = 100

        sprites.add(gameOver)
        return gameOver
    
    def nivelJupiter(sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("nivelJupiter.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
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
    
    def crearNaveEnMovimiento(spritesJuego):
        naveMov = pygame.sprite.Sprite()

        naveMov.spriteSheet = pygame.image.load("spriteSheetNave.png")
        Frames.cargarFramesNaveDerecha(naveMov)
        Frames.cargarFramesNaveIzquierda(naveMov)
        Frames.cargarFramesNaveArriba(naveMov)
        Frames.cargarFramesNaveAbajo(naveMov)

        naveMov.rect.x= 700
        naveMov.rect.y = 400

        naveMov.velocidad_x = 0
        naveMov.velocidad_y = 0

        spritesJuego.add(naveMov)
        return naveMov
    
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
    
    def nivelUrano(sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("nivelUrano.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
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

    def nivelPluton(sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("nivelPluton.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
    def crearNivelPluton(spritesJuego):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("nivelPluton.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        spritesJuego.add(nivel)

        return nivel
    
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
        Frames.cargarFramesJefeDerecha(jefe)
        Frames.cargarFramesJefeIzquierda(jefe)
        Frames.cargarFramesJefeAbajo(jefe)

        jefe.velocidad_x = 1
        spritesJuego.add(jefe)

        return jefe
    
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
    
    def crearGameOverJefeFinal(sprites):
        fin = pygame.sprite.Sprite()

        fin.image = pygame.image.load("finJuegoJefeFinal.png")
        fin.rect = fin.image.get_rect()

        fin.rect.x = 100
        fin.rect.y = 100

        sprites.add(fin)

        return fin
    
    def crearControles(sprite):
        escena = pygame.sprite.Sprite()
        escena.image = pygame.image.load("controles.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 100
        escena.rect.y = 100

        sprite.add(escena)
        return escena
    
    def ganacion(sprite):
        escena = pygame.sprite.Sprite()
        escena.image = pygame.image.load("Ganacion.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 100
        escena.rect.y = 100

        sprite.add(escena)
        return escena