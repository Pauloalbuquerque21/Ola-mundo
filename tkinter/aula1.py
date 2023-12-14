from tkinter import *

root = Tk()

class Application():
    def __init__(self):
        self.root = root 
        self.tela()
        self.frames_da_tela()
        self.criando_botoes()
        root.mainloop()
    def tela(self):
        self.root.title("Cadatri de Clientes")
        self.root.configure(bg='#1E90FF')
        self.root.geometry("788x588")   
        self.root.resizable(True, True)
        self.root.maxsize(width=988,height = 788)
        self.root.minsize(width=488,height=388)
    def frames_da_tela(self):
        self.frame_1 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fab',highlightthickness='2')
        self.frame_1.place(relx = 0.02, rely = 0.02, relwidth = 0.96, relheight = 0.46)

        self.frame_2 = Frame(self.root, bd = 4, bg='#dfe3ee', highlightbackground='#759fab',highlightthickness='2')
        self.frame_2.place(relx = 0.02, rely = 0.5, relwidth = 0.96, relheight = 0.46)
    def criando_botoes(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame_1,text = "Limpar")
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão buscar
        self.bt_limpar = Button(self.frame_1,text = "Buscar")
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão lnovo
        self.bt_limpar = Button(self.frame_1,text = "Novo")
        self.bt_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão alterar
        self.bt_limpar = Button(self.frame_1,text = "Alterar")
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão apagar
        self.bt_limpar = Button(self.frame_1,text = "Apagar")
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
Application()