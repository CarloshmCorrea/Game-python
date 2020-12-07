import pygame #importa o pygame
import math #importa cáculos para o pygame que estão ligadas a movimentação da nave
import random # importação do modo aleatório que foi utilizado nos asteróides

from player import nave # Importa a classe da nave
from objetos import lixos #Importa a classe dos lixos
from objetos1 import lixos1 #Importa a classe dos lixos1
from tiro import laser #Importa a classe do tiro a laser
from tiro1 import laser1 #Importa a classe do tiro a laser

pygame.init()

display = pygame.display.set_mode([840, 480]) #Resolução da tela
pygame.display.set_caption("TInsinando a salvar o planeta") # Nome do game na janela
font = pygame.font.SysFont(None,40) # Tipo e tamanho da fonte do scores

##########MENU##########

#COLOCANDO TUDO DENTRO DE VARIAVEIS

fundo = pygame.image.load('data/menu/fundo.png')
fundo = pygame.transform.scale(fundo, [840, 480])
iniciar = pygame.image.load('data/menu/iniciar.png')
iniciaralt = pygame.image.load('data/menu/iniciaralt.png')
sair = pygame.image.load('data/menu/sair.png')
sairalt = pygame.image.load('data/menu/sairalt.png')
game_over = pygame.image.load('data/img/gameover.jpg')
game_over = pygame.transform.scale(game_over,[840, 480])

#music_menu = pygame.mixer.Sound('data/sound/son_menu1.wav')

WIDTH = 840
HEIGHT = 480

def menu():
    #O MENU SERA CARREGADO A PARTIR DAKI PELA ORDEM 
    display.blit(fundo, (0, 0,))
    display.blit(iniciar, (25, 385))
    display.blit(sair, (600, 385))
    pygame.display.flip()

    pygame.mixer.music.load("data/sound/son_menu1.wav")
    pygame.mixer.music.play(-1)

    while(pygame.event.wait() or pygame.event.get()):

        #PEGAR A POSIÇAODO MOUSE
        mouse = pygame.mouse.get_pos()
        if 25+204 > mouse[0] > 25 and 385+66 > mouse[1] > 385:
            display.blit(iniciaralt, (25, 385))
            if pygame.mouse.get_pressed()[0]:
                jogo()
        else:
            display.blit(iniciar, (25, 385))

        if 600+200 > mouse[0] > 600 and 385+65 > mouse[1] > 385:
            display.blit(sairalt, (600, 385))
            if pygame.mouse.get_pressed()[0]:
                quit()
        else:
            display.blit(sair, (600, 385))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()

        pygame.display.flip()

def gameover():
    display.blit(game_over, (0, 0))

    tela1 = pygame.Rect(45, 415, 152, 42)
    #pygame.draw.rect(display, (255,0,0), tela1)

    tela2 = pygame.Rect(522, 415, 295, 42)
    #pygame.draw.rect(display, (0,255,0), tela2)


    pygame.display.flip()

    while(pygame.event.wait() or pygame.event.get()):

        #PEGAR A POSIÇAO DO MOUSE
        mouse = pygame.mouse.get_pos()
        if 522+295 > mouse[0] > 522 and 415+42 > mouse[1] > 415:
            if pygame.mouse.get_pressed()[0]:
                jogo()

        if 45+152 > mouse[0] > 45 and 415+42 > mouse[1] > 415:
            if pygame.mouse.get_pressed()[0]:
                quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.flip()

##########MENU##########

def jogo():  # Aqui começa as linhas do score
    score_value = 0
    textX = 10
    textY = 10

    def show_score(x, y): 
        score = font.render("Pontuação: " + str(score_value), True, (0,0,0,1))
        display.blit(score, (x, y))
    
    def show_lives(x, y): 
        vidas = font.render("Vidas: " + str(player.lives), True, (0,0,0,1))
        display.blit(vidas, (x, y))


    
    objectGroup = pygame.sprite.Group()
    lixosGroup = pygame.sprite.Group()
    lixos1Group = pygame.sprite.Group()
    laserGroup = pygame.sprite.Group()
    laser1Group = pygame.sprite.Group()

    # Imagem de fundo e suas configurações

    bg = pygame.sprite.Sprite(objectGroup)
    bg.image = pygame.image.load("data/img/fundo3.jpg")
    bg.image = pygame.transform.scale(bg.image, [840, 480])
    bg.rect = bg.image.get_rect()

    player = nave(objectGroup)


    objetos = lixos(objectGroup) # posição/limitação dos lixos
    objetos.rect.center = [100, 200]
    objetos2 = lixos(objectGroup)
    objetos.rect.center = [300, 400]

    objetos4 = lixos1(objectGroup)  # posição/limitação dos lixos
    objetos.rect.center = [100, 200]
    objetos5 = lixos1(objectGroup)
    objetos.rect.center = [300, 400]




    #Músicas

    pygame.mixer.music.load("data/sound/son_fundo1.wav")
    pygame.mixer.music.play(-1)

    #Sons

    shot = pygame.mixer.Sound("data/sound/laser.wav")
    shot1 = pygame.mixer.Sound("data/sound/explosion.wav")
    #shot2 = pygame.mixer.Sound("data/sound/laser2.wav")

    gameLoop = True  #inicio da leitura dos comandos e códigos do jogo
    timer = 0
    clock = pygame.time.Clock()
    if __name__ == "__main__":
        while gameLoop:
            clock.tick(60)
            for event in pygame.event.get(): #Aqui começa a captura dos eventos
                if event.type == pygame.QUIT: #Comando para página não fechar
                    gameLoop = False

                elif event.type == pygame.KEYDOWN: #Tecla de ativa o lase visualmente e sonoro
                    if event.key == pygame.K_j:
                        shot.play()
                        newShot = laser(objectGroup, laserGroup)
                        newShot.rect.center = player.rect.center
                    elif event.key == pygame.K_l:
                        #shot2.play()
                        newShot1 = laser1(objectGroup, laser1Group)
                        newShot1.rect.center = player.rect.center

            #O que fica desenhado na tela
            display.fill([19, 173, 235])


            objectGroup.update()

            timer += 1
            if timer > 30:
                timer = 0
                if random.random() < 0.1:
                    novolixo = lixos(objectGroup, lixosGroup)
                    novolixo1 = lixos1(objectGroup, lixos1Group)

            collisions = pygame.sprite.spritecollide(player, lixosGroup, False, pygame.sprite.collide_mask) #variável da colisão dos lixos e da nave
            collisions1 = pygame.sprite.spritecollide(player, lixos1Group, False, pygame.sprite.collide_mask)

            if collisions:
                shot1.play()
                player.hide()
                player.lives -= 1
                gameLoop = True

            elif collisions1:
                shot1.play()
                player.hide()
                player.lives -= 1
                gameLoop = True

            if player.lives == 0:
                gameLoop = False
                gameover()

            hits = pygame.sprite.groupcollide(laserGroup, lixosGroup, True, True, pygame.sprite.collide_mask) # variável da colisão do tiro laser
            hits1 = pygame.sprite.groupcollide(laser1Group, lixos1Group, True, True, pygame.sprite.collide_mask)

            if hits:
                shot1.play()
                score_value += 1
                gameLoop = True

            elif hits1:
                shot1.play()
                score_value += 1
                gameLoop = True



            objectGroup.draw(display)
            show_lives(textX, (textY * 4))
            show_score(textX, textY)
            pygame.display.update()

menu()
quit()