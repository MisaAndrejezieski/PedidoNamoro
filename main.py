import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('ACEITAS?')
root.geometry('600x600')
root.configure(background="#3a10ad")

def move_button_1(e):
    if button_1 is not None and abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo(
        "Meu amor", "Eu te amo meu amor, lanchinho mais tarde?"
    )

def denied():
    global button_1, button_2
    if button_1 is not None:
        button_1.destroy()
        button_1 = None
        messagebox.showinfo(
            "Sem graça!!!", "Você clicou no Não. Que pena!"
        )
        root.after(1000, simple_explosion)

def simple_explosion():
    # Limpar tela
    for widget in root.winfo_children():
        widget.destroy()
    
    # Criar efeito de explosão com cores e texto
    colors = ['red', 'orange', 'yellow', 'white']
    
    def show_explosion(frame=0):
        if frame < len(colors):
            root.configure(background=colors[frame])
            
            # Texto da explosão
            text = "💥 " + "BOOM!" * (frame + 1) + " 💥"
            label = Label(root, text=text, font=('Arial', 24, 'bold'), 
                         bg=colors[frame], fg='black')
            label.place(relx=0.5, rely=0.5, anchor=CENTER)
            
            root.after(200, show_explosion, frame + 1)
        else:
            # Fechar programa
            root.after(500, root.destroy)
    
    show_explosion()

margin = Canvas(root, width=500, bg="#3a10ad", height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#3a10ad', text='Quer namorar comigo?', fg='#500d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied, relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE, bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.pack()


root.bind('<Motion>', move_button_1)

root.mainloop()
