# Importando Módulos
import pygame
from pygame import mixer
import random
import time
import random
from tkinter import *

# Inicializando o pygame
pygame.init()
pygame.display.set_caption("Ludo")
screen = pygame.display.set_mode((680, 600))

# Carregando Imagens
tabuleiro = pygame.image.load('tabuleiro.jpg')
estrela = pygame.image.load('doutor-fran.jpg')
um = pygame.image.load('1.png')
dois = pygame.image.load('2.png')
tres = pygame.image.load('3.png')
quatro = pygame.image.load('4.png')
cinco = pygame.image.load('5.png')
seis = pygame.image.load('6.png')

vermelho = pygame.image.load('vermelha.png')
azul = pygame.image.load('azul.png')
verde = pygame.image.load('verde.png')
amarelo = pygame.image.load('amarela.png')

func_a = pygame.image.load('grafico.webp')
func_b = pygame.image.load('grafico2.webp')



DADO = [um, dois, tres, quatro, cinco, seis]
cor = [vermelho, verde, amarelo, azul]
graficos = [func_a, func_b]

class Pergunta:
    def __init__(self, pergunta, opcoes, correta, imagem):
        self.pergunta = pergunta
        self.opcoes = opcoes
        self.correta = correta
        self.imagem = pygame.image.load('grafico.webp')

pergunta1 = Pergunta("Qual é a forma geral de uma função afim?", ["a) y = ax^2 + b", "b) y = ax + b", "c) y = x^2 + a", "d) y = x - b"], 1, ("grafico.webp"))
pergunta2 = Pergunta("O que é necessário para que uma função afim seja crescente?", ["O coeficiente angular (a) deve ser positivo.", "b) O coeficiente angular (a) deve ser negativo.", "c) O coeficiente linear (b) deve ser positivo."], 0, ("grafico2.webp"))


# Inicializando Variáveis
numero = 1
jogadorAtual = 0
peçaMorta = False
dadoRolado = False
classificaçãoVencedor = []

jogadores_responderam = [False, False, False, False]

# Renderizando Texto
fonte = pygame.font.Font('freesansbold.ttf', 11)
FONT = pygame.font.Font('freesansbold.ttf', 16)
textoJogadorAtual = fonte.render('Jogador Atual', True, (0, 0, 0))
linha = fonte.render('------------------------------------', True, (0, 0, 0))




# Blit no loop while
def blit_tudo():
    for i in SEGURA[4:]:
        screen.blit(estrela, i)

    for i in range(len(posição)):
        for j in posição[i]:
            screen.blit(cor[i], j)

    screen.blit(DADO[numero-1], (605, 270))

    screen.blit(cor[jogadorAtual], (620, 28))
    screen.blit(textoJogadorAtual, (600, 10))
    screen.blit(linha, (592, 59))

    for i in range(len(classificaçãoVencedor)):
        rank = FONT.render(f'{i+1}.', True, (0, 0, 0))
        screen.blit(rank, (600, 85 + (40*i)))
        screen.blit(cor[classificaçãoVencedor[i]], (620, 75 + (40*i)))

# # Função de verificação das respostas do usuário para perguntas
# def resposta_ver():
    

# É possível mover a peça?
def para_casa(x, y):
    #  R2
    if (posição[x][y][1] == 284 and posição[x][y][0] <= 202 and x == 0) \
            and (posição[x][y][0] + 38*numero > VENCEDOR[x][0]):
        return False
    #  Y2
    elif (posição[x][y][1] == 284 and 368 < posição[x][y][0] and x == 2) \
            and (posição[x][y][0] - 38*numero < VENCEDOR[x][0]):
        return False
    #  G2
    elif (posição[x][y][0] == 284 and posição[x][y][1] <= 202 and x == 1) \
            and (posição[x][y][1] + 38*numero > VENCEDOR[x][1]):
        return False
    #  B2
    elif (posição[x][y][0] == 284 and posição[x][y][1] >= 368 and x == 3) \
            and (posição[x][y][1] - 38*numero < VENCEDOR[x][1]):
        return False
    return True

# Definindo Coordenadas Importantes
CASA = [[(110, 58),  (61, 107),  (152, 107), (110, 152)],  # Vermelho
        [(466, 58),  (418, 107), (509, 107), (466, 153)],  # Verde
        [(466, 415), (418, 464), (509, 464), (466, 510)],  # Amarelo
        [(110, 415), (61, 464),  (152, 464), (110, 510)]]  # Azul

SEGURA = [(50, 240), (328, 50), (520, 328), (240, 520),
          (88, 328), (240, 88), (482, 240), (328, 482)]

posição = [[[110, 58],  [61, 107],  [152, 107], [110, 152]],  # Vermelho
            [[466, 58],  [418, 107], [509, 107], [466, 153]],  # Verde
            [[466, 415], [418, 464], [509, 464], [466, 510]],  # Amarelo
            [[110, 415], [61, 464],  [152, 464], [110, 510]]]  # Azul

pulo = {(202, 240): (240, 202),  # R1 -> G3
        (328, 202): (368, 240),  # G1 -> Y3
        (368, 328): (328, 368),  # Y1 -> B3
        (240, 368): (202, 328)}  # B1 -> R3

VENCEDOR = [[240, 284], [284, 240], [330, 284], [284, 330]]

# Blit do Movimento das Peças
def mostrar_peça(x, y):
    screen.fill((255, 255, 255))
    screen.blit(tabuleiro, (0, 0))

    for i in SEGURA[4:]:
        screen.blit(estrela, i)

    for i in range(len(posição)):
        for j in posição[i]:
            screen.blit(cor[i], j)

    screen.blit(DADO[numero-1], (605, 270))
    

    

    screen.blit(cor[jogadorAtual], (620, 28))
    screen.blit(textoJogadorAtual, (600, 10))
    screen.blit(linha, (592, 59))

    for i in range(len(classificaçãoVencedor)):
        rank = FONT.render(f'{i+1}.', True, (0, 0, 0))
        screen.blit(rank, (600, 85 + (40*i)))
        screen.blit(cor[classificaçãoVencedor[i]], (620, 75 + (40*i)))

    pygame.display.update()
    time.sleep(0.5)



def mover_peça(x, y):
    global jogadorAtual, dadoRolado

    if tuple(posição[x][y]) in CASA[jogadorAtual] and numero == 6:
        posição[x][y] = list(SEGURA[jogadorAtual])
        dadoRolado = False


    elif tuple(posição[x][y]) not in CASA[jogadorAtual]:
        dadoRolado = False
        if not numero == 6:
            jogadorAtual = (jogadorAtual+1) % 4

        
        if (posição[x][y][1] == 284 and posição[x][y][0] <= 202 and x == 0) \
                and (posição[x][y][0] + 38*numero <= VENCEDOR[x][0]):
            for i in range(numero):
                posição[x][y][0] += 38
                mostrar_peça(x, y)

        #  Y2
        elif (posição[x][y][1] == 284 and 368 < posição[x][y][0] and x == 2) \
                and (posição[x][y][0] - 38*numero >= VENCEDOR[x][0]):
            for i in range(numero):
                posição[x][y][0] -= 38
                mostrar_peça(x, y)

        #  G2
        elif (posição[x][y][0] == 284 and posição[x][y][1] <= 202 and x == 1) \
                and (posição[x][y][1] + 38*numero <= VENCEDOR[x][1]):
            for i in range(numero):
                posição[x][y][1] += 38
                mostrar_peça(x, y)
        #  B2
        elif (posição[x][y][0] == 284 and posição[x][y][1] >= 368 and x == 3) \
                and (posição[x][y][1] - 38*numero <= VENCEDOR[x][1]):
            for i in range(numero):
                posição[x][y][1] -= 38
                mostrar_peça(x, y)

        # Outros Caminhos
        else:
            for _ in range(numero):
                #  R1, Y3
                if (posição[x][y][1] == 240 and posição[x][y][0] < 202) \
                        or (posição[x][y][1] == 240 and 368 <= posição[x][y][0] < 558):
                    posição[x][y][0] += 38
                # R3 -> R2 -> R1
                elif (posição[x][y][0] == 12 and posição[x][y][1] > 240):
                    posição[x][y][1] -= 44

                #  R3, Y1
                elif (posição[x][y][1] == 328 and 12 < posição[x][y][0] <= 202) \
                        or (posição[x][y][1] == 328 and 368 < posição[x][y][0]):
                    posição[x][y][0] -= 38
                #  Y3 -> Y2 -> Y1
                elif (posição[x][y][0] == 558 and posição[x][y][1] < 328):
                    posição[x][y][1] += 44

                #  G3, B1
                elif (posição[x][y][0] == 240 and 12 < posição[x][y][1] <= 202) \
                        or (posição[x][y][0] == 240 and 368 < posição[x][y][1]):
                    posição[x][y][1] -= 38
                # G3 -> G2 -> G1
                elif (posição[x][y][1] == 12 and 240 <= posição[x][y][0] < 328):
                    posição[x][y][0] += 44

                #  B3, G1
                elif (posição[x][y][0] == 328 and posição[x][y][1] < 202) \
                        or (posição[x][y][0] == 328 and 368 <= posição[x][y][1] < 558):
                    posição[x][y][1] += 38
                #  B3 -> B2 -> B1
                elif (posição[x][y][1] == 558 and posição[x][y][0] > 240):
                    posição[x][y][0] -= 44

                else:
                    for i in pulo:
                        if posição[x][y] == list(i):
                            posição[x][y] = list(pulo[i])
                            break

                mostrar_peça(x, y)

        # Matando Jogador
        if tuple(posição[x][y]) not in SEGURA:
            for i in range(len(posição)):
                for j in range(len(posição[i])):
                    if posição[i][j] == posição[x][y] and i != x:
                        posição[i][j] = list(CASA[i][j])
                
                        jogadorAtual = (jogadorAtual+3) % 4
                        

# Verificando Vencedor
def verificar_vencedor():
    global jogadorAtual
    if jogadorAtual not in classificaçãoVencedor:
        for i in posição[jogadorAtual]:
            if i not in VENCEDOR:
                return
        classificaçãoVencedor.append(jogadorAtual)
    else:
        jogadorAtual = (jogadorAtual + 1) % 4

pergunta_atual = None
escolha_do_jogador = None
dadoRolado = False

# Loop Principal
executando = True
while(executando):
    screen.fill((255, 255, 255))
    screen.blit(tabuleiro, (0, 0))  # Blit do Tabuleiro

    verificar_vencedor()
    
    # Defina coordenada como None antes do loop de eventos
    
    coordenada = None
    

    for evento in pygame.event.get():

        # Evento QUIT
        if evento.type == pygame.QUIT:
            executando = False

        # Quando o MOUSE é clicado
        if evento.type == pygame.MOUSEBUTTONUP:
            coordenada = pygame.mouse.get_pos()

            # Rolar o Dado
            if not dadoRolado and (605 <= coordenada[0] <= 669) and (270 <= coordenada[1] <= 334):
                numero = random.randint(1, 6)
                
                if numero == 6 or jogadores_responderam[jogadorAtual] == True:
                    # Se o dado for 6, defina a pergunta atual
                    pergunta_atual = pergunta1
                    escolha_do_jogador = None
                    cor_atual = cor[jogadorAtual]

                flag = True
                for i in range(len(posição[jogadorAtual])):
                    if tuple(posição[jogadorAtual][i]) not in CASA[jogadorAtual] and para_casa(jogadorAtual, i):
                        flag = False
                if (flag and numero == 6) or not flag:
                    dadoRolado = True
                    
                else:
                    jogadorAtual = (jogadorAtual+1) % 4
                    
             # Verifique se o clique está dentro das opções e armazene a escolha do jogador
            if escolha_do_jogador is None and pergunta_atual is not None:
                for i, opcao in enumerate(pergunta_atual.opcoes):
                    opcao_x = 50
                    opcao_y = 430 + i * 30
                    opcao_rect = pygame.Rect(opcao_x, opcao_y, 50, 50)

                    if opcao_rect.collidepoint(coordenada):
                        escolha_do_jogador = i  # A opção selecionada é armazenada em escolha_do_jogador
            
            # Se o jogador escolheu uma opção           
            if escolha_do_jogador is not None and pergunta_atual is not None:
                if escolha_do_jogador == pergunta_atual.correta:
                    # O jogador escolheu a opção correta, pare de exibir a pergunta
                    pergunta_atual = None
                    dadoRolado = True
                    jogadores_responderam[jogadorAtual] = True
                else:
                    # O jogador escolheu a opção incorreta, vá para o próximo jogador
                    jogadorAtual = (jogadorAtual + 1) % 4
                    pergunta_atual = None
                    dadoRolado = False

        # Exibir a pergunta e as opções
    if pergunta_atual is not None:
        texto_pergunta = fonte.render(pergunta_atual.pergunta, True, (0, 0, 0))
        screen.blit(texto_pergunta, (50, 400))

        for i, opcao in enumerate(pergunta_atual.opcoes):
            texto_opcao = fonte.render(f"{i+1}. {opcao}", True, (0, 0, 0))
            screen.blit(texto_opcao, (50, 430 + i * 30))

    #Movendo Jogador
    if dadoRolado and coordenada is not None and escolha_do_jogador != -1 and pergunta_atual is None:
        for j in range(len(posição[jogadorAtual])):
            if posição[jogadorAtual][j][0] <= coordenada[0] <= posição[jogadorAtual][j][0]+31 \
                    and posição[jogadorAtual][j][1] <= coordenada[1] <= posição[jogadorAtual][j][1]+31:
                mover_peça(jogadorAtual, j)
                break

    

    blit_tudo()
    
    pygame.display.flip()