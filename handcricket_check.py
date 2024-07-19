import random
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image

def load_symbol_images():
    global Symbol
    names = ["handcricket1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
    for i in names:
        im = Image.open(i)
        im = im.resize((200, 200))
        im = ImageTk.PhotoImage(im)
        Symbol.append(im)

def show_image(player_choice, x, y):
    img = Image.open(f"{player_choice}.png")  # Assuming image filenames are "1.png", "2.png", ..., "6.png"
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    lab = tk.Label(root, image=img, height=200, width=200, borderwidth=0)
    lab.image = img
    lab.place(x=x, y=y)

def update_player_choice(choice):
    global player_score, computer_choice
    show_image(choice, 300, 300)
    if computer_choice == choice:
        out_label.config(text="COMPUTER IS OUT")
        check_winner()
    else:
        player_score += choice
    update_score()

def update_computer_choice(choice):
    global computer_score
    show_image(choice, 1000, 300)
    computer_score += choice
    update_score()

def computer_batting():
    global out_label, computer_score, computer_choice
    out_label.config(text="Computer is batting...")
    for _ in range(6):
        computer_choice = random.randint(1, 6)
        update_computer_choice(computer_choice)
        if computer_choice == player_choice:
            out_label.config(text="COMPUTER IS OUT")
            break
    check_winner()

def player_batting():
    global player_choice, computer_choice
    out_label.config(text="Your turn to bat!")
    computer_choice = random.randint(1, 6)
    enable_buttons()

def toss():
    global player_choice, computer_choice
    out_label.config(text="Tossing...")
    toss_result = random.choice(["bat", "bowl"])
    if toss_result == "bat":
        out_label.config(text="You won the toss! Choose to bat.")
        player_choice = "bat"
        computer_choice = "bowl"
        player_batting()
    else:
        out_label.config(text="Computer won the toss and chose to bat.")
        player_choice = "bowl"
        computer_choice = "bat"
        computer_batting()

def update_score():
    global score_label
    score_label.config(text=f"YOUR SCORE: {player_score} | COMPUTER: {computer_score}")

def check_winner():
    global player_score, computer_score, out_label
    if player_score > computer_score:
        out_label.config(text="You win!")
    elif player_score < computer_score:
        out_label.config(text="Computer wins!")
    else:
        out_label.config(text="It's a tie!")
    disable_buttons()

def reset_game():
    global player_score, computer_score, player_choice, computer_choice
    player_score = 0
    computer_score = 0
    player_choice = 0
    computer_choice = 0
    out_label.config(text="")
    score_label.config(text="YOUR SCORE: 0 | COMPUTER: 0")
    disable_buttons()

def enable_buttons():
    b1.config(state=tk.NORMAL)
    b2.config(state=tk.NORMAL)
    b3.config(state=tk.NORMAL)
    b4.config(state=tk.NORMAL)
    b5.config(state=tk.NORMAL)
    b6.config(state=tk.NORMAL)

def disable_buttons():
    b1.config(state=tk.DISABLED)
    b2.config(state=tk.DISABLED)
    b3.config(state=tk.DISABLED)
    b4.config(state=tk.DISABLED)
    b5.config(state=tk.DISABLED)
    b6.config(state=tk.DISABLED)

Symbol = []
player_score = 0
computer_score = 0
player_choice = 0
computer_choice = 0

root = tk.Tk()
root.geometry("1200x800")
root.title("Hand Cricket")

# Board
f1 = tk.Frame(root, width=2000, height=1200, relief='raised')
f1.place(x=-280, y=-240)
img = ImageTk.PhotoImage(Image.open("cricket stadium background.jpg"))
Lab = tk.Label(f1, image=img)
Lab.place(x=0, y=0)

# Load symbol images
load_symbol_images()

# Create buttons
im1 = Image.open("handcricket1.png")
im1 = im1.resize((80, 65))
im1 = ImageTk.PhotoImage(im1)
b1 = tk.Button(root, image=im1, height=90, width=80, command=lambda: update_player_choice(1))
b1.place(x=50, y=50)
b1.config(state=tk.DISABLED)

im2 = Image.open("2.png")
im2 = im2.resize((80, 65))
im2 = ImageTk.PhotoImage(im2)
b2 = tk.Button(root, image=im2, height=90, width=80,command=lambda: update_player_choice(2))
b2.place(x=200, y=50)
b2.config(state=tk.DISABLED)

im3 = Image.open("3.png")
im3 = im3.resize((80, 65))
im3 = ImageTk.PhotoImage(im3)
b3 = tk.Button(root, image=im3, height=90, width=80,command=lambda: update_player_choice(3))
b3.place(x=350, y=50)
b3.config(state=tk.DISABLED)

im4 = Image.open("4.png")
im4 = im4.resize((80, 65))
im4 = ImageTk.PhotoImage(im4)
b4 = tk.Button(root, image=im4, height=90, width=80,command=lambda: update_player_choice(4))
b4.place(x=500, y=50)
b4.config(state=tk.DISABLED)

im5 = Image.open("5.png")
im5 = im5.resize((80, 65))
im5 = ImageTk.PhotoImage(im5)
b5 = tk.Button(root, image=im5, height=90, width=80,command=lambda: update_player_choice(5))
b5.place(x=650, y=50)
b5.config(state=tk.DISABLED)

im6 = Image.open("6.png")
im6 = im6.resize((80, 65))
im6 = ImageTk.PhotoImage(im6)
b6 = tk.Button(root, image=im6, height=90, width=80,command=lambda: update_player_choice(6))
b6.place(x=800, y=50)
b6.config(state=tk.DISABLED)

score_label = tk.Label(root, text="YOUR SCORE: 0 | COMPUTER: 0", font=("Arial", 16),
                       bg="black", fg="white", padx=10, pady=5, relief=tk.RAISED)
score_label.place(x=900, y=50, height=40)

out_label = tk.Label(root, text="", font=("Arial", 18),
                     bg="white", fg="red", padx=10, pady=5)
out_label.place(x=900, y=100, height=40)

toss_button = tk.Button(root, text="Toss", font=("Arial", 16), command=toss)
toss_button.place(x=900, y=160, height=40)

reset_button = tk.Button(root, text="Reset", font=("Arial", 16), command=reset_game)
reset_button.place(x=900, y=210, height=40)

root.mainloop()
