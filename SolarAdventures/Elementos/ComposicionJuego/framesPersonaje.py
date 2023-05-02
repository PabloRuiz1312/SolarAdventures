import pygame
class Frames:
    def obtenerFrame(spriteSheet,x,y,ancho,largo):
        negro = pygame.Color(0,0,0)
        frame = pygame.Surface([ancho,largo]).convert()

        frame.blit(spriteSheet,(0,0),(x,y,ancho,largo))

        frame.set_colorkey(negro)

        return frame
    #Funcion para cargar los frames de la derecha del protagonista
    def cargarFramesDerecha(protagonista):
        protagonista.framesDerecha = []
        frame = Frames.obtenerFrame(protagonista.spriteSheet,0,170,85,85)
        protagonista.framesDerecha.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,85,170,85,85)
        protagonista.framesDerecha.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,170,170,85,85)
        protagonista.framesDerecha.append(frame)
    #Funcion para cargar los frames de la izquierda del protagonista
    def cargarFramesIzquierda(protagonista):
        protagonista.framesIzquierda = []

        frame = Frames.obtenerFrame(protagonista.spriteSheet,0,85,85,85)
        
        protagonista.framesIzquierda.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,85,85,85,85)
        
        protagonista.framesIzquierda.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,170,85,85,85)
        
        protagonista.framesIzquierda.append(frame)
    #Funcion para cargar los frames de abajo del protagonista
    def cargarFramesAbajo(protagonista):
        protagonista.framesAbajo = []
        frame = Frames.obtenerFrame(protagonista.spriteSheet,0,0,85,85)
        
        protagonista.framesAbajo.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,85,0,85,85)
        
        protagonista.framesAbajo.append(frame)
        
        frame = Frames.obtenerFrame(protagonista.spriteSheet,170,0,85,85)
        
        protagonista.framesAbajo.append(frame)
        protagonista.image = protagonista.framesAbajo[0]

        protagonista.rect = protagonista.image.get_rect()
    #Funcion para cargar los frames de arriba derecha del protagonista
    def cargarFramesArriba(protagonista):
        protagonista.framesArriba = []
        frame = Frames.obtenerFrame(protagonista.spriteSheet,0,255,85,85)
        
        protagonista.framesArriba.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,85,255,85,85)
        
        protagonista.framesArriba.append(frame)

        frame = Frames.obtenerFrame(protagonista.spriteSheet,170,255,85,85)
        
        protagonista.framesArriba.append(frame)
    #Funcion para actualizar los frames escogidos del protagonista
    def actualizarFrame (protagonista,derecha,izquierda,abajo,arriba):
        if derecha == 1:
            frame = (protagonista.rect.x // 50) % len(protagonista.framesDerecha)
            protagonista.image = protagonista.framesDerecha [frame]       
        elif izquierda == 1 :
            frame = (protagonista.rect.x  // 50) % len(protagonista.framesIzquierda)
            protagonista.image = protagonista.framesIzquierda [frame]      
        elif (arriba ==  1):
            frame = (protagonista.rect.y // 50) % len(protagonista.framesArriba)
            protagonista.image = protagonista.framesArriba [frame]
        elif (abajo == 1):
            frame = (protagonista.rect.y  // 50) % len(protagonista.framesAbajo)
            protagonista.image = protagonista.framesAbajo [frame]

    def actualizarFrameJefe(protagonista,derecha,izquierda,abajo,arriba):
        if derecha == 1:
            frame = (protagonista.rect.x // 50) % len(protagonista.framesDerecha)
            protagonista.image = protagonista.framesDerecha [frame]       
        elif izquierda == 1 :
            frame = (protagonista.rect.x  // 50) % len(protagonista.framesIzquierda)
            protagonista.image = protagonista.framesIzquierda [frame]     
        elif derecha==0 and izquierda==0:
            frame = (protagonista.rect.x  // 50) % len(protagonista.framesAbajo)
            protagonista.image = protagonista.framesAbajo [frame]
    #Funcion para cargar los frames de la derecha del astronauta en el planeta
    def cargarFramesDerechaAChico(astronauta):
        astronauta.framesDerecha = []
        frame = Frames.obtenerFrame(astronauta.spriteSheet,0,113,56.6,56.5)
        astronauta.framesDerecha.append(frame)

        frame = Frames.obtenerFrame(astronauta.spriteSheet,56.6,113,56.6,56.5)
        astronauta.framesDerecha.append(frame)

        frame = Frames.obtenerFrame(astronauta.spriteSheet,113.2,113,56.6,56.5)
        astronauta.framesDerecha.append(frame)
    #Funcion para cargar los frames de la izquierda del astronauta en el planeta
    def cargarFramesIzquierdaAChico (astronauta):
        astronauta.framesIzquierda = []

        frame = Frames.obtenerFrame(astronauta.spriteSheet,0,56.5,56.6,56.5)
        
        astronauta.framesIzquierda.append(frame)

        frame = Frames.obtenerFrame(astronauta.spriteSheet,56.6,56.5,56.6,56.5)
        
        astronauta.framesIzquierda.append(frame)

        frame = Frames.obtenerFrame(astronauta.spriteSheet,113.2,56.5,56.6,56.5)
        
        astronauta.framesIzquierda.append(frame)
    #Funcion para cargar los frames de abajo del astronauta en el planeta
    def cargarFramesAbajoAChico(astronauta):
        astronauta.framesAbajo = []
        frame = Frames.obtenerFrame(astronauta.spriteSheet,0,0,56.6,56.5)
        
        astronauta.framesAbajo.append(frame)

        frame = Frames.obtenerFrame(astronauta.spriteSheet,56.6,0,56.6,56.5)
        
        astronauta.framesAbajo.append(frame)

        frame = Frames.obtenerFrame(astronauta.spriteSheet,113.2,0,56.6,56.5)
        
        astronauta.framesAbajo.append(frame)
        astronauta.image = astronauta.framesAbajo[0]

        astronauta.rect = astronauta.image.get_rect()
    #Funcion para cargar los frames de arriba del astronauta en el planeta
    def cargarFramesArribaAChico(astronauta):
        astronauta.framesArriba = []
        frame = Frames.obtenerFrame(astronauta.spriteSheet,0,169.5,56.6,56.5)
        
        astronauta.framesArriba.append(frame)

        frame = Frames.obtenerFrame(astronauta.spriteSheet,56.6,169.5,56.6,56.5)
        
        astronauta.framesArriba.append(frame)

        frame = Frames.obtenerFrame(astronauta.spriteSheet,113.2,169.5,56.6,56.5)
        
        astronauta.framesArriba.append(frame)
    #Funcion para cargar los frames de la derecha de la nave
    def cargarFramesNaveDerecha(naveMov):
        naveMov.framesDerecha = []
        frame = Frames.obtenerFrame(naveMov.spriteSheet,0,103,64,61)
        naveMov.framesDerecha.append(frame)
    #Funcion para cargar los frames de la izquierda de la nave
    def cargarFramesNaveIzquierda(naveMov):
        naveMov.framesIzquierda = []
        frame = Frames.obtenerFrame(naveMov.spriteSheet,0,175,64,58.5)
        naveMov.framesIzquierda.append(frame)
        naveMov.image = naveMov.framesIzquierda[0]

        naveMov.rect = naveMov.image.get_rect()
    #Funcion para cargar los frames de arriba de la nave
    def cargarFramesNaveArriba(naveMov):
        naveMov.framesArriba = []
        frame = Frames.obtenerFrame(naveMov.spriteSheet,0,0,64,52)
        naveMov.framesArriba.append(frame)
    #Funcion pata cargar los frames de abajo de la nave
    def cargarFramesNaveAbajo(naveMov):
        naveMov.framesAbajo = []
        frame = Frames.obtenerFrame(naveMov.spriteSheet,0,52,64,52)
        naveMov.framesAbajo.append(frame)
    def cargarFramesJefeDerecha(jefe):
        jefe.framesDerecha = []
        frame = Frames.obtenerFrame(jefe.spriteSheet,0,284.66,133.3,142.33)
        jefe.framesDerecha.append(frame)

        frame = Frames.obtenerFrame(jefe.spriteSheet,133.3,284.66,133.3,142.33)
        jefe.framesDerecha.append(frame)

        frame = Frames.obtenerFrame(jefe.spriteSheet,266.6,284.66,133.3,142.33)
        jefe.framesDerecha.append(frame)

    def cargarFramesJefeIzquierda(jefe):
        jefe.framesIzquierda = []
        frame = Frames.obtenerFrame(jefe.spriteSheet,0,142.33,133.3,142.33)
        jefe.framesIzquierda.append(frame)

        frame = Frames.obtenerFrame(jefe.spriteSheet,133.3,142.33,133.3,142.33)
        jefe.framesIzquierda.append(frame)

        frame = Frames.obtenerFrame(jefe.spriteSheet,266.6,142.33,133.3,142.33)
        jefe.framesIzquierda.append(frame)
        
    def cargarFramesJefeAbajo(jefe):
        jefe.framesAbajo = []
        frame = Frames.obtenerFrame(jefe.spriteSheet,0,0,133.3,142.33)
        jefe.framesAbajo.append(frame)

        frame = Frames.obtenerFrame(jefe.spriteSheet,133.3,0,133.3,142.33)
        jefe.framesAbajo.append(frame)

        frame = Frames.obtenerFrame(jefe.spriteSheet,266.6,0,133.3,142.33)
        jefe.framesAbajo.append(frame)

        jefe.image = jefe.framesAbajo[0]

        jefe.rect = jefe.image.get_rect()
    
