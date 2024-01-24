import pygame
from image_utils.framesPersonaje import Frames
class CargarImagen:

    def __init__(self):
        self.frames = Frames()
    #Funcion para crear el astronauta
    def crearAstronauta(self,spritesJuego):
        protagonista = pygame.sprite.Sprite()

        protagonista.spriteSheet = pygame.image.load("SolarAdventures/src/images/Astronauta.png").convert()
        
        self.frames.cargarFramesDerecha(protagonista)
        self.frames.cargarFramesIzquierda(protagonista)
        self.frames.cargarFramesAbajo(protagonista)
        self.frames.cargarFramesArriba(protagonista)

        protagonista.rect.x = 340
        protagonista.rect.y = 120
        protagonista.velocidad_x = 0
        protagonista.velocidad_y = 0

        spritesJuego.add(protagonista)

        return protagonista
    #Funcion para crear las estadisticas
    def stats(self,x,y,ancho):
        stats = pygame.sprite.Sprite()

        stats.image = pygame.Surface([ancho,20])
        stats.rect = stats.image.get_rect()

        stats.rect.x = x
        stats.rect.y = y

        return stats
    #Funcion para pintar las estadisticas
    def colocarStats(self,spritesJuego,gasolina,arreglo,vida,balas,bidones,piezas):
        naranja = pygame.Color(255,120,0)
        dorado = pygame.Color(212,175,55)
        bidonGasofa = pygame.Color(149,49,21)
        gris = pygame.Color(155,155,155)
        blanco = pygame.Color(255,255,255)
        rojo = pygame.Color(255,0,0)
        
        estadisticas = pygame.sprite.Group()

        estadisticas_1 = self.stats(900,120,gasolina*2)
        estadisticas_1.image.fill(naranja)

        estadisticas.add(estadisticas_1)
        spritesJuego.add(estadisticas_1)

        estadisticas_2 = self.stats(900,180,arreglo*2)
        estadisticas_2.image.fill(blanco)

        estadisticas.add(estadisticas_2)
        spritesJuego.add(estadisticas_2)

        estadisticas_3 = self.stats(900,330,vida*2)
        estadisticas_3.image.fill(rojo)

        estadisticas.add(estadisticas_3)
        spritesJuego.add(estadisticas_3)

        estadisticas_4 = self.stats(900,400,balas*2)
        estadisticas_4.image.fill(dorado)

        estadisticas.add(estadisticas_4)
        spritesJuego.add(estadisticas_4)

        estadisticas_5 = self.stats(900,470,bidones*66)
        estadisticas_5.image.fill(bidonGasofa)

        estadisticas.add(estadisticas_5)
        spritesJuego.add(estadisticas_5)

        estadisticas_6 = self.stats(900,540,piezas*20)
        estadisticas_6.image.fill(gris)

        estadisticas.add(estadisticas_6)
        spritesJuego.add(estadisticas_6)

        return estadisticas 
    #Funcion para crear la escena central de la nave
    def escenaNave1(self,spritesJuego):
        InteriorNave = pygame.sprite.Sprite()

        InteriorNave.image = pygame.image.load("SolarAdventures/src/images/InteriorNave1.png")
        InteriorNave.rect = InteriorNave.image.get_rect()

        InteriorNave.rect.x = 0
        InteriorNave.rect.y = 0

        spritesJuego.add(InteriorNave)

        return InteriorNave
    #Funcion para crear la escena de la izquierda de la nave
    def escenaNave2(self,spritesJuego):
        InteriorNave = pygame.sprite.Sprite()

        InteriorNave.image = pygame.image.load("SolarAdventures/src/images/InteriorNave2.png")
        InteriorNave.rect = InteriorNave.image.get_rect()

        InteriorNave.rect.x = 0
        InteriorNave.rect.y = 0

        spritesJuego.add(InteriorNave)

        return InteriorNave
    #Funcion para crear la escena de abajo de la nave
    def escenaNave3(self,spritesJuego):
        InteriorNave = pygame.sprite.Sprite()

        InteriorNave.image = pygame.image.load("SolarAdventures/src/images/InteriorNave3.png")
        InteriorNave.rect = InteriorNave.image.get_rect()

        InteriorNave.rect.x = 0
        InteriorNave.rect.y = 0

        spritesJuego.add(InteriorNave)

        return InteriorNave 
    #Funcion para crear el astronauta en los planetas
    def crearAstronautaPlaneta(self,spritesJuego):
        astronauta = pygame.sprite.Sprite()

        astronauta.spriteSheet = pygame.image.load("SolarAdventures/src/images/AstronautaEnPlaneta.png").convert()

        self.frames.cargarFramesDerechaAChico(astronauta)
        self.frames.cargarFramesIzquierdaAChico(astronauta)
        self.frames.cargarFramesAbajoAChico(astronauta)
        self.frames.cargarFramesArribaAChico(astronauta)

        astronauta.rect.x = 50
        astronauta.rect.y = 50

        astronauta.velocidad_x = 0
        astronauta.velocidad_y = 0

        spritesJuego.add(astronauta)

        return astronauta
    #Funcion para crear las balas 
    def crearBalas(self,sprites):
        bala = pygame.sprite.Sprite()

        bala.image = pygame.image.load("SolarAdventures/src/images/bala.png")
        bala.rect = bala.image.get_rect()

        bala.rect.x = 0
        bala.rect.y = 0

        sprites.add(bala)
        return bala
    #Funcion para crear el folleto del comienzo
    def crearComienzo(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/comienzo.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 100
        escena.rect.y = 100

        sprites.add(escena)

        return escena 
    #Funcion para crear el mapa
    def crearMapa(self,sprites):
        mapa = pygame.sprite.Sprite()

        mapa.image = pygame.image.load("SolarAdventures/src/images/MapaPlanetas.png")
        mapa.rect = mapa.image.get_rect()

        mapa.rect.x = 0
        mapa.rect.y = 0

        sprites.add(mapa)
        return mapa
    #Funcion para crear la flecha
    def crearFlecha(self,sprites):
        flecha = pygame.sprite.Sprite()

        flecha.image = pygame.image.load("SolarAdventures/src/images/flechaSeleccion.png")
        flecha.rect = flecha.image.get_rect() 

        flecha.rect.x = 790
        flecha.rect.y = 480

        sprites.add(flecha)

        return flecha
    #Funcion para crear la información del sol
    def infoSol(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/infoSol.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Funcion para crear la información de mercurio
    def infoMercurio(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/infoMercurio.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Funcion para crear la información de venus
    def infoVenus(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/infoVenus.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Funcion para crear la información de la tierra
    def infoTierra(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/infoTierra.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Funcion para crear la información de marte 
    def infoMarte(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/infoMarte.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Función para crear la información de júpiter
    def infoJupiter(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/infoJupiter.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Funcion para crear la información de saturno
    def infoSaturno(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/InfoSaturno.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Función para crear la información de urano
    def infoUrano(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/InfoUrano.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Función para crear la información de neptuno
    def infoNeptuno(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/InfoNeptuno.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Función para crear la información de plutón
    def infoPluton(self,spritesJuego):
        info = pygame.sprite.Sprite()
        
        info.image = pygame.image.load("SolarAdventures/src/images/infoPluton.png")
        info.rect = info.image.get_rect()

        info.rect.x = 100
        info.rect. y = 100

        spritesJuego.add(info)

        return info
    #Funcion para crear la info del nivel de la luna
    def nivelLuna(self,sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("SolarAdventures/src/images/nivelLuna.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
    #Funcion para crear la escena central de la luna
    def escenaLuna1(self,spritesJuego):
        escenaLuna = pygame.sprite.Sprite()

        escenaLuna.image = pygame.image.load("SolarAdventures/src/images/EscenaLuna1.png")
        escenaLuna.rect = escenaLuna.image.get_rect()

        escenaLuna.rect.x = 0
        escenaLuna.rect.y = 0

        spritesJuego.add(escenaLuna)
        return escenaLuna       
    #Funcion para crear la escena de la izquierda de la luna
    def escenaLuna2(self,spritesJuego):
        escenaLuna = pygame.sprite.Sprite()

        escenaLuna.image = pygame.image.load("SolarAdventures/src/images/EscenaLunaIzquierda.png")
        escenaLuna.rect = escenaLuna.image.get_rect()

        escenaLuna.rect.x = 0
        escenaLuna.rect.y = 0

        spritesJuego.add(escenaLuna)
        return escenaLuna
    #Funcion para crear la escena de arriba de la luna
    def escenaLuna3(self,spritesJuego):
        escenaLuna = pygame.sprite.Sprite()

        escenaLuna.image = pygame.image.load("SolarAdventures/src/images/EscenaLunaArriba.png")
        escenaLuna.rect = escenaLuna.image.get_rect()

        escenaLuna.rect.x = 0
        escenaLuna.rect.y = 0

        spritesJuego.add(escenaLuna)
        return escenaLuna
    #Funcion para crear la escena de abajo de la luna
    def escenaLuna4(self,spritesJuego):
        escenaLuna = pygame.sprite.Sprite()

        escenaLuna.image = pygame.image.load("SolarAdventures/src/images/EscenaLunaAbajo.png")
        escenaLuna.rect = escenaLuna.image.get_rect()

        escenaLuna.rect.x = 0
        escenaLuna.rect.y = 0

        spritesJuego.add(escenaLuna)
        return escenaLuna
    #Funcion para crear la escena de arriba izquierda de la luna
    def escenaLuna5(self,spritesJuego):
        escenaLuna = pygame.sprite.Sprite()

        escenaLuna.image = pygame.image.load("SolarAdventures/src/images/EscenaLunaArribaIzquierda.png")
        escenaLuna.rect = escenaLuna.image.get_rect()

        escenaLuna.rect.x = 0
        escenaLuna.rect.y = 0

        spritesJuego.add(escenaLuna)
        return escenaLuna
    #Funcion para crear la escena de arriba derecha de la luna
    def escenaLuna6(self,spritesJuego):
        escenaLuna = pygame.sprite.Sprite()

        escenaLuna.image = pygame.image.load("SolarAdventures/src/images/EscenaLunaArribaDerecha.png")
        escenaLuna.rect = escenaLuna.image.get_rect()

        escenaLuna.rect.x = 0
        escenaLuna.rect.y = 0

        spritesJuego.add(escenaLuna)
        return escenaLuna
    #Funcion para crear la recompensa del secreto de la luna
    def crearInyector(self,spritesJuego):
        inyector = pygame.sprite.Sprite()

        inyector.image=pygame.image.load("SolarAdventures/src/images/InyectorCuantico.png")
        inyector.rect = inyector.image.get_rect()

        inyector.rect.x = 100
        inyector.rect.y = 100

        spritesJuego.add(inyector)
        return inyector
    #Funcion para crear la nave 
    def crearNave(self,spritesJuego):
        nave = pygame.sprite.Sprite()

        nave.image = pygame.image.load("SolarAdventures/src/images/Nave.png")
        nave.rect = nave.image.get_rect()

        nave.rect.x = 450
        nave.rect.y = 200

        spritesJuego.add(nave)

        return nave
    #Funcion para crear el bidon de gasolina
    def crearBidonGasofa(self,spritesJuego):
        bidon = pygame.sprite.Sprite()

        bidon.image = pygame.image.load("SolarAdventures/src/images/BidonGasofa.png")
        bidon.rect = bidon.image.get_rect()

        bidon.rect.x = 565
        bidon.rect.y = 620

        spritesJuego.add(bidon)

        return bidon
    #Funcion para crear las piezas
    def crearPiezas(self,spritesJuego):
        pieza = pygame.sprite.Sprite()

        pieza.image = pygame.image.load("SolarAdventures/src/images/Pieza.png")
        pieza.rect = pieza.image.get_rect()

        pieza.rect.x = 380
        pieza.rect.y = 605
        
        spritesJuego.add(pieza)
        return pieza
    #Funcion para crear el objeto de la primera mision de la luna
    def propulsorLuz(self,spritesJuego):
        propulsor = pygame.sprite.Sprite()

        propulsor.image = pygame.image.load("SolarAdventures/src/images/PropulsorDeLuz.png")
        propulsor.rect = propulsor.image.get_rect()

        propulsor.rect.x = 270
        propulsor.rect.y = 380

        spritesJuego.add(propulsor)
        return propulsor
    #Funcion para crear el nivel
    def nivelMarte(self,sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("SolarAdventures/src/images/nivelMarte.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
    #Funcion para crear la primera escena de marte
    def escenaMarte1(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte1_1.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte2(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte1_2.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte3(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte1_3.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte4(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte1_4.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte5(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte2_1.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte6(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarteCentro.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte7(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte2_3.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte8(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte2_4.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte9(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte3_1.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte10(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte3_2.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def escenaMarte11(self,sprites):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaMarte3_3.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        sprites.add(escena)
        return escena
    
    def CrearCartaSecretaMarte(self,spritesJuego):
        carta = pygame.sprite.Sprite()

        carta.image = pygame.image.load("SolarAdventures/src/images/cartaSecretaMarte.png")
        carta.rect = carta.image.get_rect()

        carta.rect.x = 200
        carta.rect.y = 150

        spritesJuego.add(carta)
        return carta
    #Funcion para crear la segunda pista secreta de marte
    def CrearCartaSecretaMarte2(self,spritesJuego):
        carta = pygame.sprite.Sprite()

        carta.image = pygame.image.load("SolarAdventures/src/images/cartaSecretaMarte2.png")
        carta.rect = carta.image.get_rect()

        carta.rect.x = 200
        carta.rect.y = 150

        spritesJuego.add(carta)
        return carta
    #Funcion para crear la primera escena del paraiso
    def CrearPrimeraEscenaParaiso(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/entradaParaiso.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la escena del paraiso
    def CrearElParaiso(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/ElParaiso.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear el primer mensaje dentro del paraiso
    def crearPrimerMensajeParaiso(self,spritesJuego):
        mensaje = pygame.sprite.Sprite()

        mensaje.image = pygame.image.load("SolarAdventures/src/images/elParaisoMensaje1.png")
        mensaje.rect = mensaje.image.get_rect()

        mensaje.rect.x = 100
        mensaje.rect.y = 50

        spritesJuego.add(mensaje)
        return mensaje
    #Funcion para crear el segundo menssaje dentro del paraiso
    def crearSegundoMensajeParaiso(self,spritesJuego):
        mensaje = pygame.sprite.Sprite()

        mensaje.image = pygame.image.load("SolarAdventures/src/images/elParaisoMensaje2.png")
        mensaje.rect = mensaje.image.get_rect()

        mensaje.rect.x = 100
        mensaje.rect.y = 50

        spritesJuego.add(mensaje)
        return mensaje
    #Funcion para crear el soporte vital
    def crearSoporteVital(self,spritesJuego):
        soporte = pygame.sprite.Sprite()

        soporte.image = pygame.image.load("SolarAdventures/src/images/soporteVital.png")
        soporte.rect = soporte.image.get_rect()

        soporte.rect.x = 100
        soporte.rect.y = 100

        spritesJuego.add(soporte)

        return soporte
    #Funcion para crear el generador de agua
    def crearGeneradorAgua(self,spritesJuego):
        generador = pygame.sprite.Sprite()

        generador.image = pygame.image.load("SolarAdventures/src/images/GeneradorDeAgua.png")
        generador.rect = generador.image.get_rect()

        generador.rect.x = 100
        generador.rect.y = 100

        spritesJuego.add(generador)

        return generador
    #Funcion para crear el game over por vida 0
    def gameOverVida(self,sprites):
        
        gameOver = pygame.sprite.Sprite()

        gameOver.image = pygame.image.load("SolarAdventures/src/images/finJuegoVida.png")
        gameOver.rect = gameOver.image.get_rect()

        gameOver.rect.x = 100
        gameOver.rect.y = 100

        sprites.add(gameOver)
        return gameOver
    #Funcion para crear la info sobre jupiter
    def nivelJupiter(self,sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("SolarAdventures/src/images/nivelJupiter.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
    #Funcion para crear la info sobre la decision que tomar en jupiter
    def crearDecisionJupiter(self,spritesJuego):
        decision = pygame.sprite.Sprite()

        decision.image = pygame.image.load("SolarAdventures/src/images/decidirEnJupiter.png")
        decision.rect = decision.image.get_rect()
        
        decision.rect.x = 100
        decision.rect.y = 100

        spritesJuego.add(decision)

        return decision
    #Funcion para crear el cristal de atmosfera
    def crearCristal(self,spritesJuego):
        cristal = pygame.sprite.Sprite()

        cristal.image = pygame.image.load("SolarAdventures/src/images/CristalDeAtmosfera.png")
        cristal.rect = cristal.image.get_rect()

        cristal.rect.x = 100
        cristal.rect.y = 100

        spritesJuego.add(cristal)

        return cristal
    #Funcion para crear el distribuidor de energia
    def crearDistribuidor(self,spritesJuego):
        distribuidor = pygame.sprite.Sprite()

        distribuidor.image = pygame.image.load("SolarAdventures/src/images/distribuidorDeEnergia.png")
        distribuidor.rect = distribuidor.image.get_rect()

        distribuidor.rect.x = 100
        distribuidor.rect.y = 100

        spritesJuego.add(distribuidor)

        return distribuidor
    #Funcion para crear la primera escena en el espacio
    def crearEscenaEspacio (self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escena1Meteoritos.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la segunda escena en el espacio
    def crearEscenaEspacio2(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escena2Meteoritos.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la escena de la zona de jupiter
    def crearEscenaEspacioJupiter(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/decisionJupiter.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la nave en el espacio
    def crearNaveEnMovimiento(self,spritesJuego):
        naveMov = pygame.sprite.Sprite()

        naveMov.spriteSheet = pygame.image.load("SolarAdventures/src/images/spriteSheetNave.png")
        self.frames.cargarFramesNaveDerecha(naveMov)
        self.frames.cargarFramesNaveIzquierda(naveMov)
        self.frames.cargarFramesNaveArriba(naveMov)
        self.frames.cargarFramesNaveAbajo(naveMov)

        naveMov.rect.x= 700
        naveMov.rect.y = 400

        naveMov.velocidad_x = 0
        naveMov.velocidad_y = 0

        spritesJuego.add(naveMov)
        return naveMov
    #Funcion para crear el primer meteorito
    def crearMeteoritoSimple(self,spritesJuego):
        meteorito = pygame.sprite.Sprite()

        meteorito.image = pygame.image.load("SolarAdventures/src/images/meteorito1.png")
        meteorito.rect = meteorito.image.get_rect()

        meteorito.rect.x = 550
        meteorito.rect.y=0

        spritesJuego.add(meteorito)

        return meteorito
    #Funcion para crear el segundo meteorito
    def crearMeteoritoAlargado(self,spritesJuego):
        meteorito = pygame.sprite.Sprite()

        meteorito.image = pygame.image.load("SolarAdventures/src/images/meteorito2.png")
        meteorito.rect = meteorito.image.get_rect()

        meteorito.rect.x = 350
        meteorito.rect.y=0

        spritesJuego.add(meteorito)

        return meteorito
    #Funcion para crear el tercer meteorito
    def crearMeteoritoAncho(self,spritesJuego):
        meteorito = pygame.sprite.Sprite()

        meteorito.image = pygame.image.load("SolarAdventures/src/images/meteorito3.png")
        meteorito.rect = meteorito.image.get_rect()

        meteorito.rect.x = 150
        meteorito.rect.y=0

        spritesJuego.add(meteorito)

        return meteorito
    #Funcion para crear el cuarto meteorito
    def crearMeteoritoGrande(self,spritesJuego):
        meteorito = pygame.sprite.Sprite()

        meteorito.image = pygame.image.load("SolarAdventures/src/images/meteoritoGrande.png")
        meteorito.rect = meteorito.image.get_rect()

        meteorito.rect.x = 200
        meteorito.rect.y=0

        spritesJuego.add(meteorito)

        return meteorito
    #Funcion para crear la info de urano
    def nivelUrano(self,sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("SolarAdventures/src/images/nivelUrano.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
    #Funcion para crear la escena central de urano
    def crearEscenaCentralUrano(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaUranoCentral.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la escena cruce de urano
    def crearEscenaUranoCruce(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaUranoCruce.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la escena de arriba de urano
    def crearEscenaUranoArriba(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaUranoArriba.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la escena de abajo de urano
    def crearEscenaUranoAbajo(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaUranoAbajo.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear las bolas de hidrogeno
    def crearBolaHidrogeno(self,spritesJuego):
        bola = pygame.sprite.Sprite()

        bola.image = pygame.image.load("SolarAdventures/src/images/simboloHidrogeno.png")
        bola.rect = bola.image.get_rect()

        bola.rect.x = 0
        bola.rect.y = 0

        spritesJuego.add(bola)

        return bola
    #Funcion para crear el traje antipresion
    def crearTrajeAntiPresion(self,spritesJuego):
        traje = pygame.sprite.Sprite()

        traje.image = pygame.image.load("SolarAdventures/src/images/trajeAntiPresion.png")
        traje.rect = traje.image.get_rect()

        traje.rect.x = 100
        traje.rect.y = 100

        spritesJuego.add(traje)

        return traje
    #Funcion para crear la info sobre pluton
    def nivelPluton(self,sprites):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("SolarAdventures/src/images/nivelPluton.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        sprites.add(nivel)
        return nivel
    #Funcion para crear la info sobre pluton
    def crearNivelPluton(self,spritesJuego):
        nivel = pygame.sprite.Sprite()

        nivel.image = pygame.image.load("SolarAdventures/src/images/nivelPluton.png")
        nivel.rect = nivel.image.get_rect()

        nivel.rect.x = 100
        nivel.rect.y = 100

        spritesJuego.add(nivel)

        return nivel
    #Funcion para crear los suministros de baja vida contra el jefe
    def crearMedicamento(self,spritesJuego):
        medicamento = pygame.sprite.Sprite()

        medicamento.image = pygame.image.load("SolarAdventures/src/images/medicamento.png")
        medicamento.rect = medicamento.image.get_rect()

        medicamento.rect.x = 0
        medicamento.rect.y = 0

        spritesJuego.add(medicamento)
        return medicamento
    #Funcion para crear la mira explosiva
    def crearMira(self,spritesJuego):
        mira = pygame.sprite.Sprite()

        mira.image = pygame.image.load("SolarAdventures/src/images/mira.png")
        mira.rect = mira.image.get_rect()

        mira.rect.x = 0
        mira.rect.y = 0

        spritesJuego.add(mira)
        return mira
    #Funcion para crear la explosion
    def crearExplosion(self,spritesJuego):
        explosion = pygame.sprite.Sprite()

        explosion.image = pygame.image.load("SolarAdventures/src/images/explosion.png")
        explosion.rect = explosion.image.get_rect()

        explosion.rect.x = 0
        explosion.rect.y = 0

        spritesJuego.add(explosion)
        return explosion
    #Funcion para crear la escena central de pluton
    def crearEscenaCentralPluton(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaPlutonCentral.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la escena del jefe en pluton
    def crearEscenaJefePluton(self,spritesJuego):
        escena = pygame.sprite.Sprite()

        escena.image = pygame.image.load("SolarAdventures/src/images/escenaBossPluton.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 0
        escena.rect.y = 0

        spritesJuego.add(escena)

        return escena
    #Funcion para crear la bala que dispara el jefe
    def crearBalaMaligna(self,spritesJuego):
        bala = pygame.sprite.Sprite()

        bala.image = pygame.image.load("SolarAdventures/src/images/proyectilOscuro.png")
        bala.rect = bala.image.get_rect()

        bala.rect.x = 0
        bala.rect.y = 0

        spritesJuego.add(bala)

        return bala
    #Funcion para crear al jefe final
    def crearJefeFinal(self,spritesJuego):
        jefe = pygame.sprite.Sprite()

        jefe.spriteSheet = pygame.image.load("SolarAdventures/src/images/bossFinal.png").convert()
        self.frames.cargarFramesJefeDerecha(jefe)
        self.frames.cargarFramesJefeIzquierda(jefe)
        self.frames.cargarFramesJefeAbajo(jefe)

        jefe.velocidad_x = 1
        spritesJuego.add(jefe)

        return jefe
    #Funcion para crear el game over por falta de gasolina
    def crearGameOverGasolina(self,spritesJuego):
        fin = pygame.sprite.Sprite()

        fin.image = pygame.image.load("SolarAdventures/src/images/finJuegoGasolina.png")
        fin.rect = fin.image.get_rect()

        fin.rect.x = 100
        fin.rect.y = 100

        spritesJuego.add(fin)

        return fin 
    #Funcion para crear el gameover por meteoritos
    def crearGameOverMeteoritos(self,spritesJuego):
        fin = pygame.sprite.Sprite()

        fin.image = pygame.image.load("SolarAdventures/src/images/finJuegoMeteoritos.png")
        fin.rect = fin.image.get_rect()

        fin.rect.x = 100
        fin.rect.y = 100

        spritesJuego.add(fin)

        return fin 
    #Funcion para crear el gameover por entrar a jupiter
    def crearGameOverEntrarJupiter(self,spritesJuego):
        fin = pygame.sprite.Sprite()

        fin.image = pygame.image.load("SolarAdventures/src/images/finJuegoEntrarJupiter.png")
        fin.rect = fin.image.get_rect()

        fin.rect.x = 100
        fin.rect.y = 100

        spritesJuego.add(fin)

        return fin
    #Funcion para crear el game over por el jefe final
    def crearGameOverJefeFinal(self,sprites):
        fin = pygame.sprite.Sprite()

        fin.image = pygame.image.load("SolarAdventures/src/images/finJuegoJefeFinal.png")
        fin.rect = fin.image.get_rect()

        fin.rect.x = 100
        fin.rect.y = 100

        sprites.add(fin)

        return fin
    #Funcion para crear la info de los controles
    def crearControles(self,sprite):
        escena = pygame.sprite.Sprite()
        escena.image = pygame.image.load("SolarAdventures/src/images/controles.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 100
        escena.rect.y = 100

        sprite.add(escena)
        return escena
    #Funcion para crear la pantalla de victoria
    def ganacion(self,sprite):
        escena = pygame.sprite.Sprite()
        escena.image = pygame.image.load("SolarAdventures/src/images/Ganacion.png")
        escena.rect = escena.image.get_rect()

        escena.rect.x = 100
        escena.rect.y = 100

        sprite.add(escena)
        return escena