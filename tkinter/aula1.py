from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()

class funções():
    def limpa_tela(self):
        self.codigo_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.fone_entry.delete(0,END)
        self.cidade_entry.delete(0,END)
    def conecta_bd(self):
        self.conn = sqlite3.connect('Cliente.bd')
        self.cursor = self.conn.cursor()
    def desconecta_bd(self):
        self.conn.close()
    def montaTabelas(self):

        self.conecta_bd(); print('Conectando ao banco de dados')
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
                cod INTERGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTERGER(20),
                cidade CHAR(40)                
            );
        """)
        self.conn.commit();print('Banco de dados criado')
        self.desconecta_bd()
    def add_cliente(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.fone = self.fone_entry.get()
        self.cidade = self.cidade_entry.get()
        self.conecta_bd()

        self.cursor.execute("""INSERT INTO clientes (nome_cliente, telefone, cidade)
            Values (?,?,?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_tela()
    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values = i)
        self.desconecta_bd()
        

class Application(funções):
    def __init__(self):
        self.root = root 
        self.tela()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
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
        self.bt_limpar = Button(self.frame_1,text = "Limpar", bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold"), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão buscar
        self.bt_buscar = Button(self.frame_1,text = "Buscar",bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold"))
        self.bt_buscar.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão novo
        self.bt_novo = Button(self.frame_1,text = "Novo", bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold"), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão alterar
        self.bt_alterar = Button(self.frame_1,text = "Alterar", bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold"))
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        ### Criação do botão apagar
        self.bt_apagar = Button(self.frame_1,text = "Apagar", bg = "#107db2", fg = 'white', font=("Verdana", 8, "bold") )
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

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
        self.lb_fone = Label(self.frame_1, text = 'Telefone', bg = "#dfe3ee", font=("Verdana", 9, "bold"))
        self.lb_fone.place(relx=0.05, rely=0.6)

        self.fone_entry = Entry(self.frame_1)
        self.fone_entry.place(relx=0.05, rely=0.7, relwidth=0.4)

        ## Criação da label e entrada da cidade

        self.lb_cidade = Label(self.frame_1, text = "Cidade", bg = "#dfe3ee", font=("Verdana", 9, "bold"))
        self.lb_cidade.place(relx=0.5, rely = 0.6)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely = 0.7, relwidth = 0.4)
    
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