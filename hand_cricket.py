import random
from tkinter import*
import tkinter as tk
from PIL import ImageTk,Image
from tkinter import simpledialog

def load_symbol_images():
    global Symbol
    names = ["handcricket1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
    for i in names:
        im = Image.open(""+i)
        im = im.resize((200, 200))
        im = ImageTk.PhotoImage(im)
        Symbol.append(im)

input_name = simpledialog.askstring("Input", "Enter your name:")

def toss():
    global b1,im1

def show_image1():
    global im1,b1,Symbol,player_score
    img1 = Image.open("handcricket1.png")
    img1 = img1.resize((200, 200))
    img1 = ImageTk.PhotoImage(img1)
    Lab1 = tk.Label(root, image=img1,height=200,width=200,borderwidth=0)
    Lab1.image=img1
    Lab1.place(x=300, y=300)
    r = random.randint(1, 6)
    b7 = tk.Button(root, image=Symbol[r - 1], height=200, width=200,borderwidth=0,)
    b7.place(x=1000, y=300)
    if(r==1):
        out()
    else:
        player_choice = 1
        player_score += player_choice
        update_score()

def show_image2():
    global im2,b2,player_score
    img2 = Image.open("2.png")
    img2 = img2.resize((200, 200))
    img2 = ImageTk.PhotoImage(img2)
    Lab2 = tk.Label(root, image=img2,height=200,width=200,borderwidth=0)
    Lab2.image=img2
    Lab2.place(x=300, y=300)
    s = random.randint(1, 6)
    b8 = tk.Button(root, image=Symbol[s - 1], height=200, width=200, borderwidth=0, )
    b8.place(x=1000, y=300)
    if (s == 2):
        out()
    else:
        player_choice = 2
        player_score += player_choice
        update_score()

def show_image3():
    global im3,b3,player_score
    img3 = Image.open("3.png")
    img3 = img3.resize((200, 200))
    img3 = ImageTk.PhotoImage(img3)
    Lab3 = tk.Label(root, image=img3,height=200,width=200,borderwidth=0)
    Lab3.image=img3
    Lab3.place(x=300, y=300)
    t = random.randint(1, 6)
    b9 = tk.Button(root, image=Symbol[t - 1], height=200, width=200, borderwidth=0, )
    b9.place(x=1000, y=300)
    if (t == 3):
        out()
    else:
        player_choice = 3
        player_score += player_choice
        update_score()

def show_image4():
    global im4,b4,player_score
    img4 = Image.open("4.png")
    img4 = img4.resize((200, 200))
    img4 = ImageTk.PhotoImage(img4)
    Lab4 = tk.Label(root, image=img4,height=200,width=200,borderwidth=0)
    Lab4.image=img4
    Lab4.place(x=300, y=300)
    u = random.randint(1, 6)
    b10 = tk.Button(root, image=Symbol[u - 1], height=200, width=200, borderwidth=0 )
    b10.place(x=1000, y=300)
    if (u == 4):
        out()
    else:
        player_choice = 4
        player_score += player_choice
        update_score()

def show_image5():
    global im5,b5,player_score
    img5 = Image.open("5.png")
    img5 = img5.resize((200, 200))
    img5 = ImageTk.PhotoImage(img5)
    Lab5 = tk.Label(root, image=img5,height=200,width=200,borderwidth=0)
    Lab5.image=img5
    Lab5.place(x=300, y=300)
    v = random.randint(1, 6)
    b11 = tk.Button(root, image=Symbol[v - 1], height=200, width=200, borderwidth=0, )
    b11.place(x=1000, y=300)
    if (v == 5):
        out()
    else:
        player_choice = 5
        player_score += player_choice
        update_score()

def show_image6():
    global im6,b6,player_score
    img6 = Image.open("6.png")
    img6 = img6.resize((200, 200))
    img6 = ImageTk.PhotoImage(img6)
    Lab6 = tk.Label(root, image=img6,height=200,width=200,borderwidth=0)
    Lab6.image=img6
    Lab6.place(x=300, y=300)
    w = random.randint(1, 6)
    b12 = tk.Button(root, image=Symbol[w - 1], height=200, width=200, borderwidth=0, )
    b12.place(x=1000, y=300)
    if (w == 6):
        out()
    else:
        player_choice = 6
        player_score += player_choice
        update_score()

def update_score():
    global score_label
    score_label.config(text= f"{input_name} SCORE {player_score}" "|" "COMPUTER: 0")

def out():
    global out_label,b1,b2,b3,b4,b5,b6
    b1.config(state=tk.DISABLED)
    b2.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)
    b4.config(state=tk.DISABLED)
    b5.config(state=tk.DISABLED)
    b6.config(state=tk.DISABLED)
    out_label.config(text="YOU ARE OUT")

Symbol=[]
player_score = 0

root=tk.Tk()
root.geometry("1200x800")
root.title("Hand Cricket")
#Board
f1=tk.Frame(root,width=2000,height=1200,relief='raised')
f1.place(x=-280,y=-240)
img=ImageTk.PhotoImage(Image.open("cricket stadium background.jpg"))
Lab=tk.Label(f1,image=img)
Lab.place(x=0,y=0)

im1 = Image.open("handcricket1.png")
im1 = im1.resize((80, 65))
im1 = ImageTk.PhotoImage(im1)
b1 = tk.Button(root, image=im1, height=90, width=80,command=show_image1)
b1.place(x=50, y=50)

im2 = Image.open("2.png")
im2 = im2.resize((80, 65))
im2 = ImageTk.PhotoImage(im2)
b2 = tk.Button(root, image=im2, height=90, width=80,command=show_image2)
b2.place(x=200, y=50)

im3 = Image.open("3.png")
im3 = im3.resize((80, 65))
im3 = ImageTk.PhotoImage(im3)
b3 = tk.Button(root, image=im3, height=90, width=80,command=show_image3)
b3.place(x=350, y=50)

im4 = Image.open("4.png")
im4 = im4.resize((80, 65))
im4 = ImageTk.PhotoImage(im4)
b4 = tk.Button(root, image=im4, height=90, width=80,command=show_image4)
b4.place(x=500, y=50)

im5 = Image.open("5.png")
im5 = im5.resize((80, 65))
im5 = ImageTk.PhotoImage(im5)
b5 = tk.Button(root, image=im5, height=90, width=80,command=show_image5)
b5.place(x=650, y=50)

im6 = Image.open("6.png")
im6 = im6.resize((80, 65))
im6 = ImageTk.PhotoImage(im6)
b6 = tk.Button(root, image=im6, height=90, width=80,command=show_image6)
b6.place(x=800, y=50)

score_label = tk.Label(root, text=f"{input_name}: 0 | COMPUTER: 0", font=("Arial", 16),
                       bg="black", fg="white", padx=10, pady=5, relief=tk.RAISED)
score_label.place(x=1200,y=50,height=40)

out_label = tk.Label(root, text="", font=("Arial", 18),
                       bg="white", fg="red", padx=10, pady=5)
out_label.place(x=1200,y=100,height=40)

load_symbol_images()


root.mainloop()