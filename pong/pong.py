from PPlay.window import *
from PPlay.sprite import *
from PPlay.keyboard import *
from random import randint

janela = Window(1280, 640)
janela.set_title("Gabriel Salerno")

bola = Sprite("bola.png", frames=1)
bola.x = (1280 - bola.width)/2
bola.y = (640 - bola.height)/2
bola.set_position(bola.x,bola.y)

barraE = Sprite("barra.png", frames=1)
barraE.x = (barraE.width - 20)
barraE.y = (640 - barraE.height)/2

barraD = Sprite("barra.png", frames=1)
barraD.x = (1270 - barraD.width)
barraD.y = (640 - barraD.height)/2

obstaculo = Sprite("obstaculo.png", frames=1)
obstaculo.x = (1280 - obstaculo.width)/2

teclado = Keyboard()

velBolax = 650
velBolay = 450

velBarraEy = 270

velBarraDy = 212

movendo = False

pontuacaoE = 0
pontuacaoD = 0

contador = 0

obstaculo_visivel = False
cronometro_ativo = False

while(True):
    janela.set_background_color([0,0,255])

    # Apertar barra de espaço para iniciar
    if (teclado.key_pressed("space")) == True:
        movendo = True
    
    if movendo == True:
        # Barra da esquerda mexendo com as setinhas
        if teclado.key_pressed("up"):
            barraE.y = barraE.y + velBarraEy * janela.delta_time() * -1
        if teclado.key_pressed("down"):
            barraE.y = barraE.y + velBarraEy * janela.delta_time()

        # Limita a barra da esquerda dentro da janela
        if barraE.y < 0:
            barraE.y = 0
        if barraE.y + barraE.height > janela.height:
            barraE.y = janela.height - barraE.height

        # Barra da direita limitada dentro da janela
        if barraD.y < 0:
            barraD.y = 0
        if barraD.y + barraD.height > janela.height:
            barraD.y = janela.height - barraD.height

        # IA - bola vai para baixo barra da direita vai para baixo
        # bola vai para cima barra da direita vai para cima
        if velBolay < 0 :
            barraD.y = barraD.y + velBarraDy * janela.delta_time() *-1
        if velBolay > 0:
            barraD.y = barraD.y + velBarraDy * janela.delta_time()

        # Dá movimento a bola
        bola.x = bola.x + velBolax * janela.delta_time()
        bola.y = bola.y + velBolay * janela.delta_time()

        # Bola colidindo com a parede de cima e debaixo, resolvendo também o bug do delta_time reposicionando a bola
        if bola.y <= 0:
            bola.y = 0
            velBolay = velBolay * -1
        if bola.y + bola.height >= janela.height:
            bola.y = janela.height - bola.height
            velBolay = velBolay * -1

        # Bola colidindo com as barras, resolvendo também o bug do delta_time reposicionando a bola
        if bola.collided(barraE):
            bola.x = barraE.x + barraE.width
            velBolax = velBolax * -1 
            contador += 1
        if bola.collided(barraD):
            bola.x = barraD.x - bola.width
            velBolax = velBolax * -1 

        # Bola colidindo com o obstaculo
        if obstaculo_visivel == True:
            if bola.collided(obstaculo):
                if velBolax > 0:
                    bola.x = obstaculo.x - bola.width
                    velBolax = (velBolax + 50) * -1
                else:
                    bola.x = obstaculo.x + obstaculo.width
                    velBolax = (velBolax - 50) * -1
                
        # Cronometro para obstaculo
        if cronometro_ativo == True:
            cronometro = cronometro - janela.delta_time()
            if cronometro <= 0:
                obstaculo_visivel = False
                cronometro_ativo = False

        # Guardando a pontuação nas variaveis e reiniciando o jogo com a bola no meio
        if bola.x <= -50:
            pontuacaoD += 1
            movendo = False
            bola.x = (1280 - bola.width)/2
            bola.y = (640 - bola.height)/2
            bola.set_position(bola.x,bola.y)
            contador = 0
            cronometro_ativo = False
            obstaculo_visivel = False
            cronometro = 0
            velBolax = 650
            velBolay = 450

        if bola.x + bola.width >= janela.width + 50:
            pontuacaoE += 1
            movendo = False
            bola.x = (1280 - bola.width)/2
            bola.y = (640 - bola.height)/2
            bola.set_position(bola.x,bola.y)
            contador = 0
            cronometro_ativo = False
            obstaculo_visivel = False
            cronometro = 0
            velBolax = 650
            velBolay = 450

    # Desenhando todas as informações na tela
    bola.draw()
    barraE.draw()
    barraD.draw()
    pontuacaoEString = str(pontuacaoE)
    janela.draw_text(pontuacaoEString,(janela.width-1080),(janela.height-540),size=28, color=(0,0,0), font_name="Arial", bold=True, italic=False)
    pontuacaoDString = str(pontuacaoD)
    janela.draw_text(pontuacaoDString,(janela.width - 200),(janela.height-540),size=28, color=(0,0,0), font_name="Arial", bold=True, italic=False)
    
    if obstaculo_visivel == True:
        obstaculo.draw()
    
    if cronometro_ativo == True:
        janela.draw_text("{:.1f}".format(cronometro),((1280 - janela.width)/2),((640 - janela.height)/2),size=28, color=(0,0,0), font_name="Arial", bold=True, italic=False)

    if contador == 3:
        obstaculo_visivel = True
        cronometro_ativo = True
        cronometro = randint(2,4)
        obstaculo.y = (randint(0, 640 - obstaculo.height))
        contador = 0

    janela.update()