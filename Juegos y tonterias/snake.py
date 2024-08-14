import turtle
import time
import random

posponer=0.1

#Configuracion de la ventana

wn=turtle.Screen()
wn.title("Juego de Snake")
wn.bgcolor("blue")
wn.setup(width=600,height=600)
wn.tracer()

#Cabeza de la serpiente

cabeza=turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.color("black")
cabeza.penup()  #no dejar rastro
cabeza.goto(10,0)
cabeza.direction="stop"

#Cuerpo Serpiente

segmentos=[]

#Comida

comida=turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()  #no dejar rastro
comida.goto(0,100)




# Definicion de Funciones

def arriba():
    cabeza.direction="up"

def abajo():
    cabeza.direction="down"

def derecha():
    cabeza.direction="right"

def izquierda():
    cabeza.direction="left"


def mov():
    if cabeza.direction=="up":
        y=cabeza.ycor()
        cabeza.sety(y+20)
    if cabeza.direction=="down":
        y=cabeza.ycor()
        cabeza.sety(y-20)
    if cabeza.direction=="left":
        x=cabeza.xcor()
        cabeza.setx(x-20)
    if cabeza.direction=="right":
        x=cabeza.xcor()
        cabeza.setx(x+20)


#Teclado
wn.listen()
wn.onkeypress(arriba,"Up") # "Up" con mayuscula indica la tecla del teclado
wn.onkeypress(abajo,"Down")
wn.onkeypress(izquierda,"Left")
wn.onkeypress(derecha,"Right")




while True:
    wn.update()
    #Colisiones bordes
    if cabeza.xcor() > 280 or cabeza.xcor()<-280 or cabeza.ycor()>280 or cabeza.ycor()<-280:
        time.sleep(1)
        cabeza.goto(0,0)
        cabeza.direction="stop"
        #esconder segmentos
        for segmento in segmentos:
            segmento.goto(1000,1000)
        #limpiar lista
        segmentos.clear()

    if cabeza.distance(comida)<20:
        x=random.randint(-280,280) # el objeto tiene 20 px de ancho
        y=random.randint(-280,280)
        comida.goto(x,y)
        nuevo_segmento=turtle.Turtle()
        nuevo_segmento.speed(0)
        nuevo_segmento.shape("square")
        nuevo_segmento.color("grey")
        nuevo_segmento.penup()  #no dejar rastro
        segmentos.append(nuevo_segmento)
        
    #mover el cuerpo de la serpiente
    totalSeg=len(segmentos)
    for index in range(totalSeg -1,0,-1):
        x=segmentos[index-1].xcor()
        y=segmentos[index-1].ycor()
        segmentos[index].goto(x,y)
    if totalSeg>0:
        x=cabeza.xcor()
        y=cabeza.ycor()
        segmentos[0].goto(x,y)


    mov()
    time.sleep(posponer)


#turtle.done()


