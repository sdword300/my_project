import tkinter as tk
from tkinter import messagebox
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("XOلعبة ")
        
        self.current_player = 'X'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.winner_frame = None
        
        self.create_board()
    
    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text='', width=10, height=4,
                                               command=lambda row=i, col=j: self.click_button(row, col))
                self.buttons[i][j].grid(row=i, column=j)
    
    def click_button(self, row, col):
        if not self.buttons[row][col].cget('text'):
            self.buttons[row][col].config(text=self.current_player)
            if self.check_winner(row, col):
                self.show_winner_message(f"اللاعب {self.current_player} فاز!")
            elif self.check_draw():
                messagebox.showinfo("نهاية اللعبة", "تعادل!")
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                if self.current_player == 'O':  # دور الـ AI
                    self.ai_move()
    
    def ai_move(self):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if not self.buttons[i][j].cget('text')]
        if empty_cells:
            cell = random.choice(empty_cells)
            self.click_button(cell[0], cell[1])
    
    def check_winner(self, row, col):
        player = self.buttons[row][col].cget('text')
        for i in range(3):
            if (
                self.buttons[row][i].cget('text') == player and
                self.buttons[row][(i+1)%3].cget('text') == player and
                self.buttons[row][(i+2)%3].cget('text') == player
            ) or (
                self.buttons[i][col].cget('text') == player and
                self.buttons[(i+1)%3][col].cget('text') == player and
                self.buttons[(i+2)%3][col].cget('text') == player
            ):
                self.show_winner_message(f"اللاعب {player} فاز!")
                return True
        if row == col:
            if (
                self.buttons[0][0].cget('text') == player and
                self.buttons[1][1].cget('text') == player and
                self.buttons[2][2].cget('text') == player
            ):
                self.show_winner_message(f"اللاعب {player} فاز!")
                return True
        if row + col == 2:
            if (
                self.buttons[0][2].cget('text') == player and
                self.buttons[1][1].cget('text') == player and
                self.buttons[2][0].cget('text') == player
            ):
                self.show_winner_message(f"اللاعب {player} فاز!")
                return True
        return False
    
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if not self.buttons[i][j].cget('text'):
                    return False
        return True
    
    def show_winner_message(self, message):
        if self.winner_frame:
            self.winner_frame.destroy()
        self.winner_frame = tk.Frame(self.root, bg='green', padx=10, pady=10)
        self.winner_frame.grid(row=3, columnspan=3)
        label = tk.Label(self.winner_frame, text=message, font=('Arial', 14))
        label.pack()
        # عرض رسالة الفوز لمدة 5 ثوانٍ ثم إعادة تعيين اللعبة
        self.root.after(5000, self.reset_game)
    
    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.current_player = 'X'
        if self.winner_frame:
            self.winner_frame.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
