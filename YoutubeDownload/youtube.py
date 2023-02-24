from tkinter import * 
from pytube import YouTube
from tkinter import filedialog
from pytube.exceptions import RegexMatchError

# Criação de janela para receber os dados do úsuario
janela = Tk()
janela.title('Baixando videos do Youtube')

# Função para realizar o download do link inserido
# Utilizando a função 'filedialog.askdirectory()' para o usuario poder escolher o diretorio do download
# Condição caso não seja inserido nenhum link 
def download(link_):
    if link_:
        try:
            pasta = filedialog.askdirectory()
            YouTube(link_).streams.get_highest_resolution().download(pasta)
            aviso()
        except RegexMatchError:
            aviso_erro()
    else:
        aviso_erro()

# Função para informar que o download foi concluido
def aviso():
    janela.msg = Toplevel()
    janela.msg.title('Aviso')
    janela.msg.geometry('400x200')

    Label(janela.msg, text= 'Seu download foi concluido com sucesso', font='Arial 12', pady=30).pack()
    Button(janela.msg, text='Ok', command=janela.msg.destroy).pack()

# Função para informar que não foi adicionado nenhum link para o download
def aviso_erro():
    janela.msg = Toplevel()
    janela.msg.title('Aviso')
    janela.msg.geometry('400x200')

    Label(janela.msg, text= 'Insira um link valido para executar o download', font='Arial 12', pady=50).pack()
    Button(janela.msg, text='Ok', command=janela.msg.destroy).pack()

# Configurações da Janela de interação do usúario
quadro = Frame(janela)
quadro.pack()
Label(quadro, text = 'Insira o link do seu vídeo para realizar o download:', font= 'Arial 12').pack(side='left')
link = Entry(quadro, font='Arial 15', width=50)
link.pack(side='left')

# Criando um botão para efetuar o download 
Button(quadro, bg='red', text='>>>', bd=1, fg='white', width=4, height=2, command=lambda: download(link.get())).pack()

janela.mainloop()


# Versão simplificada do programa

#from pytube import YouTube
#YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
