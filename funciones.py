
import pygame

fuente = pygame.font.SysFont("Arial", 30)
# Función para crear un botón
def crear_boton(x, y, ancho, alto, color, texto):
    pygame.draw.rect(ventana, color, (x, y, ancho, alto))
    fuente = pygame.font.Font(None, 36)
    texto_renderizado = fuente.render(texto, True, COLOR_BLANCO)
    texto_rect = texto_renderizado.get_rect()
    texto_rect.center = (x + ancho // 2, y + alto // 2)
    ventana.blit(texto_renderizado, texto_rect)
# Función para mostrar una pregunta y sus opciones
def mostrar_pregunta(contador_preguntas):
    pregunta = fuente.render(lista_preguntas[contador_preguntas], True, COLOR_BLANCO)
    respuesta_a = fuente.render(lista_respuestas_a[contador_preguntas], True, COLOR_BLANCO)
    respuesta_b = fuente.render(lista_respuestas_b[contador_preguntas], True, COLOR_BLANCO)
    respuesta_c = fuente.render(lista_respuestas_c[contador_preguntas], True, COLOR_BLANCO)
    return pregunta, respuesta_a, respuesta_b, respuesta_c

# Función para verificar la respuesta del jugador
def verificar_respuesta(respuesta):
    global puntaje, correcto, chances
    if lista_correctas[contador_preguntas] == respuesta:
        puntaje += 10
        texto_puntaje = fuente.render(str(puntaje), True, COLOR_BLANCO)
        correcto = True
    else:
        chances += 1
