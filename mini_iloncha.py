import tkinter as tk
import random

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg='black')
        self.canvas.pack()
        
        self.snake = [(20, 20)]
        self.food = self.create_food()
        self.direction = 'Right'
        self.score = 0
        self.speed = 300 # Скорость змейки
        
        self.draw_snake()
        self.draw_food()
        
        self.root.bind("<KeyPress>", self.change_direction)
        
        btn_left = tk.Button(root, text="Chapga", command=lambda: self.change_direction('Left'))
        btn_left.pack(side=tk.BOTTOM)
        btn_right = tk.Button(root, text="O'nga", command=lambda: self.change_direction('Right'))
        btn_right.pack(side=tk.BOTTOM)
        btn_up = tk.Button(root, text="Tepaga", command=lambda: self.change_direction('Up'))
        btn_up.pack(side=tk.BOTTOM)
        btn_down = tk.Button(root, text="Pastga", command=lambda: self.change_direction('Down'))
        btn_down.pack(side=tk.BOTTOM)
        
        self.game_loop()
    
    def create_food(self):
        x = random.randint(0, 19) * 20
        y = random.randint(0, 19) * 20
        return (x, y)
    
    def draw_snake(self):
        self.canvas.delete('snake')
        for x, y in self.snake:
            self.canvas.create_rectangle(x, y, x+20, y+20, fill='green', tag='snake')
    
    def draw_food(self):
        x, y = self.food
        self.canvas.create_oval(x, y, x+20, y+20, fill='red', tag='food')
    
    def change_direction(self, direction):
        if direction in ['Up', 'Down', 'Left', 'Right']:
            self.direction = direction
    
    def game_loop(self):
        x, y = self.snake[0]
        
        if self.direction == 'Up':
            y -= 20
        elif self.direction == 'Down':
            y += 20
        elif self.direction == 'Left':
            x -= 20
        elif self.direction == 'Right':
            x += 20
        
        self.snake.insert(0, (x, y))
        
        if self.food in self.snake:
            self.score += 10
            self.food = self.create_food()
            self.draw_food()
        else:
            self.snake.pop()
        
        self.draw_snake()

        self.root.after(self.speed, self.game_loop) # Используем скорость для задержки обновления
        
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()