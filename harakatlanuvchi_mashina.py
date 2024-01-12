import tkinter as tk
window = tk.Tk()
window["bg"]="black"

canvas_width = 800
canvas_height = 400
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height,bg="white")
canvas.pack()

car_width = 100
car_height = 50
car_x = 0
car_y = canvas_height // 2 - car_height // 2
car = canvas.create_rectangle(car_x, car_y, car_x + car_width, car_y + car_height, fill="black")

def move_car():
    global car_x
    car_x += 5
    canvas.move(car, 5, 0)
    if car_x < canvas_width:
        window.after(100, move_car)

s=tk.Label(text="Speed: 100",fg="black")
s.pack()

move_car()
window.mainloop()




