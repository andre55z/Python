import csv
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import mysql.connector
from Basededados import Database
from tkinter import filedialog
         
class Cadastro:
    def __init__(self):
        bgc = "light gray"
        self.telacada = tk.Tk()
        self.telacada.geometry("350x300")
        self.telacada.configure(bg=bgc)
        self.telacada.title("Cadastro de Contato")

        tk.Label(self.telacada, text="Nome", font=("Helvetica", 12), bg=bgc).place(x=1, y=50)
        tk.Label(self.telacada, text="Número de telefone", font=("Helvetica", 12), bg=bgc).place(x=1, y=90)
        tk.Label(self.telacada, text="Instagram", font=("Helvetica", 12), bg=bgc).place(x=1, y=130)
        tk.Label(self.telacada, text="E-mail", font=("Helvetica", 12), bg=bgc).place(x=1, y=170)

        self.txtnome = tk.Entry(self.telacada, width=25)
        self.txtnome.place(x=1, y=70)
        
        self.txtnum = tk.Entry(self.telacada, width=20)
        self.txtnum.place(x=1, y=110)
        
        self.txtinsta = tk.Entry(self.telacada, width=20)
        self.txtinsta.place(x=1, y=150)
        
        self.txtemail = tk.Entry(self.telacada, width=25)
        self.txtemail.place(x=1, y=190)
        
 
        self.btn_foto = tk.Button(self.telacada, text="Selecionar Foto", command=self.selecionar_foto)
        self.btn_foto.place(x=1, y=220)

        self.foto_path = None  

        tk.Button(self.telacada, text="Salvar", width=15, height=3, bg="orange", command=self.Save).place(x=210, y=230)

        self.telacada.mainloop()

    def selecionar_foto(self):
 
        self.foto_path = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg;*.bmp")])
        if self.foto_path:
            messagebox.showinfo("Foto Selecionada", "Foto selecionada com sucesso!")

    def Save(self):
        nome = self.txtnome.get().strip()
        num = self.txtnum.get().strip()
        insta = self.txtinsta.get().strip()
        email = self.txtemail.get().strip()

        if not nome.isalpha():
            messagebox.showerror("Nome inválido", "Insira um nome válido")
            return
        
        if not num.isdigit() or len(num) != 11:
            messagebox.showerror("Telefone inválido", "Insira um telefone válido")
            return
        
 
        foto = self.foto_path if self.foto_path else None

        db = Database()
        conn = db.Connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO contatos (nome, telefone, instagram, email, foto) VALUES (%s, %s, %s, %s, %s)",
                               (nome, num, insta, email, foto))
                conn.commit()
                conn.close()
                messagebox.showinfo("Sucesso", "Contato cadastrado com sucesso!")
                self.txtnome.delete(0, tk.END)
                self.txtnum.delete(0, tk.END)
                self.txtinsta.delete(0, tk.END)
                self.txtemail.delete(0, tk.END)
                self.foto_path = None
            except mysql.connector.Error as err:
                messagebox.showerror("Erro no Banco de Dados", str(err))
class ProcuraContato:
    def __init__(self):
        bgc = "gray"
        self.telaproc = tk.Toplevel()
        self.telaproc.geometry("350x470")
        self.telaproc.configure(bg=bgc)
        self.telaproc.title("Procurar Contato")

        tk.Label(self.telaproc, text="Insira o nome do contato procurado", font=("Helvetica", 12), bg=bgc).place(x=50, y=50)
        self.txtnome = tk.Entry(self.telaproc, width=15)
        self.txtnome.place(x=110, y=80)
        tk.Button(self.telaproc, text="Ok", bg="red", width=3, height=1, command=self.BuscaContato).place(x=200, y=80)

        self.resultado_label = tk.Label(self.telaproc, text="", width=30, height=10, font=("Helvetica", 10), bg="orange", fg="black", justify="left", bd=2, relief="solid")
        self.resultado_label.place(x=50, y=120)

        self.imginicio = Image.open("Contatos/imgsctt/download.jpg")
        self.tamanho = (150, 150)
        self.imginicio = self.imginicio.resize(self.tamanho)
        self.imginicio = ImageTk.PhotoImage(self.imginicio)
        self.lblimg = tk.Label(self.telaproc, image=self.imginicio)
        self.lblimg.place(x=100, y=290) 



    def BuscaContato(self):
        nome = self.txtnome.get().strip()
        if not nome.isalpha():
                messagebox.showerror("Nome inválido", "Insira um nome válido")
                return

        db = Database()
        conn = db.Connect()
        if conn:
                try:
                        cursor = conn.cursor()
                        cursor.execute("SELECT * FROM contatos WHERE nome = %s", (nome,))
                        contato = cursor.fetchone()
                        conn.close()

                        if contato:
                            id, nome, telefone, instagram, email, foto = contato
                            resultado = f"ID: {id}\nNome: {nome}\nTelefone: {telefone}\nInstagram: {instagram}\nE-mail: {email}"
                            self.resultado_label.config(text=resultado)

                            
                            img = Image.open(foto)  
                            self.imgtk = ImageTk.PhotoImage(img)

                            
                            way = foto
                            img = Image.open(way)
                            tamanho = (150, 150)
                            novaimg = img.resize(tamanho)
                            self.novaimgtk = ImageTk.PhotoImage(novaimg)

                            if hasattr(self, 'lblimg'):
                                                        self.lblimg.destroy()

                            self.lblimg = tk.Label(self.telaproc, image=self.novaimgtk)
                            self.lblimg.place(x=100, y=290) 

                        else:
                                messagebox.showinfo("Contato não encontrado", "Nenhum contato encontrado com esse nome.")

                except mysql.connector.Error as err:
                        messagebox.showerror("Erro no banco de dados", str(err))


class ListaContatos:
    def __init__(self):
        bgc = "light gray"
        self.telalista = tk.Tk()
        self.telalista.geometry("400x350")
        self.telalista.configure(bg=bgc)
        self.telalista.title("Lista de Contatos")

        self.lbltitulo = tk.Label(self.telalista, text="Seus Contatos", font=("Helvetica", 14, "bold"), bg=bgc)
        self.lbltitulo.pack(pady=10)


        self.btn_atualizar = tk.Button(self.telalista, text="Atualizar Lista", bg="orange", command=self.carregar_contatos)
        self.btn_atualizar.pack(pady=5)

        self.listbox_contatos = tk.Listbox(self.telalista, width=50, height=10)
        self.listbox_contatos.pack(pady=10)

        self.btnexport = tk.Button(self.telalista, text="Exportar Contatos", bg="orange", command=self.exportarcontatos)
        self.btnexport.pack(pady=17)
        self.carregar_contatos()
        self.telalista.mainloop()
    def carregar_contatos(self):
        self.listbox_contatos.delete(0, tk.END)

        db = Database()
        conn = db.Connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("SELECT nome, telefone, instagram, email, foto FROM contatos")
                contatos = cursor.fetchall()
                conn.close()


                if contatos:
                    for contato in contatos:
                        nome, telefone, instagram, email, foto = contato
                        contato_info = f"{nome} | {telefone} | {instagram} | {email}"
                        self.listbox_contatos.insert(tk.END, contato_info)
            except Exception as e:
                messagebox.showerror("Erro", str(e))

    def exportarcontatos(self):
             db = Database()
             conn = db.Connect()
             if conn:
                  try:
                        cursor = conn.cursor()
                        cursor.execute("SELECT nome, telefone, instagram, email FROM contatos")
                        contatos = cursor.fetchall()
                        conn.close

                        if not contatos:
                             messagebox.showinfo("Sem contatos", "Nenhum contato listado.")
                             return

                        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                     filetypes=[("Arquivo CSV", "*.csv"),
                                                                ("Arquivo de Texto", "*.txt")])
                        if not file_path:
                            return

                        with open(file_path, mode="w", newline="") as file:
                            writer = csv.writer(file)
                            writer.writerow(["Nome", "Telefone", "Instagram", "E-mail"])
                            writer.writerows(contatos)

                        messagebox.showinfo("Sucesso", f"Contatos exportados para {file_path}")
                  except Exception as e:
                    messagebox.showerror("Erro", str(e))



                     

            

class DeletaContato:
    def __init__(self):
        bgc = "light gray"
        self.teladel = tk.Tk()
        self.teladel.geometry("350x300")
        self.teladel.configure(bg=bgc)
        self.teladel.title("Deletar contato")

        self.lblnome = tk.Label(self.teladel, text="Insira o nome do contato a ser deletado", font=("Helvetica", 12), bg=bgc)
        self.lblnome.place(x=50, y=50)
        
        self.txtnome = tk.Entry(self.teladel, width=15)
        self.txtnome.place(x=110, y=80)
        
        self.btndel = tk.Button(self.teladel, text="Ok", bg="red", width=3, height=1, command=self.DeletaContato)
        self.btndel.place(x=240, y=80)
    
    def DeletaContato(self):
        nome = self.txtnome.get().strip()
        if not nome.isalpha():
            messagebox.showerror("Nome inválido", "Insira um nome válido")
            return
        
        db = Database()
        conn = db.Connect()
        if conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contatos WHERE nome = %s", (nome,))
            conn.commit()
            conn.close()
            messagebox.showinfo("Sucesso!", f"{nome} deletado com sucesso!")
            self.teladel.destroy()

class Tela:
    def __init__(self):
        bgc="light gray"
        self.tela = tk.Tk()
        self.tela.configure(bg=bgc)
        self.tela.geometry("600x500")
        self.tela.title("Contatos")

        self.img= Image.open("Contatos/imgsctt/imgct.png")
        self.imgtk = ImageTk.PhotoImage(self.img)

        self.lblimg = tk.Label(self.tela, image=self.imgtk, bg=bgc)
        self.lblimg.place(x=110, y=50)

        bgbt = "orange"
        self.btnlist = tk.Button(self.tela, text="Lista de contatos", bg=bgbt, width=20, height=4, command=self.exibeLista )
        self.btnlist.place(x=227, y=150)

        self.btncada = tk.Button(self.tela, text="Cadastrar contatos", bg=bgbt, width=20, height=4, command=self.abrirCadastro )
        self.btncada.place(x=227, y=230)

        self.btnproc = tk.Button(self.tela, text="Procurar contato", bg=bgbt, width=20, height=4, command=self.procuraContato )
        self.btnproc.place(x=227, y=310)

        self.btnremove = tk.Button(self.tela, text="Remover contato", bg=bgbt, width=20, height=4, command=self.deletaContato )
        self.btnremove.place(x=227, y=390)

        db = Database()
        db.CriandoBanco()
        self.tela.mainloop()

    def abrirCadastro(self):
        Cadastro()

    def procuraContato(self):
        ProcuraContato()

    def exibeLista(self):
        ListaContatos()
    
    def deletaContato(self):
        DeletaContato()

Tela()
