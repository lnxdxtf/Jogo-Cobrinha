import pygame
from pygame.locals import*
from sys import exit
from random import randint

pygame.init()

####fundo
pygame.mixer.music.set_volume(0.3)
musica_fundo = pygame.mixer.music.load('BoxCat Games - Inspiration.mp3')
pygame.mixer.music.play(-1)
###colisao
colisao_som = pygame.mixer.Sound('smw_message_block.wav')

game_over_som = pygame.mixer.Sound('smw_game_over.wav')

larg_ = 1080
alt_ = 620



x_cobra = int(larg_/2)
y_cobra = int(alt_/2)
vel = 5
x_controle = vel
y_controle= 0

x_maça = randint(60, 1020)
y_maça = randint(60, 560)

lista_cobra = []
comprimento_inicial = 10

morreu = False



def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,100,0),(XeY[0],XeY[1],40,40))

def reiniciar_jogo():
    global pontos,comprimento_inicial,x_cobra,y_cobra,lista_cobra,lista_cabeça,x_maça,y_maça,morreu
    pontos = 0
    comprimento_inicial = 10
    x_cobra = int(larg_/2)
    y_cobra = int(alt_/2)
    lista_cabeça = []
    lista_cobra = []
    x_maça = randint(60, 1020)
    y_maça = randint(60, 560)
    morreu = False
    pygame.mixer.music.play(-1)


fonte = pygame.font.SysFont('arial', 50, True, True)
pontos = 0

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((larg_,alt_))
pygame.display.set_caption('JOGO DO PAI')

while True:
    relogio.tick(60)
    tela.fill((255,255,255))

    mensagem = f'Pontos: {pontos}'
    texto_format = fonte.render(mensagem, True, (85,85,85))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
        if event.type == KEYDOWN:
            if event.key == K_a:
                x_controle = -vel
                y_controle = 0
            if event.key == K_d:
                x_controle = vel
                y_controle = 0
            if event.key == K_s:
                y_controle = vel
                x_controle = 0
            if event.key == K_w:
                y_controle = -vel
                x_controle = 0
    
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle
    '''if pygame.key.get_pressed()[K_a]:
        x_cobra = x_cobra-5
    if pygame.key.get_pressed()[K_d]:
        x_cobra = x_cobra+5
    if pygame.key.get_pressed()[K_s]:
        y_cobra = y_cobra+5
    if pygame.key.get_pressed()[K_w]:
        y_cobra = y_cobra-5'''

    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,40,40))
    maça = pygame.draw.rect(tela,(255,0,0),(x_maça,y_maça,40,40))
    
    if cobra.colliderect(maça):
        x_maça = randint(60, 1020)
        y_maça = randint(60, 560)
        comprimento_inicial = comprimento_inicial+5
        pontos = pontos+10
        
        colisao_som.play()

    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    lista_cobra.append(lista_cabeça)
    aumenta_cobra(lista_cobra)

    if lista_cobra.count(lista_cabeça)>1:
        fonte2 = pygame.font.SysFont('arial', 40, True,True)
        mensagem_gameover = 'Gamer Over! Pressione "R" para reiniciar'
        texto_format_over = fonte2.render(mensagem_gameover, True, (255,0,0))
        game_over_som.play()
        pygame.mixer.music.stop()
        tela.fill((0,0,0))
        ret_texto = texto_format_over.get_rect()
        morreu = True
        while morreu:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (larg_//2,alt_//2)
            tela.blit(texto_format_over, ret_texto)
            pygame.display.update()

    if x_cobra >larg_:
        x_cobra = 0
    if x_cobra < 0 :
        x_cobra = larg_
    if y_cobra > alt_:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = alt_


    if len(lista_cobra)>comprimento_inicial:
        del lista_cobra[0]
    




    tela.blit(texto_format, (760,10))
    pygame.display.update()
