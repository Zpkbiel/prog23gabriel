import tkinter as tk
from tkinter import messagebox
import random 

#defininindo as configurações do jogo
NUM_LINHAS = 4
NUM_COLUNAS = 4
CARTAO_SIZE_W = 10
CARTAO_SIZE_H = 5
CORES_CARTAO = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'magenta', 'gray']
COR_FUNDO = "#343a40"
COR_LETRA = "#ffffff"
FONT_STYLE = ('Arial', 12, 'bold')
MAX_TENTATIVAS = 25

# Cria uma grade aleatoria de cores para os cartoes
def create_card_grid():
    cores = CORES_CARTAO * 2
    random.shuffle(cores)
    grid = []

    for _ in range(NUM_LINHAS):
        linha = []
        for _ in range(NUM_COLUNAS):
            if cores:
                cor = cores.pop()
                linha.append(cor)
        grid.append(linha)  
    return grid



# Interagindo com o clique do jogador
def card_clicked(linha, coluna):
    print("Clicado: linha =", linha, "coluna =", coluna)
    cartao = cartoes[linha][coluna]  
    cor = cartao['bg']
    if cor == 'black':
        cartao['bg'] = grid[linha][coluna]
        cartao_revelado.append(cartao)
        if len(cartao_revelado) == 2:
            check_math()


# Verificar se os dois cartoes revelados são iguais
def check_math():
	cartao1, cartao2 = cartao_revelado
	if cartao1['bg'] == cartao2['bg']:
		cartao1.after(1000, cartao1.destroy)
		cartao2.after(1000, cartao2.destroy)
		cartao_correspondentes.extend([cartao1, cartao2])
		check_win()
	else:
		cartao1.after(1000, lambda:cartao1.config(bg='black'))
		cartao2.after(1000, lambda:cartao2.config(bg='black'))
	cartao_revelado.clear()
	update_score()


# Ver se o plyer ganhou
def check_win():
	if len(cartao_correspondentes) == NUM_LINHAS * NUM_COLUNAS:
		messagebox.showinfo('Legal', 'Zerou o jogo!')
		janela.quit()

# Atualizar a pontuacao e verificar se o jogador foi de vasco
def update_score():
    global numero_tentativas
    numero_tentativas += 1
    label_tentativas.config(text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS))
    if numero_tentativas >= MAX_TENTATIVAS:
        messagebox.showinfo('F', 'Voce foi de vasco :/')
        janela.quit()




# Criando a interface principal
janela = tk.Tk()
janela.title('Jogo da Memoria')
janela.configure(bg=COR_FUNDO)


# criar grade de cartoes
grid = create_card_grid()
cartoes = []
cartao_revelado = []
cartao_correspondentes =[]
numero_tentativas = 0


for linha in range(NUM_LINHAS):
    linha_de_cartoes = []
    for coluna in range(NUM_COLUNAS):  # Use NUM_COLUNAS aqui
        cartao = tk.Button(janela, command=lambda linha=linha, coluna=coluna: card_clicked(linha, coluna), width=CARTAO_SIZE_W, height=CARTAO_SIZE_H, bg='black', relief=tk.RAISED, bd=3)
        cartao.grid(row=linha, column=coluna, padx=5, pady=5)  # Use row=linha e column=coluna aqui
        linha_de_cartoes.append(cartao)
    cartoes.append(linha_de_cartoes)




# personalizando o botão
button_style = {'activebackground': '#f8f9fa', 'font' : FONT_STYLE, 'fg' :COR_LETRA}
janela.option_add('*Button' ,button_style)

# lable para numero de tentativas
label_tentativas = tk.Label(janela, text='Tentativas: {}/{}'.format(numero_tentativas, MAX_TENTATIVAS), fg=COR_LETRA, bg=COR_FUNDO, font=FONT_STYLE)
label_tentativas.grid(row=NUM_LINHAS, columnspan=NUM_COLUNAS, padx=10, pady=10)


janela.mainloop()

print(len(cartoes))  # Deve ser igual a NUM_LINHAS
print(len(cartoes[0]))  # Deve ser igual a NUM_COLUNAS
print(len(grid))  # Deve ser igual a NUM_LINHAS
print(len(grid[0]))  # Deve ser igual a NUM_COLUNAS

def card_clicked(linha, coluna):
    print("Clicado: linha =", linha, "coluna =", coluna)
    cartao = cartoes[linha][coluna]

