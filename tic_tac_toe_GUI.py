import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("420x500")
root.resizable(False, False)

# Beige Theme Colors
bg_color = "#f5f5dc"      # beige background
button_bg = "#fffaf0"     # soft cream buttons
grid_color = "#d2b48c"    # tan border
x_color = "#8b0000"       # dark red X
o_color = "#2f4f4f"       # dark slate gray O

current_player = "X"
buttons = []
game_active = True

root.configure(bg=bg_color)

def check_winner():
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if (buttons[condition[0]]["text"] ==
            buttons[condition[1]]["text"] ==
            buttons[condition[2]]["text"] != ""):
            return True
    return False

def check_draw():
    for btn in buttons:
        if btn["text"] == "":
            return False
    return True

def button_click(index):
    global current_player, game_active

    if buttons[index]["text"] == "" and game_active:
        buttons[index]["text"] = current_player

        if current_player == "X":
            buttons[index]["fg"] = x_color
        else:
            buttons[index]["fg"] = o_color

        if check_winner():
            messagebox.showinfo("Game Over", f"Player {current_player} Wins!")
            game_active = False
        elif check_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            game_active = False
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global current_player, game_active
    current_player = "X"
    game_active = True
    for btn in buttons:
        btn.config(text="", fg="black")

# Grid Frame
frame = tk.Frame(root, bg=bg_color)
frame.pack(pady=30)

for i in range(9):
    btn = tk.Button(frame,
                    text="",
                    font=("Arial", 48, "bold"),
                    width=3,
                    height=1,
                    bg=button_bg,
                    activebackground="#f0e6d6",
                    bd=3,
                    relief="ridge",
                    highlightbackground=grid_color,
                    command=lambda i=i: button_click(i))
    btn.grid(row=i//3, column=i%3, padx=6, pady=6)
    buttons.append(btn)

# Restart Button
restart_btn = tk.Button(root,
                        text="Restart Game",
                        font=("Arial", 16, "bold"),
                        bg="#d2b48c",
                        fg="black",
                        activebackground="#c2a070",
                        bd=2,
                        command=reset_game)
restart_btn.pack(pady=20)

root.mainloop()
