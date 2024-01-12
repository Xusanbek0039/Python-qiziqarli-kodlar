from tkinter import *
import string, random

oyna = Tk()
oyna["bg"] = "#1B4F72"

matn = Label(text="Sizning parolingiz", bg="#1B4F72", fg="white")

def parol():
    elementlar = string.ascii_letters + string.digits + string.punctuation
    asosiy = "".join(random.choice(elementlar) for _ in range(10))
    matn['text'] = asosiy

tugma = Button(text="Generatsiya", command=parol, bg="#00BFFF")

matn.pack(pady=100)
tugma.pack()

oyna.mainloop()
