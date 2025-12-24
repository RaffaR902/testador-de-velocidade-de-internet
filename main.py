# Importa os componentes do Tkinter para criar a interface gráfica
from tkinter import *

# Importa classes da biblioteca PIL para trabalhar com imagens
from PIL import Image, ImageTk

# Biblioteca para teste de velocidade de internet
import speedtest

# -------- Definição das cores usadas na interface --------
COR_00 = "#f0f3f5"  # Cinza claro
COR_01 = "#feffff"  # Branco
COR_02 = "#3fb5a3"  # Verde água
COR_03 = "#fc766d"  # Vermelho claro
COR_04 = "#403d3d"  # Cinza escuro
COR_05 = "#4a88e8"  # Azul

# -------- Criação da janela principal --------
janela = Tk()                                # Inicializa a janela
janela.title("")                             # Título da janela (vazio)
janela.geometry("350x200")                   # Tamanho da janela
janela.configure(background=COR_01)          # Cor de fundo
janela.resizable(width=FALSE, height=FALSE)  # Impede redimensionamento

# -------- Divisão da janela em dois frames --------

# Frame superior (logo e título)
frame_logo = Frame(janela, width=350, height=60, bg=COR_01)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

# Frame inferior (conteúdo principal)
frame_corpo = Frame(janela, width=350, height=140, bg=COR_01)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

# -------- Configuração do frame do logo --------

imagem = Image.open('images/speed.png')
imagem = imagem.resize((55, 55))     # Redimensiona a imagem
imagem = ImageTk.PhotoImage(imagem)  # Converte para um formato compatível com o Tkinter

# Label para exibir a imagem do logo
label_logo_imagem = Label(
    frame_logo,
    height=60,
    image=imagem,
    compound=LEFT,
    padx=10,
    anchor='nw',
    font=('Arial 16 bold'),
    bg=COR_01,
    fg=COR_03
)
label_logo_imagem.place(x=20, y=0)

# Label com o nome do aplicativo
label_logo_nome = Label(
    frame_logo,
    text='Internet Speed Test',
    padx=10,
    anchor=NE,
    font=('Arial 20'),
    bg=COR_01,
    fg=COR_04
)
label_logo_nome.place(x=75, y=10)

# Linha colorida decorativa abaixo do logo
label_logo_linha = Label(
    frame_logo,
    width=350,
    anchor=NW,
    font=('Arial 1'),
    bg=COR_02
)
label_logo_linha.place(x=0, y=57)


# -------- Configuração do frame do corpo --------

# Valor do download
label_download = Label(
    frame_corpo,
    text='',
    anchor=NW,
    font=('Arial 20'),
    bg=COR_01,
    fg=COR_04
)
label_download.place(x=44, y=25)

# Texto indicando download
label_download_mbps = Label(
    frame_corpo,
    text='Mbps Download',
    anchor=NW,
    font=('Arial 10'),
    bg=COR_01,
    fg=COR_04
)
label_download_mbps.place(x=30, y=70)

# Imagem de download
imagem_download = Image.open('images/down.png')
imagem_download = imagem_download.resize((50, 50))
imagem_download = ImageTk.PhotoImage(imagem_download)
label_logo_imagem = Label(
    frame_corpo,
    height=60,
    image=imagem_download,
    compound=LEFT,
    padx=10,
    anchor='nw',
    font=('Arial 16 bold'),
    bg=COR_01,
    fg=COR_03
)
label_logo_imagem.place(x=130, y=35)

# -------- Upload --------

# Valor do upload
label_upload = Label(
    frame_corpo,
    text='',
    anchor=NW,
    font=('Arial 20'),
    bg=COR_01,
    fg=COR_04
)
label_upload.place(x=235, y=25)

# Texto indicando upload
label_upload_mbps = Label(
    frame_corpo,
    text='Mbps Upload',
    anchor=NW,
    font=('Arial 10'),
    bg=COR_01,
    fg=COR_04
)
label_upload_mbps.place(x=230, y=70)

# Imagem de upload
imagem_upload = Image.open('images/up.png')
imagem_upload = imagem_upload.resize((50, 50))
imagem_upload = ImageTk.PhotoImage(imagem_upload)
label_logo_imagem = Label(
    frame_corpo,
    height=60,
    image=imagem_upload,
    compound=LEFT,
    padx=10,
    anchor='nw',
    font=('Arial 16 bold'),
    bg=COR_01,
    fg=COR_03
)
label_logo_imagem.place(x=170, y=35)

# -------- Função de teste --------
def main():
    st = speedtest.Speedtest()

    download = st.download() / 1024 / 1024
    upload = st.upload() / 1024 / 1024

    label_download.config(text=f"{download:.2f}")
    label_upload.config(text=f"{upload:.2f}")

    botao_testar.config(text="Testar novamente")

    botao_testar['text'] = 'Testar novamente'
    botao_testar.place(x=115, y=100)

# -------- Botão para iniciar o teste --------
botao_testar = Button(
    frame_corpo,
    command=main,
    text='Iniciar teste',
    font='Arial 10 bold',
    relief=RAISED,
    overrelief=RIDGE,
    bg=COR_05,
    fg=COR_01
)
botao_testar.place(x=135, y=100)

# -------- Loop principal da aplicação --------
janela.mainloop()
