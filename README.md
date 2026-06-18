# Trabalho Final – Algoritmos I

## 🪐 Disciplina
Algoritmos 1 

## 👨‍🏫 Professor
Carlos Salles

## 👥 Aluno
Arthur Brito Moura e Silva

## 🕹️ Opção de Trabalho
Jogo Interativo 2D (Pygame Wars)

## 📝 Descrição do Projeto
Este projeto consiste no desenvolvimento de um jogo temático baseado no universo de *Star Wars*. O jogador comanda a nave de um jovem Padawan tentando escapar das forças do Império após a Ordem 66. O objetivo principal é movimentar a nave para desviar de asteroides e combater caças inimigos (TIE Fighters) enquanto a barra de energia é carregada para habilitar o salto no Hiperespaço.

O sistema foi desenvolvido aplicando conceitos fundamentais de **Programação Estruturada**, utilizando um loop principal de eventos, estruturas condicionais para inteligência artificial básica dos inimigos, listas dinâmicas para o controle de elementos na tela (tiros e asteroides) e sistemas de colisão baseados em coordenadas matemáticas e matrizes de pixels. O jogo possui 3 estágios de pontuação, cada um apresentando mensagens na tela e novas dinâmicas, além de um Menu, uma Introdução e tela de Game Over.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python (Versão 3.14.4)
* **Biblioteca Gráfica/Áudio:** Pygame-ce (Versão 2.5.7)
* **IDE:** Visual Studio Code (VS Code)

---

## 📁 Estrutura do Projeto

Jogos_Pygame/
│
├── imagens/
│   ├── asteroides.png
│   ├── jedi.png
│   └── tie.png
│
├── sons/
│   ├── duel_of_the_fates.mp3
│   ├── star_wars_theme.mp3
│   ├── tie_fighter.mp3
│   └── vader_breath.mp3
│
├── PygameWars.py
├── README.md
└── trabalho_final.py

## 🚀 Execução

Após abrir o diretório do projeto no VS Code, abra o terminal e execute o comando abaixo para iniciar o jogo:

python PygameWars.py 