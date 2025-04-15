from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *

janela = Window(1280, 640)
janela.set_title("Gabriel Salerno")

bola = Sprite("bola.png", frames=1)
bola.x = (1280 - bola.width)/2
bola.y = (640 - bola.height)/2
bola.set_position(bola.x,bola.y)

barraE = Sprite("barra.png", frames=1)
barraE.x = (barraE.width-30)
barraE.y = (640 - barraE.height)/2

barraD = Sprite("barra.png", frames=1)
barraD.x = (1268 - barraE.width)
barraD.y = (640 - barraE.height)/2

teclado = Keyboard()

velx = 0.5
vely = 0.1

movendo = False

while(True):
    janela.set_background_color([0,0,255])
    bola.draw()
    barraE.draw()
    barraD.draw()
    if (teclado.key_pressed("space")) == True:
        movendo = True
    if movendo == True:
        bola.x = bola.x + velx
        bola.y = bola.y + vely
        if bola.x <= 0 or bola.x + bola.width >= janela.width:
            velx = velx * -1
        if bola.y <= 0 or bola.y + bola.height >= janela.height:
            vely = vely * -1
    janela.update()
