import pygame
import random
import asyncio
from framesPersonaje import Frames
from mensajesJuego import Texto
from imagenes import cargarImagen
from mensajesFolletos import cargarMensajes
from cambiosDeEscena import cambioEscena
from interaccionesJuego import iteracciones
from colisionesJuego import Colisiones
from misionesPlanetas import misiones
from misionesPlanetasTexto import misionesTexto
from finJuego import gameOvers
async def main():
    #Ancho y largo de la ventana
    ANCHO = 1200
    LARGO = 800
    #definimos los colores
    negro = pygame.Color(0,0,0)
    blanco = pygame.Color(255,255,255)
    rojo = pygame.Color(255,0,0)
    verde = pygame.Color(0,255,0)                             
    azul = pygame.Color(0,0,255)
    naranja = pygame.Color(255,120,0)
    dorado = pygame.Color(212,175,55)
    bidonGasofa = pygame.Color(149,49,21)
    gris = pygame.Color(155,155,155) 
    def gestionarEventos(protagonista,derecha,izquierda,arriba,abajo,trajeAP):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_d]):
            if(trajeAP):
                protagonista.rect.x+=3
            else:
                protagonista.rect.x+=2
            derecha = 1
            izquierda = 0
            arriba = 0
            abajo = 0
        if(teclaPulsada[pygame.K_a]):
            if(trajeAP):
                protagonista.rect.x-=3
            else:
                protagonista.rect.x-=2
            derecha = 0
            izquierda = 1
            arriba = 0
            abajo = 0
        if(teclaPulsada[pygame.K_s]):
            if(trajeAP):
                protagonista.rect.y+=3
            else:
                protagonista.rect.y+=2
            derecha = 0
            izquierda = 0
            arriba = 0
            abajo = 1
        if(teclaPulsada[pygame.K_w]):
            if(trajeAP):
                protagonista.rect.y-=3
            else:
                protagonista.rect.y-=2
            derecha = 0
            izquierda = 0
            arriba = 1
            abajo = 0
        return derecha,izquierda,arriba,abajo
    def gestionarEventosMapa(flecha,mapa):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_LEFT]):
            flecha.rect.x-=4
        elif(teclaPulsada[pygame.K_RIGHT]):
            flecha.rect.x+=4
        elif(teclaPulsada[pygame.K_ESCAPE]):
            mapa=False
        return mapa  
    def disparar(screen,protagonista,pintarBala,bala,balas,recargar):
        teclaPulsada = pygame.key.get_pressed()
        if(balas>0):
            if(recargar==True):
                pintarBala.rect.x = protagonista.rect.x+20
                pintarBala.rect.y = protagonista.rect.y   
            if((teclaPulsada[pygame.K_q] or teclaPulsada[pygame.K_SPACE]) and recargar==True):
                balas-=1
                recargar=False
            if(recargar==False):
                bala.draw(screen)
                pintarBala.rect.y-=22
                if(pintarBala.rect.y<-10):
                    recargar=True
        return balas,recargar   
    def gestionarEventosNave(protagonista,derecha,izquierda,arriba,abajo):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_d]):
            protagonista.rect.x+=1
            derecha = 1
            izquierda = 0
            arriba = 0
            abajo = 0
        if(teclaPulsada[pygame.K_a]):
            protagonista.rect.x-=1
            derecha = 0
            izquierda = 1
            arriba = 0
            abajo = 0
        if(teclaPulsada[pygame.K_s]):
            protagonista.rect.y+=1
            derecha = 0
            izquierda = 0
            arriba = 0
            abajo = 1
        if(teclaPulsada[pygame.K_w]):
            protagonista.rect.y-=1
            derecha = 0
            izquierda = 0
            arriba = 1
            abajo = 0
        return derecha,izquierda,arriba,abajo
    def gestionarEventosMeteoritos(meteorito1,meteorito2,meteorito3,meteorito4):
        if(meteorito1.rect.y>600):
            meteorito1.rect.y+=6
        else:
             meteorito1.rect.y+=4
        if(meteorito2.rect.y>450):
            meteorito2.rect.y+=5
        else:
            meteorito2.rect.y+=3
        if(meteorito2.rect.y>400):
            meteorito3.rect.y+=3
        else:
            meteorito3.rect.y+=2
        if(meteorito4.rect.y>350):
            meteorito4.rect.y+=4
        else:
            meteorito4.rect.y+=2
        if(meteorito1.rect.y>790):
            meteorito1.rect.y = -40
        if(meteorito2.rect.y>790):
            meteorito2.rect.y = -40
        if(meteorito3.rect.y>790):
            meteorito3.rect.y = -40
        if(meteorito4.rect.y>790):
            meteorito4.rect.y = -150

    #-----------------Inicializacion pygame-----------------#
    pygame.init()
    screen = pygame.display.set_mode([ANCHO,LARGO])
    contadorNivel=0
    #------------------Astronauta y movimiento --------------#
    astronauta = pygame.sprite.Group()
    protagonista = cargarImagen.crearAstronauta(astronauta)
    astronautaEnPlaneta = pygame.sprite.Group()
    protagonistaEnPlaneta = cargarImagen.crearAstronautaPlaneta(astronautaEnPlaneta)
    derecha = 0 
    izquierda = 0 
    arriba = 0 
    abajo = 0 
    bala = pygame.sprite.Group()
    pintarBala = cargarImagen.crearBalas(bala)
    recargar = True
    #------------------Nave y movimiento-----------------#
    nave = pygame.sprite.Group()
    pintarNave = cargarImagen.crearNave(nave)
    #------------------Estadisticas----------------------#
    vida = 100
    balas = 0
    gasolina = 100
    arreglo = 100
    bidones = 0
    piezas = 0
    contadorIteraccion = 0
    estadisticas = pygame.sprite.Group()
    #------------------Informacion planetas--------------#
    infoSol = pygame.sprite.Group()
    pintarSol = cargarImagen.infoSol(infoSol)
    infoMercurio = pygame.sprite.Group()
    pintarMercurio = cargarImagen.infoMercurio(infoMercurio)
    infoVenus = pygame.sprite.Group()
    pintarVenus = cargarImagen.infoVenus(infoVenus)
    infoTierra = pygame.sprite.Group()
    pintarTierra = cargarImagen.infoTierra(infoTierra)
    infoMarte = pygame.sprite.Group()
    pintarMarte = cargarImagen.infoMarte(infoMarte)
    infoJupiter = pygame.sprite.Group()
    pintarJupiter = cargarImagen.infoJupiter(infoJupiter)
    infoSaturno = pygame.sprite.Group()
    pintarSaturno = cargarImagen.infoSaturno(infoSaturno)
    infoUrano = pygame.sprite.Group()
    pintarUrano = cargarImagen.infoUrano(infoUrano)
    infoNeptuno = pygame.sprite.Group()
    pintarNeptuno = cargarImagen.infoNeptuno(infoNeptuno)
    infoPluton = pygame.sprite.Group()
    pintarPluton = cargarImagen.infoPluton(infoPluton)
    
    #------------------Escena nave-----------------------#
    escenaComienzo = pygame.sprite.Group()
    pintarComienzo = cargarImagen.crearComienzo(escenaComienzo)
    escenaControles = pygame.sprite.Group()
    pintarControles = cargarImagen.crearControles(escenaControles)
    salirControles = False
    salirComienzo = False
    escenaNaveCentral = pygame.sprite.Group()
    pintarNave1 = cargarImagen.escenaNave1(escenaNaveCentral)
    escenaNaveIzquierda = pygame.sprite.Group()
    pintarNave2 = cargarImagen.escenaNave2(escenaNaveIzquierda)
    escenaNaveAbajo = pygame.sprite.Group()
    pintarNave3 = cargarImagen.escenaNave3(escenaNaveAbajo)
    mapaEspacio = pygame.sprite.Group()
    pintarMapa = cargarImagen.crearMapa(mapaEspacio)
    flechaMapa = pygame.sprite.Group()
    pintarFlecha = cargarImagen.crearFlecha(flechaMapa)
    escenaNave1 = True
    escenaNave2 = False
    escenaNave3 = False
    #------------------Escena luna-----------------------#
    salirNivelLuna = False
    nivelLuna = pygame.sprite.Group()
    pintarNivelLuna = cargarImagen.nivelLuna(nivelLuna)
    escenaLuna1 = pygame.sprite.Group()
    pintarLuna1 = cargarImagen.escenaLuna1(escenaLuna1)
    escenaLuna2 = pygame.sprite.Group()
    pintarLuna2 = cargarImagen.escenaLuna2(escenaLuna2)
    escenaLuna3 = pygame.sprite.Group()
    pintarLuna3 = cargarImagen.escenaLuna3(escenaLuna3)
    escenaLuna4 = pygame.sprite.Group()
    pintarLuna4 = cargarImagen.escenaLuna4(escenaLuna4)
    escenaLuna5 = pygame.sprite.Group()
    pintarLuna5 = cargarImagen.escenaLuna5(escenaLuna5)
    escenaLuna6 = pygame.sprite.Group()
    pintarLuna6 = cargarImagen.escenaLuna6(escenaLuna6)
    propulsor = pygame.sprite.Group()
    pintarPropulsor = cargarImagen.propulsorLuz(propulsor)
    bidon = pygame.sprite.Group()
    pintarBidon = cargarImagen.crearBidonGasofa(bidon)
    pieza = pygame.sprite.Group()
    pintarPieza = cargarImagen.crearPiezas(pieza)
    inyector = pygame.sprite.Group()
    pintarInyector = cargarImagen.crearInyector(inyector)
    luna1 = True
    luna2 = False
    luna3 = False
    luna4 = False
    luna5 = False
    luna6 = False
    volverNave = False
    cogerPieza = False
    cogerBidon = False
    cogerPropulsor = False
    mostrarInyector = False
    secretoLuna = False
    #------------Escena marte---------------------------#
    salirNivelMarte = False
    nivelMarte = pygame.sprite.Group()
    pintarNivelMarte = cargarImagen.nivelMarte(nivelMarte)
    escena1_1 = pygame.sprite.Group()
    pintarEscena1_1 = cargarImagen.escenaMarte1(escena1_1)
    escena1_2 = pygame.sprite.Group()
    pintarEscena1_2 = cargarImagen.escenaMarte2(escena1_2)
    escena1_3 = pygame.sprite.Group()
    pintarEscena1_3 = cargarImagen.escenaMarte3(escena1_3)
    escena1_4 = pygame.sprite.Group()
    pintarEscena1_4 = cargarImagen.escenaMarte4(escena1_4)
    escena2_1 = pygame.sprite.Group()
    pintarEscena2_1 = cargarImagen.escenaMarte5(escena2_1)
    escena2_2 = pygame.sprite.Group()
    pintarEscena2_2 = cargarImagen.escenaMarte6(escena2_2)
    escena2_3 = pygame.sprite.Group()
    pintarEscena2_3 = cargarImagen.escenaMarte7(escena2_3)
    escena2_4 = pygame.sprite.Group()
    pintarEscena2_4 = cargarImagen.escenaMarte8(escena2_4)
    escena3_1 = pygame.sprite.Group()
    pintarEscena3_1 = cargarImagen.escenaMarte9(escena3_1)
    escena3_2 = pygame.sprite.Group()
    pintarEscena3_2 = cargarImagen.escenaMarte10(escena3_2)
    escena3_3 = pygame.sprite.Group()
    pintarEscena3_3 = cargarImagen.escenaMarte11(escena3_3)
    cartaParaiso1 = pygame.sprite.Group()
    carta1 = cargarImagen.CrearCartaSecretaMarte(cartaParaiso1)
    cartaParaiso2 = pygame.sprite.Group()
    carta2 = cargarImagen.CrearCartaSecretaMarte2(cartaParaiso2)
    cartaParaiso3 = pygame.sprite.Group()
    carta3 = cargarImagen.crearPrimerMensajeParaiso(cartaParaiso3)
    cartaParaiso4 = pygame.sprite.Group()
    carta4 = cargarImagen.crearSegundoMensajeParaiso(cartaParaiso4)
    escenaParaiso1 = pygame.sprite.Group()
    pintarEsPar1 = cargarImagen.CrearPrimeraEscenaParaiso(escenaParaiso1)
    escenaParaiso2 = pygame.sprite.Group()
    pintarEsPar2 = cargarImagen.CrearElParaiso(escenaParaiso2)
    mensajeSoporteVital = pygame.sprite.Group()
    pintarSoporteVital = cargarImagen.crearSoporteVital(mensajeSoporteVital)
    generador = pygame.sprite.Group()
    pintarGenerador = cargarImagen.crearGeneradorAgua(generador)
    marte1 = False
    marte2 = False
    marte3 = False
    marte4 = False
    marte5 = False
    marte6 = True
    marte7 = False
    marte8 = False
    marte9 = False
    marte10 = False
    marte11= False
    cogerPieza2 = False
    cogerPieza3 = False
    cogerPieza4 = False
    cogerBidon2 = False
    entrarParaiso = False
    primeraParaiso = False
    segundaParaiso = False
    paraiso = False
    mostrarCarta = False
    saquear = False
    mostrarSoporte = False
    soporteVital = False
    generadorAgua = False
    #-----------Escena jupiter--------------------------#
    salirNivelJupiter = False
    naveMovimiento = pygame.sprite.Group()
    naveMov = cargarImagen.crearNaveEnMovimiento(naveMovimiento)
    nivelJupiter = pygame.sprite.Group()
    pintarNivelJupiter = cargarImagen.nivelJupiter(nivelJupiter)
    escenaEspacio1 = pygame.sprite.Group()
    pintarEspacio1 = cargarImagen.crearEscenaEspacio(escenaEspacio1)
    escenaEspacio2 = pygame.sprite.Group()
    pintarEspacio2 = cargarImagen.crearEscenaEspacio2(escenaEspacio2)
    escenaEspacio3 = pygame.sprite.Group()
    pintarEspacio3 = cargarImagen.crearEscenaEspacioJupiter(escenaEspacio3)
    decision = pygame.sprite.Group()
    pintarDecision = cargarImagen.crearDecisionJupiter(decision)
    cristalEnergia = pygame.sprite.Group()
    pintarCristal = cargarImagen.crearCristal(cristalEnergia)
    distribuidorEnergia = pygame.sprite.Group()
    pintarDistribuidor = cargarImagen.crearDistribuidor(distribuidorEnergia)
    meteoritoPequeño = pygame.sprite.Group()
    meteorito1 = cargarImagen.crearMeteoritoSimple(meteoritoPequeño)
    meteoritoAlargado = pygame.sprite.Group()
    meteorito2 = cargarImagen.crearMeteoritoAlargado(meteoritoAlargado)
    meteoritoAncho = pygame.sprite.Group()
    meteorito3 = cargarImagen.crearMeteoritoAncho(meteoritoAncho)
    meteoritoGrande = pygame.sprite.Group()
    meteorito4 = cargarImagen.crearMeteoritoGrande(meteoritoGrande)
    espacio1 = False
    espacio2 = False
    espacio3 = False
    cristal = False
    distribuidor = False
    decidir = 0
    #------------Escena Urano---------------------------#
    salirNivelUrano = False
    nivelUrano = pygame.sprite.Group()
    pintarNivelUrano = cargarImagen.nivelUrano(nivelUrano)
    escenaUrano1 = pygame.sprite.Group()
    pintarUrano1 = cargarImagen.crearEscenaCentralUrano(escenaUrano1)
    escenaUrano2 = pygame.sprite.Group()
    pintarUrano2 = cargarImagen.crearEscenaUranoCruce(escenaUrano2)
    escenaUrano3 = pygame.sprite.Group()
    pintarUrano3 = cargarImagen.crearEscenaUranoArriba(escenaUrano3)
    escenaUrano4 = pygame.sprite.Group()
    pintarUrano4 = cargarImagen.crearEscenaUranoAbajo(escenaUrano4)
    bolaHidrogeno = pygame.sprite.Group()
    pintarHidrogeno = cargarImagen.crearBolaHidrogeno(bolaHidrogeno)
    trajeAntiPresion = pygame.sprite.Group()
    pintarTraje = cargarImagen.crearTrajeAntiPresion(trajeAntiPresion)
    trajeAP = False
    hidrogeno = 0
    urano1 = False
    urano2 = False
    urano3 = False
    urano4 = False
    contadorHidrogeno = 0
    contadorEspera = 0
    cogerHidrogeno = False
    #------------Escena Pluton--------------------------#
    salirNivelPluton = False
    nivelPluton = pygame.sprite.Group()
    pintarNivelPluton = cargarImagen.nivelPluton(nivelPluton)
    escenaPluton1 = pygame.sprite.Group()
    pintarPluton1 = cargarImagen.crearEscenaCentralPluton(escenaPluton1)
    escenaPluton2 = pygame.sprite.Group()
    pintarPluton2 = cargarImagen.crearEscenaJefePluton(escenaPluton2)
    jefe = pygame.sprite.Group()
    antagonista = cargarImagen.crearJefeFinal(jefe)
    balaOscura = pygame.sprite.Group()
    pintarBalaOscura = cargarImagen.crearBalaMaligna(balaOscura) 
    crearExplosion = pygame.sprite.Group()
    pintarExplosion = cargarImagen.crearExplosion(crearExplosion)
    crearMira = pygame.sprite.Group()
    pintarMira = cargarImagen.crearMira(crearMira)
    crearMedicamento = pygame.sprite.Group()
    pintarMedicamento = cargarImagen.crearMedicamento(crearMedicamento)  
    ganacion = pygame.sprite.Group()
    pintarGanacion = cargarImagen.ganacion(ganacion)
    pluton1 = True
    pluton2 = False
    vidaJefe = 100
    contadorDisparo = 0
    disparoMaligno = False
    disparo = False
    ataqueEspecial=False
    contadorMira = 0
    contadorExplosion = 0
    contadorAtaqueEspecial = 0
    derechaJefe = 0
    izquierdaJefe = 0
    contadorMensaje = 0
    #------------Planetas y misiones--------------------#
    faseInicial = True
    mapa = False
    luna = False
    marte = False
    jupiter = False
    urano = False
    pluton = False
    primeraMision = False
    segundaMision = False
    terceraMision = False
    cuartaMision = False
    quintaMision = False
    #----------Game overs-------------------------------#
    gameOverVida = pygame.sprite.Group()
    pintarFinVida = cargarImagen.gameOverVida(gameOverVida)
    gameOverJupiter = pygame.sprite.Group()
    pintarFinJupiter = cargarImagen.crearGameOverEntrarJupiter(gameOverJupiter)
    gameOverArreglos = pygame.sprite.Group()
    pintarFinArreglos = cargarImagen.crearGameOverMeteoritos(gameOverArreglos)
    gameOverGasolina = pygame.sprite.Group()
    pintarFinGasolina = cargarImagen.crearGameOverGasolina(gameOverGasolina)
    gameOverJefe = pygame.sprite.Group()
    pintarFinJefe = cargarImagen.crearGameOverJefeFinal(gameOverJefe)
    finVida = False
    finGasolina = False
    finArreglos = False
    finEntrarJupiter = False
    finMarte = False
    finJupiter = False
    finUrano = False
    finPluton = False
    resetear = False
    funcionando = True
    contadorFinJuego = 0
    while funcionando:
        screen.fill(negro)
        for evento in pygame.event.get():
            if(evento.type == pygame.QUIT):
                funcionando = False
        
        if(finVida==True):
            gameOverVida.draw(screen)
            if(finMarte==True and resetear==False):
                salirNivelMarte,marte,contadorNivel,resetear,vida,funcionando=gameOvers.empezarPorVida(salirNivelMarte,marte,contadorNivel,resetear,vida,funcionando)
            if(finUrano==True and resetear==False):
                salirNivelUrano,urano,contadorNivel,resetear,vida,funcionando=gameOvers.empezarPorVida(salirNivelUrano,urano,contadorNivel,resetear,vida,funcionando)
        if(finVida==True and finPluton==True):
            gameOverJefe.draw(screen)
            salirNivelPluton,pluton,contadorNivel,resetear,vida,funcionando=gameOvers.empezarPorVida(salirNivelPluton,pluton,contadorNivel,resetear,vida,funcionando)
            contadorExplosion = 0
            contadorMira = 0
            vidaJefe = 100
            contadorAtaqueEspecial = 0
        if(finGasolina==True):
            gameOverGasolina.draw(screen)
            if(finJupiter==True and resetear==False):
                if(contadorFinJuego==200):
                    salirNivelMarte,marte,contadorNivel,resetear,funcionando=gameOvers.empezarPorGasolina(salirNivelMarte,marte,contadorNivel,resetear,funcionando)
                if(contadorFinJuego!=200):
                    contadorFinJuego+=1 
            if(finUrano==True and resetear==False):
                if(contadorFinJuego==200):
                    salirNivelJupiter,jupiter,contadorNivel,resetear,funcionando=gameOvers.empezarPorGasolina(salirNivelJupiter,jupiter,contadorNivel,resetear,funcionando)
                if(contadorFinJuego!=200):
                    contadorFinJuego+=1
            if(finPluton==True and resetear==False):
                if(contadorFinJuego==200):
                    salirNivelUrano,urano,contadorNivel,resetear,funcionando=gameOvers.empezarPorGasolina(salirNivelUrano,urano,contadorNivel,resetear,funcionando)
                if(contadorFinJuego!=200):
                    contadorFinJuego+=1
        if(finArreglos==True):
            gameOverArreglos.draw(screen)
            if(finJupiter==True and resetear==False):
                salirNivelJupiter,jupiter,contadorNivel,resetear,arreglo,funcionando = gameOvers.empezarPorArreglos(salirNivelJupiter,jupiter,contadorNivel,resetear,arreglo,funcionando)
        if(finEntrarJupiter==True):
            gameOverJupiter.draw(screen)
            if(finJupiter==True and resetear==False):
                salirNivelJupiter,jupiter,contadorNivel,resetear,funcionando = gameOvers.empezarPorJupiter(salirNivelJupiter,jupiter,contadorNivel,resetear,funcionando)
        if(salirComienzo==False):
            escenaComienzo.draw(screen)
            salirComienzo = cargarMensajes.comienzo(salirComienzo)
        elif(salirControles==False and salirComienzo==True):
            escenaControles.draw(screen)
            salirControles,contadorNivel = cargarMensajes.controles(salirControles,contadorNivel)
        elif(faseInicial==True and luna == False and marte==False and jupiter==False and urano==False and pluton==False):
            if(mapa==False):
                if(escenaNave1):
                    escenaNaveCentral.draw(screen)
                if(escenaNave2):
                    escenaNaveIzquierda.draw(screen)
                if(escenaNave3):
                    escenaNaveAbajo.draw(screen)
                balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa = iteracciones.iteraccionesNave(screen,protagonista,balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa,distribuidor)
                astronauta.draw(screen)
                derecha,izquierda,arriba,abajo = gestionarEventos(protagonista,derecha,izquierda,arriba,abajo,trajeAP)
                balas,recargar = disparar(screen,protagonista,pintarBala,bala,balas,recargar)
                Colisiones.colisionNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                escenaNave1,escenaNave2,escenaNave3 = cambioEscena.cambioEcenaNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                misionesTexto.misionInicial(screen,primeraMision)
            if(mapa==True):
                mapaEspacio.draw(screen)
                flechaMapa.draw(screen)
                mapa=gestionarEventosMapa(pintarFlecha,mapa)
                Colisiones.colisionesMapa(pintarFlecha)
                Texto.mensajesMapa(screen,pintarFlecha,primeraMision,segundaMision,terceraMision,cuartaMision,quintaMision)
                iteracciones.iteraccionesMapa(screen,pintarFlecha,infoSol,infoMercurio,infoVenus,infoTierra,infoMarte,infoJupiter,infoSaturno,infoUrano,infoNeptuno,infoPluton)
                luna,primeraMision,faseInicial = misiones.misionPrincipal(primeraMision,mapa,luna,faseInicial,pintarFlecha)
                misionesTexto.misionInicial(screen,primeraMision)
                if(faseInicial==False):
                    gasolina-=15
                    contadorNivel=0
                    salirNivelLuna = False
            estadisticas.draw(screen)
            estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
            Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
            Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
        elif(faseInicial==False and luna == True and marte==False and jupiter==False and urano==False and pluton==False):
            if(salirNivelLuna==False):
                nivelLuna.draw(screen)
                mapa = False
                escenaNave2=False
                escenaNave1 = True
                salirNivelLuna,contadorNivel = cargarMensajes.nivelLuna(salirNivelLuna,contadorNivel)
                pintarNave.rect.x = 450
                pintarNave.rect.y = 200
                protagonistaEnPlaneta.rect.x = 570
                protagonistaEnPlaneta.rect.y = 480
                protagonista.rect.x = 340
                protagonista.rect.y = 150
            elif(volverNave==False):
                if(luna1==True):
                    escenaLuna1.draw(screen)
                    nave.draw(screen)
                if(luna2==True):
                    escenaLuna2.draw(screen)
                if(luna3==True):
                    escenaLuna3.draw(screen)
                    if(cogerBidon==False):
                        bidon.draw(screen)
                if(luna4==True):
                    escenaLuna4.draw(screen)
                    if(cogerPieza==False):
                        pieza.draw(screen)
                if(luna5==True):
                    escenaLuna5.draw(screen)
                    if(cogerPropulsor==False):
                        propulsor.draw(screen)
                if(luna6==True):
                    escenaLuna6.draw(screen)
                astronautaEnPlaneta.draw(screen)
                derecha,izquierda,arriba,abajo = gestionarEventos(protagonistaEnPlaneta,derecha,izquierda,arriba,abajo,trajeAP)
                balas,recargar = disparar(screen,protagonistaEnPlaneta,pintarBala,bala,balas,recargar)
                volverNave,cogerPieza,piezas,cogerBidon,bidones,cogerPropulsor,secretoLuna,mostrarInyector = iteracciones.iteraccionesLuna(screen,protagonistaEnPlaneta,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escenaNave1,cogerBidon,cogerPieza,cogerPropulsor,bidones,piezas,secretoLuna,mostrarInyector,inyector)
                Colisiones.colisionesLuna(protagonistaEnPlaneta,pintarNave,luna1,luna2,luna3,luna4,luna5,luna6)
                luna1,luna2,luna3,luna4,luna5,luna6 = cambioEscena.cambioEscenaLuna(protagonistaEnPlaneta,luna1,luna2,luna3,luna4,luna5,luna6)
                estadisticas.draw(screen)
                estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                Frames.actualizarFrame(protagonistaEnPlaneta,derecha,izquierda,abajo,arriba)
                marte,luna,segundaMision = misiones.misionLuna(segundaMision,cogerPropulsor,mapa,marte,pintarFlecha,luna)
                misionesTexto.misionLuna(screen,segundaMision,mapa,volverNave)
                if(volverNave==True):
                    protagonista.rect.y  = 150
            else:
                if(mapa==False):
                    if(escenaNave1):
                        escenaNaveCentral.draw(screen)
                    if(escenaNave2):
                        escenaNaveIzquierda.draw(screen)
                    if(escenaNave3):
                        escenaNaveAbajo.draw(screen)
                    balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa = iteracciones.iteraccionesNave(screen,protagonista,balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa,distribuidor)
                    astronauta.draw(screen)
                    derecha,izquierda,arriba,abajo = gestionarEventos(protagonista,derecha,izquierda,arriba,abajo,trajeAP)
                    balas,recargar = disparar(screen,protagonista,pintarBala,bala,balas,recargar)
                    Colisiones.colisionNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                    escenaNave1,escenaNave2,escenaNave3 = cambioEscena.cambioEcenaNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                    volverNave,cogerPieza,piezas,cogerBidon,bidones,cogerPropulsor,secretoLuna,mostrarInyector = iteracciones.iteraccionesLuna(screen,protagonista,volverNave,luna1,luna2,luna3,luna4,luna5,luna6,escenaNave1,cogerBidon,cogerPieza,cogerPropulsor,bidones,piezas,secretoLuna,mostrarInyector,inyector)
                    estadisticas.draw(screen)
                    estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                    Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                    Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                    marte,luna,segundaMision = misiones.misionLuna(segundaMision,cogerPropulsor,mapa,marte,pintarFlecha,luna)
                    misionesTexto.misionLuna(screen,segundaMision,mapa,volverNave)
                    if(volverNave==False):
                        protagonistaEnPlaneta.rect.y = 490
                else:
                    mapaEspacio.draw(screen)
                    flechaMapa.draw(screen)
                    mapa=gestionarEventosMapa(pintarFlecha,mapa)
                    Colisiones.colisionesMapa(pintarFlecha)
                    Texto.mensajesMapa(screen,pintarFlecha,primeraMision,segundaMision,terceraMision,cuartaMision,quintaMision)
                    iteracciones.iteraccionesMapa(screen,pintarFlecha,infoSol,infoMercurio,infoVenus,infoTierra,infoMarte,infoJupiter,infoSaturno,infoUrano,infoNeptuno,infoPluton)
                    estadisticas.draw(screen)
                    estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                    Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                    Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                    marte,luna,segundaMision = misiones.misionLuna(segundaMision,cogerPropulsor,mapa,marte,pintarFlecha,luna)
                    misionesTexto.misionLuna(screen,segundaMision,mapa,volverNave)
                    contadorNivel = 0
        elif(faseInicial==False and luna == False and marte==True and jupiter==False and urano==False and pluton==False):
            if(salirNivelMarte==False):
                nivelMarte.draw(screen)
                mapa = False
                marte1 = False
                marte2 = False
                marte3 = False
                marte4 = False
                marte5 = False
                marte6 = True
                marte7 = False
                marte8 = False
                marte9 = False
                marte10 = False
                marte11 = False
                escenaNave2=False
                escenaNave1 = True
                soporteVital = False
                entrarParaiso=False
                cogerBidon=False
                cogerBidon2=False
                cogerPieza=False
                cogerPieza2=False
                cogerPieza3=False
                cogerPieza4=False
                entrarParaiso=False
                terceraMision=False
                generadorAgua=False
                paraiso = False
                salirNivelMarte,contadorNivel = cargarMensajes.nivelMarte(salirNivelMarte,contadorNivel)
                pintarNave.rect.x = 385
                pintarNave.rect.y = 320
                protagonistaEnPlaneta.rect.x = 500
                protagonistaEnPlaneta.rect.y = 590
                protagonista.rect.x = 340
                protagonista.rect.y = 150
                volverNave = False
                if(salirNivelMarte==True):
                    if(secretoLuna==True):
                        gasolina-=20
                    elif(secretoLuna==False):
                        gasolina-=30
                finMarte=False
                finVida=False
                finGasolina=False
            else:
                if(volverNave==False):
                    if(soporteVital==True):
                        vida-=0.01
                    elif(soporteVital==False):
                        vida-=0.03                       
                    if(primeraParaiso==True):
                        escenaParaiso1.draw(screen)
                    if(segundaParaiso==True):
                        escenaParaiso2.draw(screen)
                    if(marte1==True):
                        escena1_1.draw(screen)
                        if(cogerBidon==False):
                            bidon.draw(screen)
                            pintarBidon.rect.x = 190
                            pintarBidon.rect.y = 620
                    if(marte2==True):
                        escena1_2.draw(screen)
                    if(marte3==True):
                        escena1_3.draw(screen)
                        if(cogerPieza==False):
                            pieza.draw(screen)
                            pintarPieza.rect.x = 570
                            pintarPieza.rect.y = 540
                    if(marte4==True):
                        escena1_4.draw(screen)
                    if(marte5==True):
                        escena2_1.draw(screen)
                        if(cogerPieza2==False):
                            pieza.draw(screen)
                            pintarPieza.rect.x = 125
                            pintarPieza.rect.y = 615
                    if(marte6==True):
                        escena2_2.draw(screen)
                        nave.draw(screen)
                    if(marte7==True):
                        escena2_3.draw(screen)
                    if(marte8==True):
                        escena2_4.draw(screen)
                        if(cogerPieza3==False):
                            pieza.draw(screen)
                            pintarPieza.rect.x = 170
                            pintarPieza.rect.y = 660
                    if(marte9==True):
                        escena3_1.draw(screen)
                    if(marte10==True):
                        escena3_2.draw(screen)
                        if(cogerPieza4==False):
                            pieza.draw(screen)
                            pintarPieza.rect.x = 615
                            pintarPieza.rect.y = 435
                    if(marte11==True):
                        escena3_3.draw(screen)
                        if(cogerBidon2==False):
                            bidon.draw(screen)
                            pintarBidon.rect.x = 390
                            pintarBidon.rect.y = 390

                    astronautaEnPlaneta.draw(screen)
                    derecha,izquierda,arriba,abajo = gestionarEventos(protagonistaEnPlaneta,derecha,izquierda,arriba,abajo,trajeAP)
                    balas,recargar = disparar(screen,protagonistaEnPlaneta,pintarBala,bala,balas,recargar)
                    marte1,marte2,marte3,marte4,marte5,marte6,marte7,marte8,marte9,marte10,marte11,primeraParaiso,segundaParaiso = cambioEscena.cambioEscenaMarte(protagonistaEnPlaneta,marte1,marte2,marte3,marte4,marte5,marte6,marte7,marte8,marte9,marte10,marte11,paraiso,primeraParaiso,segundaParaiso)
                    Colisiones.colisionesMarte(protagonistaEnPlaneta,pintarNave,marte1,marte2,marte3,marte4,marte5,marte6,marte8,marte9,marte10,marte11,primeraParaiso,segundaParaiso)
                    bidones,piezas,cogerBidon,cogerBidon2,cogerPieza,cogerPieza2,cogerPieza3,cogerPieza4,volverNave,vida,mostrarCarta,entrarParaiso,paraiso,primeraParaiso = iteracciones.iteraccionesMarte(screen,protagonistaEnPlaneta,marte1,marte2,marte3,marte4,marte5,marte6,marte8,marte9,marte10,marte11,vida,bidones,piezas,cogerBidon,cogerBidon2,cogerPieza,cogerPieza2,cogerPieza3,cogerPieza4,volverNave,escenaNave1,escenaNave3,mostrarCarta,entrarParaiso,cartaParaiso1,cartaParaiso2,paraiso,primeraParaiso)
                    paraiso,mostrarSoporte,mostrarCarta,soporteVital,vida,piezas,saquear,marte4,primeraParaiso = iteracciones.iteraccionesParaiso(screen,protagonistaEnPlaneta,paraiso,primeraParaiso,segundaParaiso,mensajeSoporteVital,soporteVital,mostrarSoporte,mostrarCarta,vida,piezas,cartaParaiso3,cartaParaiso4,saquear,marte4)
                    estadisticas.draw(screen)
                    estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                    misionesTexto.misionMarte(screen,terceraMision,piezas,volverNave,mapa,entrarParaiso,soporteVital,paraiso,escenaNave3)
                    Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                    Frames.actualizarFrame(protagonistaEnPlaneta,derecha,izquierda,abajo,arriba)
                    if(volverNave==True):
                        protagonista.rect.y = 150
                    if(vida<0.5):
                        finVida=True
                        finMarte=True
                        marte=False
                        if(cogerPieza==True):
                            cogerPieza=False
                            piezas-=1
                        if(cogerPieza2==True):
                            cogerPieza2=False
                            piezas-=1
                        if(cogerPieza3==True):
                            cogerPieza3=False
                            piezas-=1
                        if(cogerPieza4==True):
                            cogerPieza4=False
                            piezas-=1
                        if(cogerBidon==True):
                            cogerBidon=False
                            bidones-=1
                        if(cogerBidon2==True):
                            cogerBidon2=False
                            bidones-=1
                        if(soporteVital==True):
                            soporteVital=False
                            piezas-=2
                        if(secretoLuna==True):
                            gasolina+=20
                        elif(secretoLuna==False):
                            gasolina+=30
                if(volverNave==True):
                    if(mapa==False):
                        if(escenaNave1):
                            escenaNaveCentral.draw(screen)
                        if(escenaNave2):
                            escenaNaveIzquierda.draw(screen)
                        if(escenaNave3):
                            escenaNaveAbajo.draw(screen)
                        balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa = iteracciones.iteraccionesNave(screen,protagonista,balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa,distribuidor)
                        astronauta.draw(screen)
                        derecha,izquierda,arriba,abajo = gestionarEventos(protagonista,derecha,izquierda,arriba,abajo,trajeAP)
                        balas,recargar = disparar(screen,protagonista,pintarBala,bala,balas,recargar)
                        Colisiones.colisionNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                        escenaNave1,escenaNave2,escenaNave3 = cambioEscena.cambioEcenaNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                        bidones,piezas,cogerBidon,cogerBidon2,cogerPieza,cogerPieza2,cogerPieza3,cogerPieza4,volverNave,vida,mostrarCarta,entrarParaiso,paraiso,primeraParaiso = iteracciones.iteraccionesMarte(screen,protagonista,marte1,marte2,marte3,marte4,marte5,marte6,marte8,marte9,marte10,marte11,vida,bidones,piezas,cogerBidon,cogerBidon2,cogerPieza,cogerPieza2,cogerPieza3,cogerPieza4,volverNave,escenaNave1,escenaNave3,mostrarCarta,entrarParaiso,cartaParaiso1,cartaParaiso2,paraiso,primeraParaiso)
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        jupiter,marte,terceraMision = misiones.misionMarte(terceraMision,generadorAgua,mapa,jupiter,pintarFlecha,marte)
                        misionesTexto.misionMarte(screen,terceraMision,piezas,volverNave,mapa,entrarParaiso,soporteVital,paraiso,escenaNave3)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                        generadorAgua,mostrarCarta,piezas = misiones.construirGenerador(screen,protagonista,volverNave,escenaNave3,generadorAgua,mostrarCarta,generador,piezas)
                        if(volverNave==False):
                            protagonistaEnPlaneta.rect.y = 580
                    else:
                        mapaEspacio.draw(screen)
                        flechaMapa.draw(screen)
                        mapa=gestionarEventosMapa(pintarFlecha,mapa)
                        Colisiones.colisionesMapa(pintarFlecha)
                        Texto.mensajesMapa(screen,pintarFlecha,primeraMision,segundaMision,terceraMision,cuartaMision,quintaMision)
                        iteracciones.iteraccionesMapa(screen,pintarFlecha,infoSol,infoMercurio,infoVenus,infoTierra,infoMarte,infoJupiter,infoSaturno,infoUrano,infoNeptuno,infoPluton)
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                        jupiter,marte,terceraMision = misiones.misionMarte(terceraMision,generadorAgua,mapa,jupiter,pintarFlecha,marte)
                        misionesTexto.misionMarte(screen,terceraMision,piezas,volverNave,mapa,entrarParaiso,soporteVital,paraiso,escenaNave3)
                        contadorNivel = 0
                        salirNivelJupiter = False
        elif(faseInicial==False and luna == False and marte==False and jupiter==True and urano==False and pluton==False):
            if(salirNivelJupiter==False):
                nivelJupiter.draw(screen)
                mapa = False
                escenaNave2 = False
                escenaNave1 = True
                espacio1 = True
                espacio3 = False
                espacio2 = False
                cristal = False
                distribuidor = False
                volverNave = False
                resetear = False
                arreglo = 100
                salirNivelJupiter,contadorNivel = cargarMensajes.nivelJupiter(salirNivelJupiter,contadorNivel)
                protagonista.rect.x = 340
                protagonista.rect.y = 150
                naveMov.rect.x= 700
                naveMov.rect.y = 400 
                if(salirNivelJupiter==True):
                    if(secretoLuna==True):
                        gasolina-=25
                    elif(secretoLuna==False):
                        gasolina-=40
                finJupiter = False
                if(finArreglos==True or finEntrarJupiter==True):
                    if(secretoLuna==True):
                        gasolina+=25
                    elif(secretoLuna==False):
                        gasolina+=40
                finArreglos = False
                finGasolina = False
                finEntrarJupiter = False
                if(gasolina<0):
                    finJupiter = True
                    finGasolina = True
                    jupiter = False
                    if(secretoLuna==True):
                        gasolina+=65
                    elif(secretoLuna==False):
                        gasolina+=100    
            else:
                if(volverNave==False):
                    if(espacio1):
                        escenaEspacio1.draw(screen)
                        meteoritoPequeño.draw(screen)
                        meteoritoAlargado.draw(screen)
                        meteoritoAncho.draw(screen)
                    if(espacio2):
                        escenaEspacio2.draw(screen)
                        meteoritoGrande.draw(screen)
                    if(espacio3):
                        escenaEspacio3.draw(screen)
                        naveMovimiento.draw(screen)
                        cristal,volverNave,jupiter,finJupiter,finEntrarJupiter = iteracciones.decision(screen,naveMov,cristal,volverNave,jupiter,finJupiter,finEntrarJupiter,decision)
                        mostrarCarta = True
                    if(espacio3==False):
                        naveMovimiento.draw(screen)
                    derecha,izquierda,arriba,abajo = gestionarEventosNave(naveMov,derecha,izquierda,arriba,abajo)
                    gestionarEventosMeteoritos(meteorito1,meteorito2,meteorito3,meteorito4)
                    espacio1,espacio2,espacio3 = cambioEscena.cambioEscenaJupiter(naveMov,espacio1,espacio2,espacio3)
                    Colisiones.colisionesNave(naveMov,espacio1,espacio3)
                    arreglo = Colisiones.colisionesConMeteorito(naveMov,meteorito1,meteorito2,meteorito4,meteorito3,arreglo,espacio1,espacio2,espacio3)
                    misionesTexto.misionJupiter(screen,naveMov,mapa,cuartaMision,volverNave,espacio3,cristal,distribuidor,escenaNave3)
                    if(arreglo>0):
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                    else:
                        finJupiter = True
                        finArreglos = True
                        jupiter = False
                        arreglo = 1  
                    Frames.actualizarFrame(naveMov,derecha,izquierda,abajo,arriba)
                elif(volverNave==True):
                    if(mapa==False):
                        if(escenaNave1):
                            escenaNaveCentral.draw(screen)
                        if(escenaNave2):
                            escenaNaveIzquierda.draw(screen)
                        if(escenaNave3):
                            escenaNaveAbajo.draw(screen)
                        balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa = iteracciones.iteraccionesNave(screen,protagonista,balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa,distribuidor)
                        astronauta.draw(screen)
                        derecha,izquierda,arriba,abajo = gestionarEventos(protagonista,derecha,izquierda,arriba,abajo,trajeAP)
                        balas,recargar = disparar(screen,protagonista,pintarBala,bala,balas,recargar)
                        Colisiones.colisionNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                        mostrarCarta,cristal,distribuidor = iteracciones.construirDistribuidor(screen,protagonista,mostrarCarta,cristal,cristalEnergia,distribuidor,distribuidorEnergia,escenaNave3)
                        misionesTexto.misionJupiter(screen,naveMov,mapa,cuartaMision,volverNave,espacio3,cristal,distribuidor,escenaNave3)
                        escenaNave1,escenaNave2,escenaNave3 = cambioEscena.cambioEcenaNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                    else:
                        mapaEspacio.draw(screen)
                        flechaMapa.draw(screen)
                        mapa=gestionarEventosMapa(pintarFlecha,mapa)
                        Colisiones.colisionesMapa(pintarFlecha)
                        Texto.mensajesMapa(screen,pintarFlecha,primeraMision,segundaMision,terceraMision,cuartaMision,quintaMision)
                        iteracciones.iteraccionesMapa(screen,pintarFlecha,infoSol,infoMercurio,infoVenus,infoTierra,infoMarte,infoJupiter,infoSaturno,infoUrano,infoNeptuno,infoPluton)
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        cuartaMision,jupiter,urano = misiones.misionJupiter(cuartaMision,pintarFlecha,volverNave,cristal,distribuidor,mapa,jupiter,urano)
                        misionesTexto.misionJupiter(screen,naveMov,mapa,cuartaMision,volverNave,espacio3,cristal,distribuidor,escenaNave3)
                        Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                        contadorNivel = 0
                        salirNivelUrano = False
        elif(faseInicial==False and luna == False and marte==False and jupiter==False and urano==True and pluton==False):
            if(salirNivelUrano==False):
                nivelUrano.draw(screen)
                mapa = False
                volverNave = False
                escenaNave2 = False
                escenaNave1 = True
                urano1 = True
                urano2 = False
                urano3 = False
                urano4 = False
                protagonistaEnPlaneta.rect.x = 150
                protagonistaEnPlaneta.rect.y = 280
                pintarPieza.rect.x = 600
                pintarPieza.rect.y = 225
                pintarBidon.rect.x = 372
                pintarBidon.rect.y = 170
                pintarNave.rect.x = 30
                pintarNave.rect.y = 30
                hidrogeno = 0
                trajeAP = False
                cogerHidrogeno = False
                cogerBidon = False
                cogerPieza = False
                resetear = False
                salirNivelUrano,contadorNivel = cargarMensajes.nivelUrano(salirNivelUrano,contadorNivel)
                if(salirNivelUrano==True):
                    if(secretoLuna==True):
                        gasolina-=35
                    elif(secretoLuna==False):
                        gasolina-=50
                finUrano = False
                finGasolina = False
                finVida = False
                if(gasolina<0):
                    finUrano = True
                    finGasolina = True
                    urano = False
                    if(secretoLuna==True):
                        gasolina+=75
                    elif(secretoLuna==False):
                        gasolina+=90
            else:
                if(volverNave==False):
                    if(soporteVital==True):
                        vida-=0.02
                    elif(soporteVital==False):
                        vida-=0.045 
                    if(urano1==True):
                        escenaUrano1.draw(screen)
                        nave.draw(screen)
                    if(urano2==True):
                        escenaUrano2.draw(screen)
                        if(cogerPieza==False):
                            pieza.draw(screen)
                        cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera = iteracciones.mostrarHidrogeno(screen,protagonistaEnPlaneta,bolaHidrogeno,pintarHidrogeno,cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera)
                    if(urano3==True):
                        escenaUrano3.draw(screen)
                        if(cogerBidon==False):
                            bidon.draw(screen)
                        cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera = iteracciones.mostrarHidrogeno(screen,protagonistaEnPlaneta,bolaHidrogeno,pintarHidrogeno,cogerHidrogeno,hidrogeno,contadorHidrogeno,contadorEspera)

                    if(urano4==True):
                        escenaUrano4.draw(screen)
                    astronautaEnPlaneta.draw(screen)
                    derecha,izquierda,arriba,abajo = gestionarEventos(protagonistaEnPlaneta,derecha,izquierda,arriba,abajo,trajeAP)
                    balas,recargar = disparar(screen,protagonistaEnPlaneta,pintarBala,bala,balas,recargar)
                    urano1,urano2,urano3,urano4 = cambioEscena.cambioEscenaUrano(protagonistaEnPlaneta,urano1,urano2,urano3,urano4)
                    Colisiones.colisionesUrano(protagonistaEnPlaneta,pintarNave,urano1,urano2,urano3,urano4)
                    cogerBidon,cogerPieza,piezas,bidones,vida,volverNave,escenaNave1 = iteracciones.iteraccionesUrano(screen,protagonistaEnPlaneta,urano1,urano2,urano3,urano4,cogerBidon,cogerPieza,piezas,bidones,vida,volverNave,escenaNave1)
                    misionesTexto.misionUrano(screen,quintaMision,mapa,hidrogeno,trajeAP,volverNave,escenaNave3)
                    estadisticas.draw(screen)
                    estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                    Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                    Frames.actualizarFrame(protagonistaEnPlaneta,derecha,izquierda,abajo,arriba)
                    if(volverNave==True):
                        protagonista.rect.y = 150
                    if(vida<0.5):
                        finVida=True
                        finUrano=True
                        urano=False
                        if(secretoLuna==True):
                            gasolina+=35
                        elif(secretoLuna==False):
                            gasolina+=50
                        if(cogerPieza==True):
                            piezas-=1
                            cogerPieza=False
                        if(cogerBidon==True):
                            bidones-=1
                            cogerBidon=False
                if(volverNave==True):
                    if(mapa==False):
                        if(escenaNave1):
                            escenaNaveCentral.draw(screen)
                        if(escenaNave2):
                            escenaNaveIzquierda.draw(screen)
                        if(escenaNave3):
                            escenaNaveAbajo.draw(screen)
                        balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa = iteracciones.iteraccionesNave(screen,protagonista,balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa,distribuidor)
                        astronauta.draw(screen)
                        derecha,izquierda,arriba,abajo = gestionarEventos(protagonista,derecha,izquierda,arriba,abajo,trajeAP)
                        balas,recargar = disparar(screen,protagonista,pintarBala,bala,balas,recargar)
                        Colisiones.colisionNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                        cogerBidon,cogerPieza,piezas,bidones,vida,volverNave,escenaNave1 = iteracciones.iteraccionesUrano(screen,protagonista,urano1,urano2,urano3,urano4,cogerBidon,cogerPieza,piezas,bidones,vida,volverNave,escenaNave1)
                        mostrarCarta,trajeAP,hidrogeno = iteracciones.construirTraje(screen,protagonista,trajeAP,trajeAntiPresion,hidrogeno,mostrarCarta,escenaNave3)
                        misionesTexto.misionUrano(screen,quintaMision,mapa,hidrogeno,trajeAP,volverNave,escenaNave3)
                        quintaMision,urano,pluton=misiones.misionUrano(quintaMision,pintarFlecha,volverNave,trajeAP,mapa,urano,pluton)
                        escenaNave1,escenaNave2,escenaNave3 = cambioEscena.cambioEcenaNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                        if(volverNave==False):
                            protagonistaEnPlaneta.rect.y = 580
                    else:
                        mapaEspacio.draw(screen)
                        flechaMapa.draw(screen)
                        mapa=gestionarEventosMapa(pintarFlecha,mapa)
                        Colisiones.colisionesMapa(pintarFlecha)
                        Texto.mensajesMapa(screen,pintarFlecha,primeraMision,segundaMision,terceraMision,cuartaMision,quintaMision)
                        iteracciones.iteraccionesMapa(screen,pintarFlecha,infoSol,infoMercurio,infoVenus,infoTierra,infoMarte,infoJupiter,infoSaturno,infoUrano,infoNeptuno,infoPluton)
                        quintaMision,urano,pluton=misiones.misionUrano(quintaMision,pintarFlecha,volverNave,trajeAP,mapa,urano,pluton)
                        misionesTexto.misionUrano(screen,quintaMision,mapa,hidrogeno,trajeAP,volverNave,escenaNave3)
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                        contadorNivel = 0
                        salirNivelPluton = False
        elif(faseInicial==False and luna == False and marte==False and jupiter==False and urano==False and pluton==True):
            if(salirNivelPluton==False):
                nivelPluton.draw(screen)
                mapa=False
                volverNave=False
                escenaNave2=False
                escenaNave1=True
                pluton1=True
                pluton2=False
                pintarNave.rect.x = 250
                pintarNave.rect.y = 400
                protagonistaEnPlaneta.rect.x = 392
                protagonistaEnPlaneta.rect.y = 690
                antagonista.rect.x=200
                vodaJefe=100
                resetear = False
                salirNivelPluton,contadorNivel = cargarMensajes.nivelPluton(salirNivelPluton,contadorNivel)
                if(salirNivelPluton==True):
                    if(secretoLuna==True):
                        gasolina-=20
                    elif(secretoLuna==False):
                        gasolina-=30
                finPluton = False
                finGasolina = False
                finVida = False
                if(gasolina<0):
                    finPluton  = True
                    finGasolina = True
                    pluton = False
                    if(secretoLuna==True):
                        gasolina+=70
                    elif(secretoLuna==False):
                        gasolina+=80
            else:
                if(volverNave==False):
                    if(pluton1):
                        escenaPluton1.draw(screen)
                        nave.draw(screen)
                    if(pluton2):
                        escenaPluton2.draw(screen)
                        if(vidaJefe>0):
                            jefe.draw(screen)
                            Frames.actualizarFrameJefe(antagonista,derechaJefe,izquierdaJefe,0,0)
                            contadorDisparo,disparoMaligno,vidaJefe,disparo,vida,ataqueEspecial,contadorAtaqueEspecial,contadorMira,contadorExplosion,derechaJefe,izquierdaJefe,balas = iteracciones.combate(screen,protagonistaEnPlaneta,antagonista,vidaJefe,pintarBala,disparo,contadorDisparo,disparoMaligno,balaOscura,pintarBalaOscura,vida,crearMira,crearExplosion,pintarMira,pintarExplosion,ataqueEspecial,contadorAtaqueEspecial,contadorMira,contadorExplosion,derechaJefe,izquierdaJefe,soporteVital,balas,pintarMedicamento,crearMedicamento)
                            iteracciones.movimientoJefe(antagonista,derechaJefe,izquierdaJefe,vidaJefe)
                            contadorMensaje = Texto.hemorragia(screen,vidaJefe,contadorMensaje)
                            contadorMensaje = Texto.explosion(screen,vidaJefe,contadorMensaje)
                        if(vidaJefe<=0 and contadorNivel==200):
                            if(contadorNivel!=200):
                                contadorNivel+=1
                            if(contadorNivel==200):
                                pluton=False

                    astronautaEnPlaneta.draw(screen)
                    derecha,izquierda,arriba,abajo = gestionarEventos(protagonistaEnPlaneta,derecha,izquierda,arriba,abajo,trajeAP)
                    balas,recargar = disparar(screen,protagonistaEnPlaneta,pintarBala,bala,balas,recargar)
                    volverNave = iteracciones.entrarNavePluton(screen,protagonistaEnPlaneta,pluton1,volverNave,escenaNave1)
                    pluton1,pluton2 = cambioEscena.cambioEscenaPluton(protagonistaEnPlaneta,pluton1,pluton2)
                    Colisiones.colisionesPluton(protagonistaEnPlaneta,pintarNave,pluton1,pluton2)
                    if(vida<0.5):
                        finPluton = True
                        finVida = True
                        pluton = False
                        contadorMensaje = 0
                        if(secretoLuna==True):
                            gasolina+=20
                        else:
                            gasolina+=30
                    else:
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        Frames.actualizarFrame(protagonistaEnPlaneta,derecha,izquierda,abajo,arriba)
                else:
                    if(mapa==False):
                        if(escenaNave1):
                            escenaNaveCentral.draw(screen)
                        if(escenaNave2):
                            escenaNaveIzquierda.draw(screen)
                        if(escenaNave3):
                            escenaNaveAbajo.draw(screen)
                        balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa = iteracciones.iteraccionesNave(screen,protagonista,balas,gasolina,bidones,arreglo,piezas,vida,escenaNave1,escenaNave2,escenaNave3,contadorIteraccion,mapa,distribuidor)
                        astronauta.draw(screen)
                        derecha,izquierda,arriba,abajo = gestionarEventos(protagonista,derecha,izquierda,arriba,abajo,trajeAP)
                        balas,recargar = disparar(screen,protagonista,pintarBala,bala,balas,recargar)
                        Colisiones.colisionNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                        escenaNave1,escenaNave2,escenaNave3 = cambioEscena.cambioEcenaNave(protagonista,escenaNave1,escenaNave2,escenaNave3)
                        volverNave = iteracciones.entrarNavePluton(screen,protagonista,pluton1,volverNave,escenaNave1)
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
                        if(volverNave==False):
                            protagonistaEnPlaneta.rect.y = 580
                    else:
                        mapaEspacio.draw(screen)
                        flechaMapa.draw(screen)
                        mapa=gestionarEventosMapa(pintarFlecha,mapa)
                        Colisiones.colisionesMapa(pintarFlecha)
                        Texto.mensajesMapa(screen,pintarFlecha,primeraMision,segundaMision,terceraMision,cuartaMision,quintaMision)
                        iteracciones.iteraccionesMapa(screen,pintarFlecha,infoSol,infoMercurio,infoVenus,infoTierra,infoMarte,infoJupiter,infoSaturno,infoUrano,infoNeptuno,infoPluton)
                        estadisticas.draw(screen)
                        estadisticas = cargarImagen.colocarStats(estadisticas,gasolina,arreglo,vida,balas,bidones,piezas)
                        Texto.mensajesHUD(screen,gasolina,arreglo,vida,balas,bidones,piezas)
                        Frames.actualizarFrame(protagonista,derecha,izquierda,abajo,arriba)
        elif(pluton==False and vidaJefe<=0):
            ganacion.draw(screen)
            funcionando,contadorNivel = cargarMensajes.mensajeGanar(funcionando,contadorNivel)

        pygame.display.flip()
        await asyncio.sleep(0)
asyncio.run(main())
            