import pygame
from datos import *
from constantes import *

texto = "" #DEFINO CADENA VACIA PARA IR PUDIENDO METER LOS TITULOS
lista_preguntas = []
lista_respuestas_a = []
lista_respuestas_b = []
lista_respuestas_c = []
lista_correctas = []
puntaje = 0
preguntar = False
contador_preguntas = -1
correcto = False
chances = 0
alpha = 128

for elemento in lista:
    lista_preguntas.append(elemento['pregunta']) #AGREGO CADA ELEMENTO A LA LISTA DEFINIDA
    lista_respuestas_a.append(elemento['a'])
    lista_respuestas_b.append(elemento['b'])
    lista_respuestas_c.append(elemento['c'])
    lista_correctas.append(elemento['correcta'])

pygame.init()

#DEFINO MUSICA
pygame.mixer.init()
pygame.mixer.music.set_volume(0.7)
sonido_fondo = pygame.mixer.Sound("musica_fondo.mp3")
sonido_fondo.set_volume(0.2)
sonido_correcta = pygame.mixer.Sound("correcto.mp3")
sonido_correcta.set_volume(0.4)
sonido_error = pygame.mixer.Sound("error.mp3")
sonido_error.set_volume(0.4)
sonido_fondo.play()

#DEFINO PANTALLA
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Preguntados")

#DEFINO TRANSPARENCIA
superficie = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA), pygame.SRCALPHA)
superficie.fill((0, 0, 0, alpha))

#DEFINO FONDO
fondo = pygame.image.load("fondo.jpg")
fondo = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA)) # me cambia el tamanio fondo

#DEFINO LOGO
logo = pygame.image.load("logo.png")
logo = pygame.transform.scale(logo, (175, 175))

#DEFINIR TEXTOS
font = pygame.font.SysFont("Arial", 25)
texto_rend = font.render(str(texto), True, COLOR_NEGRO) #CONVIENE CASTEAR A STR POR LAS DUDAS, y guardo en variable TITULO -CADENA VACIA DEFINIDA ANTES-
texto_pregunta = font.render("Pregunta", True, COLOR_BLANCO)
texto_reiniciar = font.render("Reiniciar", True, COLOR_BLANCO)
score = font.render("Score", True, COLOR_NEGRO)
texto_puntaje = font.render(str(puntaje), True, COLOR_NEGRO)

running = True

while running:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            running = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos) # ME GUARDO EN UNA VARIABLE CASTEADA A LISTA EL EVENTO.POS QUE ME DICE DONDE APRETE
            #print(posicion_click) #PRINTEO COMO CHEQUEO DE LA POSICION
            #BOTON PREGUNTA
            if (posicion_click[0] > 160 and posicion_click[0] <360) and (posicion_click[1] > 480 and posicion_click[1] <555):  #CREO CONDICION PARA QUE SI ENTRA A LA POSICION CAMBIE PREG, primero alto de boton dps ancho son las que separadas con parentesis se separa
                correcto = False
                chances = 2
                if contador_preguntas < (len(lista_preguntas) -1): #AGREGO VERIFICACION 
                    contador_preguntas += 1
                else:
                    contador_preguntas = 0  #Para que cambie de pregunta es el contador
                preguntar = True
                pregunta = lista_preguntas[contador_preguntas] #PARA GUARDARME LA PRIMERA PREGUNTA EN LA VARIABLE
                texto_rend = font.render(str(pregunta), True, COLOR_NEGRO) #RENDERIZO ASI ME MUESTRA LA PREG
                respuesta_a = font.render(lista_respuestas_a[contador_preguntas], True, COLOR_NEGRO)
                respuesta_b = font.render(lista_respuestas_b[contador_preguntas], True, COLOR_NEGRO)
                respuesta_c = font.render(lista_respuestas_c[contador_preguntas], True, COLOR_NEGRO)
            #VERIFICO SI APRETO ALGUNA OPCION   
            if ((posicion_click[0] > 145 and posicion_click[0] < 245) and (posicion_click[1] > 250 and posicion_click[1] < 300)):
                if (lista_correctas[contador_preguntas] == 'a'):
                    puntaje += 10
                    texto_puntaje = font.render(str(puntaje), True, COLOR_NEGRO)
                    correcto = True
                    sonido_correcta.play()
                else:
                    chances -= 1
                    # Borra las opciones incorrectas al responder incorrectamente
                    respuesta_a = font.render("", True, COLOR_NEGRO)
                    sonido_error.play()

            if ((posicion_click[0] > 350 and posicion_click[0] < 450) and (posicion_click[1] > 250 and posicion_click[1] < 300)):
                if (lista_correctas[contador_preguntas] == 'b'):
                    puntaje += 10
                    texto_puntaje = font.render(str(puntaje), True, COLOR_NEGRO)
                    correcto = True
                    sonido_correcta.play()
                else:
                    chances -= 1
                    # Borra las opciones incorrectas al responder incorrectamente
                    respuesta_b = font.render("", True, COLOR_NEGRO)
                    sonido_error.play()
            if ((posicion_click[0] > 565 and posicion_click[0] < 665) and (posicion_click[1] > 250 and posicion_click[1] < 300)):
                if (lista_correctas[contador_preguntas] == 'c'):
                    puntaje += 10
                    texto_puntaje = font.render(str(puntaje), True, COLOR_NEGRO)
                    correcto = True
                    sonido_correcta.play()
                else:
                    chances -= 1
                    # Borra las opciones incorrectas al responder incorrectamente
                    respuesta_c = font.render("", True, COLOR_NEGRO)
                    sonido_error.play()
            #BOTON REINICIAR
            if (posicion_click[0] > 430 and posicion_click[0] < 630) and (posicion_click[1] > 480 and posicion_click[1] < 555):
                puntaje = 0
                correcto = False
                texto_puntaje = font.render(str(puntaje), True, COLOR_NEGRO)
                chances = 2
                contador_preguntas = 0
                pregunta = lista_preguntas[contador_preguntas]
                texto_rend = font.render(str(pregunta), True, COLOR_NEGRO)
                respuesta_a = font.render(lista_respuestas_a[contador_preguntas], True, COLOR_NEGRO)
                respuesta_b = font.render(lista_respuestas_b[contador_preguntas], True, COLOR_NEGRO)
                respuesta_c = font.render(lista_respuestas_c[contador_preguntas], True, COLOR_NEGRO)
                
            
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(logo, (302, 10))
    pygame.draw.rect(pantalla, COLOR_ROSA, (160, 480, 200, 75))
    pantalla.blit(texto_pregunta, (210, 500))  # Posiciona el texto "Pregunta" en el botón rosa
    pygame.draw.rect(pantalla, COLOR_GRIS, (430, 480, 200, 75))
    pantalla.blit(texto_reiniciar, (475, 500))  # Posiciona el texto "Reiniciar" en el botón gris
    
    if preguntar == True:
        superficie_semitransparente = pygame.Surface((ANCHO_VENTANA, ALTO_VENTANA), pygame.SRCALPHA)
        pygame.draw.rect(superficie_semitransparente, (255, 255, 255, alpha), (100, 200, 665, 150))
        pantalla.blit(superficie_semitransparente, (0, 0))
        pantalla.blit(texto_rend, (100, 200))
        if correcto == False and chances > 0:
            pantalla.blit(respuesta_a, (145, 250))
            pantalla.blit(respuesta_b, (350, 250))
            pantalla.blit(respuesta_c, (565, 250))
       
    pygame.draw.rect(pantalla, COLOR_GRIS, (430, 480, 200, 75))
    pantalla.blit(texto_reiniciar, (475, 500))
    pantalla.blit(score, (40,30) )
    pantalla.blit(texto_puntaje, (60,50))

    pygame.display.flip()
sonido_fondo.stop()
pygame.quit()
