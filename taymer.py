import tkinter as tk
from tkinter import messagebox

def start_timer():
    time_left = 60
    while time_left > 0:
        time_label.config(text=f"Vaqt qoldi: {time_left} sekund", bg="black",fg="red")
        time_left -= 1
        time_label.update()
        time_label.after(1000)
    messagebox.showinfo("Taymer", "Vaqt buldi!")

root = tk.Tk()
root["bg"]="black"
root.geometry("300x200")

time_label = tk.Label(root, text="Vaqt qoldi: 60 sekund", font=("Arial", 16), bg="black",fg="cadetblue")
time_label.pack(pady=50)

start_button = tk.Button(root, text="Boshlash", command=start_timer,bg="cadetblue",fg="white")
start_button.pack()

root.mainloop()