import random
import tkinter as tk
from tkinter import messagebox

# 1. Core Logic Functions
#count = 0

def roll_dice():
    #global count
    count=0
    count += 1
    num = random.randint(1, 6)
    result_label.config(text=f"🎲 {num} 🎲")
    count_label.config(text=f"Total Rolls: {count}")

def exit_game():
    messagebox.showinfo("Thanks", "Thank you for playing!!!")
    root.destroy()

# 2. Setup Window (Auto-sizes to fit content)
root = tk.Tk()
root.title("Dice Game")
root.configure(bg="yellow")

# 3. Create and Pack Visual Elements
tk.Label(root, text="Dice Rolling Game", font=("Arial", 40, "bold"), bg="darkgreen",fg="gold").pack(pady=10)

result_label = tk.Label(root, text="🎲", font=("Arial", 48), bg="darkgreen", fg="white")
result_label.pack(pady=10)

tk.Button(root, text="Roll Dice", font=("Arial", 25), bg="red", fg="white", command=roll_dice).pack(pady=10)

count_label = tk.Label(root, text="Total Rolls: 0", font=("Arial", 25), bg="darkgreen", fg="lightgray")
count_label.pack(pady=10)

tk.Button(root, text="Exit Game",font=("Arial", 25), bg="black", fg="white", command=exit_game).pack(pady=20)

root.mainloop()