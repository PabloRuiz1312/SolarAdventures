import pygame
class CargarMensajes:
    def __init__(self):
        pass

    def comienzo(self,salir):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            salir = True
        return salir
    
    def controles(self,salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelLuna(self,salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelMarte(self,salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelJupiter(self,salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelUrano(self,salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelPluton(self,salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def mensajeGanar(self,salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = False
        return salir,contadorNivel
    
    