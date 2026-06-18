import pygame
import random 

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("sons/star_wars_theme.mp3")

som_blaster = pygame.mixer.Sound("sons/tie_fighter.mp3")
som_blaster.set_volume(0.4)
som_vader = pygame.mixer.Sound("sons/vader_breath.mp3")
som_vader.set_volume(0.6)

info = pygame.display.Info()
LARGURA = info.current_w
ALTURA = info.current_h

tela = pygame.display.set_mode((LARGURA, ALTURA), pygame.FULLSCREEN)
pygame.display.set_caption("Pygame Wars")

fonte_titulo = pygame.font.SysFont("arial", 100, bold = True)
fonte_texto = pygame.font.SysFont("arial", 40)
fonte_interface = pygame.font.SysFont("arial", 30)
fonte_vitoria = pygame.font.SysFont("arial", 60, bold = True)
fonte_creditos = pygame.font.SysFont("arial", 35)

texto_intro = ["PYGAME WARS", "", "", "", "", "", "", "", "A República caiu.", "", "O Senador Palpatine, secretamente um Lorde Sith,", "", "declarou-se Imperador e instituiu o Império Galático.", "", "Coruscant e o templo Jedi foram completamente tomados e destruídos.", "", "Anakin Skywalker, aprendiz de Obi-Wan Kenobi, foi corrompido", "pelo Lorde Sidious e tornou-se Darth Vader.", "", "Os Jedi foram mortos por toda a galáxia, traídos por soldados clones da própria República", "", "sob o comando de Palpatine, que os programou para executar a Ordem 66.", "", "Entretanto, alguns Jedi sobreviveram ao expurgo e,", "", "em algum lugar da vasta galáxia, um jovem padawan foge com sua nave,", "", "que precisa de energia para saltar no hiperespaço", "", " e escapar das maõs do Império..."]
posicao_y = ALTURA

jedi_img = pygame.image.load("imagens/jedi.png")
tie_img = pygame.image.load("imagens/tie.png")
asteroide_img = pygame.image.load("imagens/asteroides.png")
jedi_img = pygame.transform.scale(jedi_img, (70, 70))
tie_img = pygame.transform.scale(tie_img, (70, 70))
asteroide_img = pygame.transform.scale(asteroide_img, (50, 50))

jogador_x = LARGURA // 2
jogador_y = 120

vidas = 5
energia_hiperespaco = 0 
velocidade = 8 

inimigo1_x = LARGURA // 4
inimigo1_y = ALTURA - 120 

inimigo2_x = LARGURA // 2
inimigo2_y = ALTURA - 120

inimigo3_x = 3 * LARGURA // 4
inimigo3_y = ALTURA - 120 

inimigo1_ativo = True
inimigo2_ativo = True
inimigo3_ativo = True

vel_inimigos = 3
direcao = 1

tiros_jedi = []
tiros_inimigos = []
asteroides = []

ultimo_ponto = pygame.time.get_ticks()
ultimo_asteroide = pygame.time.get_ticks()
ultimo_tiro_inimigo = pygame.time.get_ticks()

tempo_hiperespaco = 0
tempo_mensagem = 0

estado = "MENU"

game_over = False 

hiperespaco_disponivel = False

venceu = False

rodando = True

evento_400 = False
evento_600 = False

mensagem_evento = ""

estrelas = []
for i in range (200):
    x = random.randint(0, LARGURA,)
    y = random.randint(0, ALTURA)
    tamanho = random.randint(1,3)
    estrelas.append((x, y, tamanho))

clock = pygame.time.Clock()

pygame.mixer.music.play()

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            rodando = False

        if evento.type == pygame.KEYDOWN:
            if estado == "MENU":
                if evento.key == pygame.K_RETURN:
                    estado = "INTRO"
                    pygame.mixer.music.play(-1)

            if estado == "JOGO":
                if evento.key == pygame.K_SPACE:
                    if energia_hiperespaco >= 600:
                        tiros_jedi.append([jogador_x, jogador_y + 30])
                        som_blaster.play()

            if evento.key == pygame.K_ESCAPE:
                rodando = False

            if game_over and evento.key == pygame.K_r:
                som_vader.stop()
                pygame.mixer.music.load("sons/duel_of_the_fates.mp3")
                pygame.mixer.music.set_volume(0.6)
                pygame.mixer.music.play(-1)

                game_over = False
                vidas = 5
                energia_hiperespaco = 0 

                inimigo1_ativo = True
                inimigo2_ativo = True
                inimigo3_ativo = True

                jogador_x = LARGURA // 2
                jogador_y = 120

                inimigo1_x = LARGURA // 4
                inimigo1_y = ALTURA - 120
                inimigo2_x = LARGURA // 2
                inimigo2_y = ALTURA - 120
                inimigo3_x = 3 * LARGURA // 4
                inimigo3_y = ALTURA - 120

                tiros_inimigos.clear()
                tiros_jedi.clear()
                asteroides.clear()

                evento_400 = False
                evento_600 = False
                mensagem_evento = ""
                hiperespaco_disponivel = False
                venceu = False

                ultimo_ponto = pygame.time.get_ticks()
                ultimo_asteroide = pygame.time.get_ticks()
                ultimo_tiro_inimigo = pygame.time.get_ticks()

            if hiperespaco_disponivel and evento.key == pygame.K_h:
                pygame.mixer.music.stop()
                pygame.mixer.stop()
                estado = "HIPERESPACO"
                tempo_hiperespaco = pygame.time.get_ticks()

    tela.fill((0, 0, 0))
    for estrela in estrelas:
        pygame.draw.circle(tela, (255, 255, 255), (estrela[0], estrela[1]), estrela[2])

    if estado == "MENU":
        titulo = fonte_titulo.render("PYGAME WARS", True, (255, 255, 0))
        instrucoes = fonte_texto.render("Pressione ENTER para iniciar", True, (255, 255, 255))
        autor = fonte_interface.render("Arthur Brito Moura e Silva", True, (255, 255, 255))
        texto_disciplina = fonte_creditos.render("Algoritmos 1", True, (255, 255, 255))

        tela.blit(titulo, (LARGURA // 2 - titulo.get_width() // 2, 150))
        tela.blit(instrucoes, (LARGURA // 2 - instrucoes.get_width() // 2, 350))
        tela.blit(autor, (20, ALTURA - 50))
        tela.blit(texto_disciplina, (LARGURA - texto_disciplina.get_width() - 20, ALTURA - texto_disciplina.get_height() - 20))

    if estado == "INTRO":
        y = posicao_y
        posicao_y -= 0.5

        for linha in texto_intro:
            if linha == "PYGAME WARS":
                superficie = fonte_titulo.render(linha, True, (255, 255, 0))
            else:
                superficie = fonte_texto.render(linha, True, (255, 255, 0))

            x = (LARGURA - superficie.get_width())// 2
            tela.blit(superficie, (x, y))
            y += 45

        if posicao_y < -1500:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("sons/duel_of_the_fates.mp3")
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(-1)
            estado = "JOGO"
            print ("Entrou no jogo")
            
    elif estado == "JOGO":
        if game_over:
            tela.fill((0, 0, 0))
            texto_fim = fonte_titulo.render("ORDEM 66 EXECUTADA", True, (255, 0, 0))
            texto_reinicio = fonte_texto.render("Pressione R para Reiniciar", True, (255, 255, 255))
            tela.blit(texto_fim, (LARGURA // 2 - texto_fim.get_width() // 2, ALTURA // 2))
            tela.blit(texto_reinicio, (LARGURA // 2 - texto_reinicio.get_width() // 2, ALTURA // 2 + 100))

        else:
            pygame.draw.rect(tela, (80,  80, 80), (LARGURA // 2 - 250, 30, 500, 30))
            largura_barra = (energia_hiperespaco / 1000) * 500
            pygame.draw.rect(tela, (0, 255, 0), (LARGURA // 2 - 250, 30, largura_barra, 30))

            x_barra = LARGURA // 2 - 250
            x_400 = x_barra + (400 / 1000) * 500
            x_600 = x_barra + (600 / 1000) * 500
            pygame.draw.line(tela, (255, 255, 255), (x_400, 25), (x_400, 75), 4)
            pygame.draw.line(tela, (255, 255, 255), (x_600, 25), (x_600, 75), 4)

            tempo_atual = pygame.time.get_ticks()

            if tempo_atual - ultimo_ponto >= 1500:
                energia_hiperespaco += 10
                ultimo_ponto = tempo_atual

            if energia_hiperespaco >= 1000:
                hiperespaco_disponivel = True

                if energia_hiperespaco > 1000:
                    energia_hiperespaco = 1000

                ultimo_ponto = tempo_atual


            if energia_hiperespaco >= 400 and evento_400 == False:
                mensagem_evento = "CINTURÃO DE ASTERÓIDES DETECTADO"
                tempo_mensagem = tempo_atual
                evento_400 = True

            if energia_hiperespaco >=600 and evento_600 == False:
                mensagem_evento = "DEFESAS ATIVADAS"
                tempo_mensagem = tempo_atual
                evento_600 = True

            if energia_hiperespaco >= 1000:
                hiperespaco_disponivel = True

            if energia_hiperespaco >= 400:
                tempo_atual = pygame.time.get_ticks()
                if tempo_atual - ultimo_asteroide >= 1000:
                    x = random.randint(25, LARGURA - 25)
                    asteroides.append([x, 0])
                    ultimo_asteroide = tempo_atual
            
            if tempo_atual - ultimo_tiro_inimigo >= 800:
                if inimigo1_ativo:
                    tiros_inimigos.append([inimigo1_x, inimigo1_y])

                if inimigo2_ativo:
                    tiros_inimigos.append([inimigo2_x, inimigo2_y])

                if inimigo3_ativo:
                    tiros_inimigos.append([inimigo3_x, inimigo3_y])

                if inimigo1_ativo or inimigo2_ativo or inimigo3_ativo:
                    som_blaster.play()

                ultimo_tiro_inimigo = tempo_atual


            teclas = pygame.key.get_pressed()

            if teclas[pygame.K_a]:
                jogador_x -= velocidade

            if teclas[pygame.K_d]:
                jogador_x += velocidade
            
            if teclas[pygame.K_w]:
                jogador_y -= velocidade

            if teclas[pygame.K_s]:
                jogador_y += velocidade


            if jogador_x < 100:
                jogador_x = 100
            if jogador_x > LARGURA - 100:
                jogador_x = LARGURA - 100
            if jogador_y < 20:
                jogador_y = 20
            if jogador_y > ALTURA // 2:
                jogador_y = ALTURA // 2


            if inimigo1_ativo:
                inimigo1_x += vel_inimigos * direcao
            if inimigo2_ativo:
                inimigo2_x += vel_inimigos * direcao
            if inimigo3_ativo:
                inimigo3_x += vel_inimigos * direcao 


            for asteroide in asteroides:
                asteroide[1] += 5
            for tiro in tiros_jedi: 
                tiro[1] += 8
            for tiro in tiros_inimigos:
                tiro[1] -= 4

            for tiro in tiros_jedi:
                if inimigo1_ativo and abs(tiro[0] - inimigo1_x) < 25 and abs(tiro[1] - inimigo1_y) < 25:
                    inimigo1_ativo = False
                    energia_hiperespaco += 100
                    tiros_jedi.remove(tiro)
                elif inimigo2_ativo and abs(tiro[0] - inimigo2_x) < 25 and abs(tiro[1] - inimigo2_y) < 25:
                    inimigo2_ativo = False
                    energia_hiperespaco += 100
                    tiros_jedi.remove(tiro)
                elif inimigo3_ativo and abs(tiro[0] - inimigo3_x) < 25 and abs(tiro[1] - inimigo3_y) < 25:
                    inimigo3_ativo = False
                    energia_hiperespaco += 100
                    tiros_jedi.remove(tiro)

            for asteroide in asteroides:
                distancia_x = abs(asteroide[0] - jogador_x)
                distancia_y = abs(asteroide[1] - jogador_y)
                
                if distancia_x < 25 and distancia_y < 25:
                    vidas -= 1
                    asteroide[1] = ALTURA + 100

            for tiro in tiros_inimigos:
                distancia_x = abs(tiro[0] - jogador_x)
                distancia_y = abs(tiro[1] - jogador_y)

                if distancia_x < 20 and distancia_y < 20:
                    vidas -= 1
                    tiro[1] = - 100

            if vidas <= 0 and not game_over:
                pygame.mixer.music.stop()
                pygame.mixer.stop()
                som_vader.play(-1)
                game_over = True

            if inimigo3_x > LARGURA - 100:
                direcao = -1

            if inimigo1_x < 100:
                direcao = 1

            texto_energia = fonte_interface.render("Energia para o Salto no Hiperespaço", True, (255, 255, 255))
            texto_vidas = fonte_interface.render(f"Vidas: {vidas}", True, (255, 255, 255))

            tela.blit(texto_energia, (LARGURA // 2 - texto_energia.get_width() // 2, 0))
            tela.blit(texto_vidas, (30, 30))

            pygame.draw.rect(tela, (80, 80, 80), (LARGURA // 2 - 250, 35, 500, 30))
            largura_barra = (energia_hiperespaco / 1000) * 500
            pygame.draw.rect(tela, (0, 255, 0), (LARGURA // 2 - 250, 35, largura_barra, 30))

            if vidas == 1 and  not hiperespaco_disponivel:
                texto_critico = fonte_texto.render("ESCUDOS EM ESTADO CRÍTICO", True, (255, 0, 0))
                tela.blit(texto_critico, (LARGURA // 2 - texto_critico.get_width() // 2, ALTURA // 2 - 100))

            tela.blit(jedi_img, (jogador_x - 25, jogador_y - 25))

            if inimigo1_ativo:
                tela.blit(tie_img, (inimigo1_x - 25, inimigo1_y - 25))

            if inimigo2_ativo:
                tela.blit(tie_img, (inimigo2_x - 25, inimigo2_y - 25))

            if inimigo3_ativo:
                tela.blit(tie_img, (inimigo3_x - 25, inimigo3_y - 25))


            for tiro in tiros_jedi:
                pygame.draw.line(tela, (0, 255, 0), (tiro[0], tiro [1]), (tiro[0], tiro[1] + 15), 3)

            for tiro in tiros_inimigos:
                pygame.draw.line(tela, (255, 0, 0), (tiro[0], tiro[1]), (tiro[0], tiro[1] - 15), 3)


            if mensagem_evento != "":
                texto_msg = fonte_texto.render(mensagem_evento, True, (255, 255, 0))
                tela.blit(texto_msg, (LARGURA // 2- texto_msg.get_width() // 2, ALTURA // 2))
            
            if hiperespaco_disponivel:
                texto_hiper = fonte_texto.render("SALTO PARA O HIPERESPAÇO DISPONÍVEL", True, (255, 255, 0))
                texto_h = fonte_texto.render("PRESSIONE H", True, (255, 255, 255))
                tela.blit(texto_hiper, (LARGURA // 2 - texto_hiper.get_width() // 2, ALTURA // 2 - 100))
                tela.blit(texto_h, (LARGURA // 2 - texto_h.get_width() // 2, ALTURA // 2))

            if tempo_atual - tempo_mensagem > 3000:
                mensagem_evento = ""

            for asteroide in asteroides:
                tela.blit(asteroide_img, (asteroide[0] - 20, asteroide[1] - 20))
        
    elif estado == "HIPERESPACO":
        tela.fill((0, 0, 0))

        for estrela in estrelas:
            pygame.draw.line(tela, (255, 255, 255), (estrela[0], estrela[1]), (estrela[0], estrela[1] + 80), 3)
        
        if pygame.time.get_ticks() - tempo_hiperespaco > 3000:
            texto_vitoria = fonte_vitoria.render("VOCÊ SOBREVIVEU À ORDEM 66", True, (255, 255, 0))
            tela.blit(texto_vitoria, (LARGURA // 2 - texto_vitoria.get_width() // 2, ALTURA // 2))
   
    pygame.display.flip()
    clock.tick(60)
   
pygame.quit()