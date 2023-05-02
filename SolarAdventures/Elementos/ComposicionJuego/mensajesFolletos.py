import pygame
class cargarMensajes:
    def comienzo(salir):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN]):
            salir = True
        return salir
    
    def controles(salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelLuna(salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelMarte(salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelJupiter(salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelUrano(salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def nivelPluton(salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = True
        elif(contadorNivel!=200):
            contadorNivel+=1
        return salir,contadorNivel
    
    def mensajeGanar(salir,contadorNivel):
        teclaPulsada = pygame.key.get_pressed()
        if(teclaPulsada[pygame.K_RETURN] and contadorNivel==200):
            salir = False
        return salir,contadorNivel
    
    