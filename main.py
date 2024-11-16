import tkinter as tk
from tkinter import messagebox
import random
import pygame

class LoveProposalApp:
    def __init__(self, root):
        self.root = root
        self.root.title('ACEITAS?')
        self.root.geometry('600x600')
        self.root.configure(background='#affc8d')

        self.init_pygame()
        self.create_widgets()
        self.bind_events()

        self.button_no = None
        self.button_yes = None

    def init_pygame(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        
        # Tente carregar a imagem da explosão
        try:
            self.explosion_image = pygame.image.load('explosion.png')  # Verifique se a imagem está no diretório
        except pygame.error as e:
            messagebox.showerror("Erro", f"Não foi possível carregar a imagem: {e}")
            self.root.quit()

    def create_widgets(self):
        margin = tk.Canvas(self.root, width=500, bg='#affc8d', height=100, bd=0, highlightthickness=0, relief='ridge')
        margin.pack()

        label = tk.Label(self.root, bg='#affc8d', text='Quer namorar comigo?', fg='#500d22', font=('Montserrat', 24, 'bold'))
        label.pack()

        self.button_no = tk.Button(self.root, text='Não', bg='#ffb3c1', command=self.denied, relief=tk.RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
        self.button_no.pack()

        self.button_yes = tk.Button(self.root, text='Sim', bg='#ffb3c1', command=self.accepted, relief=tk.RIDGE, bd=3, font=('Montserrat', 14, 'bold'))
        self.button_yes.pack()

    def bind_events(self):
        self.root.bind('<Motion>', self.move_button_no)

    def move_button_no(self, event):
        if self.button_no is not None and abs(event.x - self.button_no.winfo_x()) < 50 and abs(event.y - self.button_no.winfo_y()) < 40:
            x = random.randint(0, self.root.winfo_width() - self.button_no.winfo_width())
            y = random.randint(0, self.root.winfo_height() - self.button_no.winfo_height())
            self.button_no.place(x=x, y=y)

    def accepted(self):
        messagebox.showinfo("Meu amor", "Eu te amo meu amor, lanchinho mais tarde?")

    def denied(self):
        if self.button_no is not None:
            self.button_no.destroy()
            self.button_no = None
            messagebox.showinfo("Sem graça!!!", "Você clicou no Não. Que pena!")
            self.explode_button(self.button_yes)

    def explode_button(self, button):
        if button:
            x, y = button.winfo_x(), button.winfo_y()
            button.destroy()
            self.create_explosion(x, y)

    def create_explosion(self, x, y):
        for i in range(20):
            self.screen.fill((175, 200, 141))  # Cor de fundo
            self.screen.blit(self.explosion_image, (x - self.explosion_image.get_width() // 2, y - self.explosion_image.get_height() // 2))
            pygame.display.flip()
            self.clock.tick(30)

            # Loop de eventos para o Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.root.quit()

        pygame.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoveProposalApp(root)
    root.mainloop()
    