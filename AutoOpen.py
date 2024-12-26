import pyautogui as auto
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Tela:
    def __init__(self):

        self.jan = tk.Tk()
        self.jan.geometry("500x120")
        self.jan.configure(bg="gray")
        self.jan.title("Abrir arquivo")

        self.lbl = tk.Label(self.jan, text="Escreva o nome do arquivo", height=1, width=20, font=("Times New Roman", 10), bg="gray")
        self.lbl.place(x=172, y=20)

        self.txtbox = tk.Text(self.jan, height=1, width=20, font=("Arial", 13))
        self.txtbox.place(x=156.6, y=50)

        self.bt = tk.Button(self.jan, text="Abrir", height=1, width=10, bg="red", command= self.open)
        self.bt.place(x=207, y=80)

        list =[" ", ".xlsx", ".docx", ".pptx", ".png", ".jpg"]
        self.cbox = ttk.Combobox(self.jan, values=list, width= 7, height=1 )
        self.cbox.place(x= 350, y=50)
        self.jan.mainloop()
    def open(self):
        text = self.txtbox.get("1.0", tk.END).strip()
        ext = self.cbox.get().strip()
        if text:
            auto.PAUSE = 2
            auto.press('win')
            auto.write(text)
            auto.write(ext)
            auto.press('enter')
        else:
            messagebox.showwarning("Atenção!", "Insira o arquivo corretamente.")
    


class criando:
    def __init__(self):
        pass
    tela = Tela()



