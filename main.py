import random
import tkinter as tk
from tkinter import messagebox

# Theme Config & State
BG, CARD, CYAN, WHITE = "#1A1C29", "#25283D", "#00E5FF", "#FFFFFF"
history = []

def roll_dice():
    # 1. Logic
    num_dice = int(dice_count_var.get())
    rolls = [random.randint(1, 6) for _ in range(num_dice)]
    dice_sum = sum(rolls)
    history.append(dice_sum)
    
    # 2. Update UI
    result_label.config(text="  ".join([f"🎲 {r}" for r in rolls]))
    sum_label.config(text=f"TOTAL SUM: {dice_sum}")
    
    stats_text = f"Rolls: {len(history)}  |  Min: {min(history)}  |  Max: {max(history)}  |  Avg: {sum(history)/len(history):.1f}"
    stats_label.config(text=stats_text)
    history_label.config(text=f"Last 5: {str(history[-5:])[1:-1]}")

def reset_game():
    history.clear()
    result_label.config(text="🎲")
    sum_label.config(text="TOTAL SUM: 0")
    stats_label.config(text="Rolls: 0  |  Min: 0  |  Max: 0  |  Avg: 0.0")
    history_label.config(text="Last 5: -")
    dice_count_var.set("1")

# Window Setup
root = tk.Tk()
root.title("Neon Dice Arena")
root.geometry("420x580")
root.configure(bg=BG)

# UI Elements
tk.Label(root, text="D I C E   A R E N A", font=("Impact", 32), bg=BG, fg=CYAN).pack(pady=20)

# Selector
select_frame = tk.Frame(root, bg=BG)
select_frame.pack(pady=10)
tk.Label(select_frame, text="DICE COUNT:", font=("Arial Black", 10), bg=BG, fg="#8F94FB").pack(side=tk.LEFT, padx=5)
dice_count_var = tk.StringVar(value="1")
tk.OptionMenu(select_frame, dice_count_var, "1", "2", "3").pack(side=tk.LEFT)

# Display Box
result_label = tk.Label(root, text="🎲", font=("Arial", 40), bg=BG, fg=WHITE)
result_label.pack(pady=10)
sum_label = tk.Label(root, text="TOTAL SUM: 0", font=("Arial Black", 14), bg=BG, fg=CYAN)
sum_label.pack(pady=5)

# Buttons
btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(pady=15)
tk.Button(btn_frame, text="ROLL", font=("Arial Black", 12), bg="#FF007F", fg=WHITE, width=8, command=roll_dice).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="RESET", font=("Arial Black", 12), bg="#FFB300", fg=BG, width=8, command=reset_game).pack(side=tk.LEFT, padx=5)

# Dashboard
stats_label = tk.Label(root, text="Rolls: 0  |  Min: 0  |  Max: 0  |  Avg: 0.0", font=("Arial Black", 10), bg=BG, fg=CYAN)
stats_label.pack(pady=15)
history_label = tk.Label(root, text="Last 5: -", font=("Arial", 11, "italic"), bg=BG, fg="#8F94FB")
history_label.pack(pady=5)

tk.Button(root, text="EXIT", font=("Arial Black", 10), bg="#3A3D52", fg=WHITE, command=lambda: [messagebox.showinfo("Thanks", "Thank you!"), root.destroy()]).pack(pady=25)

root.mainloop()