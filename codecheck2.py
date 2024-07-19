import random
import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import ImageTk, Image

# Function to load symbol images
def load_symbol_images():
    global Symbol
    Symbol = []
    names = ["handcricket1.png", "2.png", "3.png", "4.png", "5.png", "6.png"]
    for name in names:
        img = Image.open(name)
        img = img.resize((80, 65))
        img = ImageTk.PhotoImage(img)
        Symbol.append(img)

# Function to update the score label
def update_score():
    global score_label, player_score, computer_score
    score_label.config(text=f"{input_name}: {player_score} | COMPUTER: {computer_score}")

# Function to handle player's choice and update game state
# Function to handle player's choice and update game state
def handle_player_choice(choice):
    global player_score, computer_score, out_label, b_buttons, is_player_batting

    # Display player's choice image
    player_choice_img = Symbol[choice - 1]
    player_choice_label.config(image=player_choice_img)
    player_choice_label.image = player_choice_img

    # Generate random choice for computer
    computer_choice = random.randint(1, 6)
    computer_choice_img = Symbol[computer_choice - 1]
    computer_choice_label.config(image=computer_choice_img)
    computer_choice_label.image = computer_choice_img

    # Determine outcome
    if choice == computer_choice:
        out_label.config(text="YOU ARE OUT!")
        disable_buttons()
    else:
        if is_player_batting:
            player_score += choice
        else:
            computer_score += computer_choice
        update_score()

    # Check if game should end (player and computer choose the same number)
    if choice == computer_choice:
        if is_player_batting:
            messagebox.showinfo("Game Over", "You and the computer chose the same number! Game Over.")
        else:
            messagebox.showinfo("Game Over", "You and the computer chose the same number! Game Over.")
        root.quit()  # Close the tkinter application

# Function to disable all choice buttons after player is out
def disable_buttons():
    for button in b_buttons:
        button.config(state=tk.DISABLED)

# Function to conduct toss and decide who bats first
def toss():
    global is_player_batting
    toss_result = random.choice(["HEADS", "TAILS"])
    if toss_result == "HEADS":
        is_player_batting = True
        messagebox.showinfo("Toss Result", f"{input_name} won the toss and will bat first!")
    else:
        is_player_batting = False
        messagebox.showinfo("Toss Result", "Computer won the toss and will bat first!")
    open_hand_cricket_window()

# Function to open the game window after the toss
def open_hand_cricket_window():
    global root, player_score, computer_score, out_label, score_label, player_choice_label, computer_choice_label

    root.withdraw()  # Hide the root window from the user

    # Create a new game window
    game_window = tk.Toplevel()
    game_window.geometry("1200x800")
    game_window.title("Hand Cricket")

    # Load symbol images
    load_symbol_images()

    # GUI elements setup
    f1 = tk.Frame(game_window, width=2000, height=1200, relief='raised')
    f1.place(x=-280, y=-240)
    img = ImageTk.PhotoImage(Image.open("cricket stadium background.jpg"))
    Lab = tk.Label(f1, image=img)
    Lab.place(x=0, y=0)

    b_buttons = []
    for i in range(6):
        img = Symbol[i]
        button = tk.Button(game_window, image=img, height=90, width=80, command=lambda i=i+1: handle_player_choice(i))
        button.place(x=50 + i * 150, y=50)
        b_buttons.append(button)

    player_choice_label = tk.Label(game_window, height=200, width=200, borderwidth=0)
    player_choice_label.place(x=300, y=300)

    computer_choice_label = tk.Label(game_window, height=200, width=200, borderwidth=0)
    computer_choice_label.place(x=1000, y=300)

    player_score = 0
    computer_score = 0

    score_label = tk.Label(game_window, text=f"{input_name}: {player_score} | COMPUTER: {computer_score}", font=("Arial", 16),
                           bg="black", fg="white", padx=10, pady=5, relief=tk.RAISED)
    score_label.place(x=1200, y=50, height=40)

    out_label = tk.Label(game_window, text="", font=("Arial", 18),
                         bg="white", fg="red", padx=10, pady=5)
    out_label.place(x=1200, y=100, height=40)

    game_window.mainloop()

# Initialize tkinter and ask for player's name
root = tk.Tk()
root.withdraw()  # Hide the root window initially

input_name = simpledialog.askstring("Input", "Enter your name:")

# Show the toss window
toss()

root.mainloop()  # Start the main tkinter event loop
