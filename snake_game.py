import turtle
import random
import time

puntacion_jugador = 0
puntuacion_maxima = 0
tiempo_retraso = 0.1

# pantalla de ventana creada
wind = turtle.Screen()
wind.title("Laberinto de serpientes🐍")
wind.bgcolor("blue")

# El tamaño de la pantalla
wind.setup(width=600, height=600)

# Creación de la serpiente
serpiente = turtle.Turtle()
serpiente.shape("square")
serpiente.color("black")
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direccion = "Stop"

# crear la comida
snake_food = turtle.Turtle()
formas = random.choice(['triangle', 'circle'])
snake_food.shape(formas)
snake_food.color("green")
snake_food.speed(0)
snake_food.penup()
snake_food.goto(0, 100)

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Su puntuación: 0  Puntuación más alta: 0", align="center", font=("Arial", 24, "normal"))

# Asignación de direcciones
def mover_izquierda():
    if serpiente.direccion != "derecha":
        serpiente.direccion = "izquierda"

def mover_derecha():
    if serpiente.direccion != "izquierda":
        serpiente.direccion = "derecha"

def mover_arriba():
    if serpiente.direccion != "abajo":
        serpiente.direccion = "arriba"

def mover_abajo():
    if serpiente.direccion != "arriba":
        serpiente.direccion = "abajo"

def mover():
    if serpiente.direccion == "arriba":
        serpiente.sety(serpiente.ycor() + 20)

    if serpiente.direccion == "abajo":
        serpiente.sety(serpiente.ycor() - 20)

    if serpiente.direccion == "derecha":
        serpiente.setx(serpiente.xcor() + 20)

    if serpiente.direccion == "izquierda":
        serpiente.setx(serpiente.xcor() - 20)

# Configuración de las teclas
wind.listen()
wind.onkeypress(mover_izquierda, 'Left')
wind.onkeypress(mover_derecha, 'Right')
wind.onkeypress(mover_arriba, 'Up')
wind.onkeypress(mover_abajo, 'Down')

segmentos = []

# Implementar la jugabilidad
while True:
    wind.update()
    
    # Comprobación de colisiones con los bordes
    if serpiente.xcor() > 290 or serpiente.xcor() < -290 or serpiente.ycor() > 290 or serpiente.ycor() < -290:
        time.sleep(1)
        serpiente.goto(0, 0)
        serpiente.direccion = "Stop"
        serpiente.shape("square")
        serpiente.color("green")

        for segmento in segmentos:
            segmento.goto(1000, 1000)  # Quitar los segmentos de la pantalla
        segmentos.clear()

        puntacion_jugador = 0
        tiempo_retraso = 0.1
        pen.clear()
        pen.write("Su puntuación: {}  Puntuación más alta: {}".format(puntacion_jugador, puntuacion_maxima), align="center", font=("Arial", 24, "normal"))

    # Comprobación de colisión con la comida
    if serpiente.distance(snake_food) < 20:
        coord_x = random.randint(-270, 270)
        coord_y = random.randint(-270, 270)
        snake_food.goto(coord_x, coord_y)

        # Añadir segmento
        segmento_añadido = turtle.Turtle()
        segmento_añadido.speed(0)
        segmento_añadido.shape("square")
        segmento_añadido.color("white")
        segmento_añadido.penup()
        segmentos.append(segmento_añadido)

        tiempo_retraso -= 0.001
        puntacion_jugador += 10

        if puntacion_jugador > puntuacion_maxima:
            puntuacion_maxima = puntacion_jugador
        pen.clear()
        pen.write("Su puntuación: {}  Puntuación más alta: {}".format(puntacion_jugador, puntuacion_maxima), align="center", font=("Arial", 24, "normal"))

    # Mover los segmentos del cuerpo de la serpiente
    for i in range(len(segmentos) - 1, 0, -1):
        coord_x = segmentos[i - 1].xcor()
        coord_y = segmentos[i - 1].ycor()
        segmentos[i].goto(coord_x, coord_y)

    if len(segmentos) > 0:
        segmentos[0].goto(serpiente.xcor(), serpiente.ycor())

    mover()

    # Comprobación de colisión con el cuerpo de la serpiente
    for segmento in segmentos:
        if segmento.distance(serpiente) < 20:
            time.sleep(1)
            serpiente.goto(0, 0)
            serpiente.direccion = "Stop"
            serpiente.color('white')

            for segmento in segmentos:
                segmento.goto(1000, 1000)
            segmentos.clear()
            puntacion_jugador = 0
            tiempo_retraso = 0.1
            pen.clear()
            pen.write("Su puntuación: {}  Puntuación más alta: {}".format(puntacion_jugador, puntuacion_maxima), align="center", font=("Arial", 24, "normal"))

    time.sleep(tiempo_retraso)

turtle.mainloop()