import tweepy
import schedule
import time
import tkinter as tk
from tkinter import messagebox
import threading


class Tela:
    def __init__(self):
        self.tela = tk.Tk()
        self.tela.configure(bg="gray")
        self.tela.resizable(False, False)
        self.tela.geometry("600x300")
        self.tela.title("Tweet Automático")

        # Componentes da interface
        self.lbl = tk.Label(self.tela, text="Escreva o tweet que deseja automatizar", 
                            height=2, width=50, font=("Times New Roman", 12), bg="gray")
        self.lbl.place(x=90, y=5)

        self.txt = tk.Text(self.tela, height=10, width=50)
        self.txt.place(x=105, y=50)

        self.lb = tk.Label(self.tela, text="Digite o horário para postar:", 
                           height=1, width=35, font=("Times New Roman", 8), bg="gray")
        self.lb.place(x=290, y=217)

        self.t = tk.Entry(self.tela, width=8)
        self.t.place(x=465, y=217)

        self.bt = tk.Button(self.tela, text="Pronto", height=1, width=10, bg='red', command=(self.tweet, messagebox.showinfo("Atenção!", "Não feche o app até o tweet ser feito.")))
        self.bt.place(x=105, y=217)

        self.tela.mainloop()

    def tweet(self):
        tweet_text = self.txt.get("1.0", tk.END).strip()
        tweet_time = self.t.get().strip()

        def send_tweet():
            try:
                api = tweepy.Client(
                    consumer_key='API KEY',
                    consumer_secret='API SECRET',
                    access_token= 'ACCESS TOKEN',
                    access_token_secret= 'ACCESS T S'
                )
                api.create_tweet(text=tweet_text)
                print(f"Tweet enviado: {tweet_text}")
            except Exception as e:
                print(f"Erro ao enviar o tweet: {e}")

        def schedule_tweet():
            schedule.every().day.at(tweet_time).do(send_tweet)
            while True:
                schedule.run_pending()
                time.sleep(60)

        threading.Thread(target=schedule_tweet, daemon=True).start()


if __name__ == "__main__":
    Tela()
