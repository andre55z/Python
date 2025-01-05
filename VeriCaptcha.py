import tkinter as tk
import PIL
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageTk
import random
import string

class Tela ():
    #Criando a tela, botões e textboxes
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.title("Verificando Captcha")
        self.tela.configure(bg="light gray")

        self.txt = ""

        
        self.tela.geometry("420x300")
        self.bt = tk.Button(self.tela, text="Gerar outro captcha", bg="blue", command=self.GerandoCap).place(x=140, y=185)

        self.img_label = tk.Label(self.tela, bg="light gray")
        self.img_label.place(x=100, y=80)

        self.txtver = tk.Text(self.tela, height=1, width=22)
        self.txtver.place(x=107, y=220)

        self.result_label = tk.Label(self.tela, bg="light gray", font=("Arial", 8))
        self.result_label.place(x=107, y=245)

        self.btver = tk.Button(self.tela, text="ok", width=3, height=1, bg="purple", command=self.Verificando).place(x=295, y=220)

        self.GerandoCap()
        self.tela.mainloop()
    #Função que gera o Captcha
    def GerandoCap(self, tam=6):
            #Forma o grupo de caracteres do Captcha
            carac = string.ascii_letters + string.digits
            #Forma o Captcha
            self.txt = ''.join(random.choices(carac, k=tam))

            #Define o tamanho do Captcha
            large = 200
            height = 100
            img = Image.new('RGB', (large, height), (250, 250, 250))
            draw = ImageDraw.Draw(img)
            #Desenha a borda
            bdcolor = (128, 0, 128)
            bdth = 5
            draw.rectangle([0, 0, large-1, height-1], outline = bdcolor, width=bdth)

            font = ImageFont.truetype("arial.ttf", 40)

            #Distorce o Captcha
            for i, char in enumerate(self.txt):
                x = 20 + i * 30
                y = random.randint(20, 40)
                draw.text((x,y), char, font=font,fill=(random.randint(0, 150), random.randint(0, 150), random.randint(0, 150)))

            img = img.filter(ImageFilter.GaussianBlur(1))
            self.ExbImg(img)
    #Printa a imagem do Captcha na tela
    def ExbImg(self, img):
        imgtk = ImageTk.PhotoImage(img)
        self.img_label.config(image=imgtk)
        self.img_label.image = imgtk
    #Verifica se o Captcha esta certo
    def Verificando (self):
         resp  = self.txtver.get("1.0", "end-1c")
         if resp==self.txt:
               self.result_label.config(text="Captcha correto!", fg="green")
         else:
               self.result_label.config(text="Captcha incorreto!", fg="red")

#Carregando a tela
if __name__ == "__main__":
     tela = Tela()

