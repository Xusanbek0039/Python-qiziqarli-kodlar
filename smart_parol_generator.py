from tkinter import *
import string, random

def uzgarish():
	p=int(parol_uzunligi.get())
	if 4<=p<=5:
		tasvir["text"]="SODDA"
		tasvir["fg"]="white"
		tasvir["bg"]="crimson"
	elif 6<=p<=10:
		tasvir["text"]="NORMAL"
		tasvir["bg"]="orange"
		tasvir["fg"]="black"
	else:
		tasvir["text"]="XAVFSIZ"
		tasvir["bg"]="lawngreen"
		tasvir["fg"]="black"

def password():
	p=int(parol_uzunligi.get())
	elementlar = string.ascii_letters + string.digits + string.punctuation
	asosiy = "".join(random.choice(elementlar) for _ in range(p))
	parol.delete("1.0",END)
	parol.insert(END,asosiy)

oyna=Tk()
oyna["bg"]="black"

parol_sharti=Label(text="Parol uzunligini kiriting:",
font="TkFixedFont",
bg="black",
fg="white").pack()

parol_uzunligi=Spinbox(from_="4.0",to="15.0",
width=2,
command=uzgarish)
parol_uzunligi.pack(pady=20)

generatsiya=Button(text="Generatsiya",
bg="black",
fg="white",
activebackground="white",
font="TkCaptionFont",
command=password).pack()

parol_xavfsizligi=Label(text="Parol xavfsizligi:",
bg="black",
fg="white",
font="TkFixedFont").pack(pady=10)

tasvir=Label(text="SODDA",
width=13,
font="TkCaptionFont",
fg="white",
bg="crimson")
tasvir.pack(pady=10)

parol=Text(width=17,
height=1,
bg="black",
fg="white")
parol.pack(pady=10)

oyna.mainloop()