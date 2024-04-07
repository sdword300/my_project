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
        
        self.create_board()
        self.create_scoreboard()
    
    def create_board(self):
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text=" ", width=10, height=3,
                                   font=("Arial", 24, "bold"),
                                   command=lambda row=i, col=j: self.on_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)
    
    def create_scoreboard(self):
        self.score_label = tk.Label(self.root, text="نتيجة اللعبة:", font=("Arial", 16))
        self.score_label.grid(row=3, column=0, columnspan=3, pady=10)
        
        self.player1_label = tk.Label(self.root, text=f"لاعب 1: {self.player1_score}", font=("Arial", 14))
        self.player1_label.grid(row=4, column=0, padx=10)
        
        self.player2_label = tk.Label(self.root, text=f"لاعب 2: {self.player2_score}", font=("Arial", 14))
        self.player2_label.grid(row=4, column=1, padx=10)
    
    def on_click(self, row, col):
        index = row * 3 + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state=tk.DISABLED)
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
        index = self.get_best_move(empty_indices)
        self.board[index] = "O"
        self.buttons[index].config(text="O", state=tk.DISABLED)
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
    
    def get_best_move(self, empty_indices):
        best_score = -float("inf")
        best_move = None
        for index in empty_indices:
            self.board[index] = "O"
            score = self.minimax(False)
            self.board[index] = " "
            if score > best_score:
                best_score = score
                best_move = index
        return best_move
    
    def minimax(self, is_maximizing):
        if self.check_winner():
            return 1 if not is_maximizing else -1
        elif " " not in self.board:
            return 0
        
        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "O"
                    score = self.minimax(False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "X"
                    score = self.minimax(True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score
    
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
            self.buttons[i].config(text=" ", state=tk.NORMAL)
        self.current_player = "X"
    
    def update_scoreboard(self):
        self.player1_label.config(text=f"لاعب 1: {self.player1_score}")
        self.player2_label.config(text=f"لاعب 2: {self.player2_score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
