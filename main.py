import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title('ACEITAS?')
root.geometry('600x600')
root.configure(background='#affc8d')

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
        explode_button(button_2)

def explode_button(button):
    if button:
        for i in range(10, 0, -1):
            button.config(width=i, height=i, bg='red')
            root.update()
            root.after(50)
        for i in range(10):
            button.config(bg='yellow' if i % 2 == 0 else 'red')
            root.update()
            root.after(100)
        button.place_forget()
        create_explosion(button.winfo_x(), button.winfo_y())

def create_explosion(x, y):
    explosion = Canvas(root, width=100, height=100, bg='gray', bd=0, highlightthickness=0, relief='ridge')
    explosion.place(x=x, y=y)
    for i in range(10):
        explosion.config(bg='darkgray' if i % 2 == 0 else 'black')
        root.update()
        root.after(100)
    explosion.destroy()

margin = Canvas(root, width=500, bg='#affc8d', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg='#affc8d', text='Quer namorar comigo?', fg='#500d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text='Não', bg='#ffb3c1', command=denied, relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
button_2 = tk.Button(root, text='Sim', bg='#ffb3c1', relief=RIDGE, bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.pack()

# Vincular o evento após colocar o botão no lugar
root.bind('<Motion>', move_button_1)

root.mainloop()
