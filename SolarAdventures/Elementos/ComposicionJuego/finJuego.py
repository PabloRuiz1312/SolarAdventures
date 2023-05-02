import pygame
class gameOvers:

    def empezarPorVida(nivel,planeta,contadorNivel,resetear,vida,funcionando):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            nivel=False
            planeta=True
            contadorNivel=0
            vida=100
        if(teclaPulsada[pygame.K_ESCAPE]):
            funcionando=False
        return nivel,planeta,contadorNivel,resetear,vida,funcionando
    
    def empezarPorGasolina(nivel,planeta,contadorNivel,resetear,funcionando):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            nivel=False
            planeta=True
            contadorNivel=0
        if(teclaPulsada[pygame.K_ESCAPE]):
            funcionando=False
        return nivel,planeta,contadorNivel,resetear,funcionando
    
    def empezarPorArreglos(nivel,planeta,contadorNivel,resetear,arreglos,funcionando):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            nivel=False
            planeta=True
            contadorNivel=0
            arreglos=100
        if(teclaPulsada[pygame.K_ESCAPE]):
            funcionando=False
        return nivel,planeta,contadorNivel,resetear,arreglos,funcionando

    def empezarPorJupiter(salirNivelJupiter,jupiter,contadorNivel,resetear,funcionando):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            salirNivelJupiter=False
            jupiter=True
            contadorNivel=0
        if(teclaPulsada[pygame.K_ESCAPE]):
            funcionando=False
        return salirNivelJupiter,jupiter,contadorNivel,resetear,funcionando