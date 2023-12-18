from tkinter import *
from tkinter import ttk

root = Tk()

class Application():
    def __init__(self):
        self.root = root 
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
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
    def widgets_frame1(self):
        ### Criação do botão limpar
        self.bt_limpar = Button(self.frame_1,text = "Limpar", bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold"))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão buscar
        self.bt_limpar = Button(self.frame_1,text = "Buscar",bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold"))
        self.bt_limpar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão lnovo
        self.bt_limpar = Button(self.frame_1,text = "Novo", bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold"))
        self.bt_limpar.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão alterar
        self.bt_limpar = Button(self.frame_1,text = "Alterar", bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold"))
        self.bt_limpar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão apagar
        self.bt_limpar = Button(self.frame_1,text = "Apagar", bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold") )
        self.bt_limpar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

        ## Crianção da label e entrada do código
        self.lb_codigo = Label(self.frame_1, text = "Código", bg = "#dfe3ee", font=("Verdana", 9, "bold"))
        self.lb_codigo.place(relx = 0.05, rely = 0.05)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx = 0.05, rely = 0.15, relwidth = 0.08)

        ## Criação da label e entrada do nome
        self.lb_nome = Label(self.frame_1, text = "Nome", bg = "#dfe3ee", font=("Verdana", 9, "bold"))
        self.lb_nome.place(relx = 0.05, rely = 0.35)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx = 0.05, rely=0.45, relwidth=0.8)

        ## Criação da label e entrada do telefone
        self.lb_nome = Label(self.frame_1, text = 'Telefone', bg = "#dfe3ee", font=("Verdana", 9, "bold"))
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Criação da label e entrada da cidade

        self.lb_nome = Label(self.frame_1, text = "Cidade", bg = "#dfe3ee", font=("Verdana", 9, "bold"))
        self.lb_nome.place(relx=0.5, rely = 0.6)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.5, rely = 0.7, relwidth = 0.4)
    
    def lista_frame2(self):
        self.ListaCli = ttk.Treeview(self.frame_2, height = 3, column=('col1','col2','col3','col4'))
        self.ListaCli.heading("#0", text = '')
        self.ListaCli.heading('#1', text = 'Codigo')
        self.ListaCli.heading('#2', text = 'Nome')
        self.ListaCli.heading('#3', text = 'Telefone')
        self.ListaCli.heading('#4', text = 'Cidade')

        self.ListaCli.column('#0', width = 1)
        self.ListaCli.column('#1', width = 50)
        self.ListaCli.column('#2', width = 200)
        self.ListaCli.column('#3', width = 125)
        self.ListaCli.column('#4', width = 125)

        self.ListaCli.place(relx = 0.01, rely = 0.1, relwidth = 0.95, relheight=0.85)

        self.scroolLista = Scrollbar(self.frame_2, orient = 'vertical')
        self.ListaCli.configure(yscroll = self.scroolLista.set)
        self.scroolLista.place(relx=0.95, rely=0.1, relwidth=0.04, relheight=0.85)

Application()