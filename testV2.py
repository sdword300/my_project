import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("لعبة XO")
        
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.player1_score = 0
        self.player2_score = 0
        
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text=" ", width=10, height=3,
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j)
                self.buttons.append(button)
                
        self.scoreboard = tk.Label(root, text=f"نتيجة اللعبة: لاعب 1: {self.player1_score}, لاعب 2: {self.player2_score}")
        self.scoreboard.grid(row=3, columnspan=3)
        
    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("نتيجة اللعبة", f"اللاعب {self.current_player} فاز!")
                if self.current_player == "X":
                    self.player1_score += 1
                else:
                    self.player2_score += 1
                self.update_scoreboard()
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("نتيجة اللعبة", "تعادل!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()
    
    def ai_move(self):
        empty_indices = [i for i, val in enumerate(self.board) if val == " "]
        index = random.choice(empty_indices)
        self.board[index] = "O"
        self.buttons[index].config(text="O")
        if self.check_winner():
            messagebox.showinfo("نتيجة اللعبة", "اللاعب AI فاز!")
            self.player2_score += 1
            self.update_scoreboard()
            self.reset_game()
        elif " " not in self.board:
            messagebox.showinfo("نتيجة اللعبة", "تعادل!")
            self.reset_game()
        else:
            self.current_player = "X"
    
    def check_winner(self):
        lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6)]
        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False
    
    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text=" ")
        self.current_player = "X"
    
    def update_scoreboard(self):
        self.scoreboard.config(text=f"نتيجة اللعبة: لاعب 1: {self.player1_score}, لاعب 2: {self.player2_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
