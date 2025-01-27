import os
import pyqrcode
import png
from pyqrcode import QRCode
import tkinter as tk
from tkinter import messagebox

class Tela:

    def __init__(self):
        self.tela = tk.Tk()
        self.tela.geometry("437x237")
        self.tela.configure(bg="light blue")
        self.tela.title("Gerador de QRcodes")

        self.lbl = tk.Label(self.tela, text="Insira a URL", width=40, height=1, bg="light blue", font=("Helvetica", 14) )
        self.lbl.place(x=2, y=25)
        self.txt = tk.Text(self.tela, width=40, height=1)
        self.txt.place(x=60, y=70)
        def criarQR():
            url = self.txt.get("1.0", tk.END).strip()
            if url:
                
                qr = pyqrcode.create(url)
                downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
                way = os.path.join(downloads_path, "qrcode.png")
                qr.png(way, scale=8)
                messagebox.showinfo("Sucesso", f"QR Code salvo em {way}")
            else:
                messagebox.showerror("Erro!", "Insira uma url válida.")
        self.btn = tk.Button(self.tela, text="Criar!", width=15, height=2, bg="red", command=criarQR).place(x=160, y=100)

        self.tela.mainloop()

if __name__ == "__main__":
    Tela()