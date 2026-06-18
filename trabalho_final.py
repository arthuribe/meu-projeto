import pygame
import random

pygame.init()

tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Trabalho Final de Algoritmos 1")

x = 375
y = 500

rodando = True

clock = pygame.time.Clock()

obstaculos = [[100,0], [300, 200], [500, 400]]

pontuacao = 0

fonte = pygame.font.Font(None, 36)

while rodando:

    clock.tick(60)  

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_d]:
        x += 5

    if teclas[pygame.K_a]:
        x -= 5

    if x < 0:
        x = 0
    
    if x > 750:
        x = 750
    
    if y < 0:
        y = 0
    
    if y > 550:
        y = 550

    for obstaculo in obstaculos:

        obstaculo[1] += 5

        if obstaculo[1] > 600:
         obstaculo[1] = 0
         obstaculo[0] = random.randint(0, 750)
         pontuacao += 1

    tela.fill((0, 0, 0))

    texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, (255, 255, 255))

    tela.blit(texto_pontos, (10, 10))

    pygame.draw.rect(tela, (255, 0, 0), (x, y, 50, 50))
    
    for obstaculo in obstaculos:

         pygame.draw.rect(tela, (0, 255, 0), (obstaculo[0], obstaculo[1], 50, 50))
       
    jogador = pygame.Rect(x, y, 50, 50)

    for obstaculo in obstaculos:

     retangulo_obstaculo = pygame.Rect(obstaculo[0], obstaculo[1], 50, 50)
        
     if jogador.colliderect(retangulo_obstaculo):
        rodando = False

    pygame.display.update()

pygame.quit() 