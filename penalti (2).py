from tkinter import *
from tkinter import PhotoImage
import random

root=Tk()
root["bg"]="white"

nw="/storage/emulated/0/Documents/pixelLab/20240220_190704.png"

lg="/storage/emulated/0/Documents/pixelLab/20240220_190718.png"

rg="/storage/emulated/0/Documents/pixelLab/20240220_190604.png"

goal="/storage/emulated/0/Documents/pixelLab/20240220_193252.png"

nn="/storage/emulated/0/Documents/pixelLab/20240220_193335.png"

def main(text):
	bot=random.choice(["LEFT","CENTER","RIGHT"])
	if bot==text:
		noway=PhotoImage(file=nw)
		goalkeeper.configure(image=noway)
		goalkeeper.image=noway
		no=PhotoImage(file=nn)
		rr.configure(image=no)
		rr.image=no
	elif text=="LEFT":
		leftgol=PhotoImage(file=lg)
		goalkeeper.configure(image=leftgol)
		goalkeeper.image=leftgol
		gg=PhotoImage(file=goal)
		rr.configure(image=gg)
		rr.image=gg
	elif text=="CENTER":
		noway=PhotoImage(file=nw)
		goalkeeper.configure(image=noway)
		goalkeeper.image=noway
		no=PhotoImage(file=nn)
		rr.configure(image=no)
		rr.image=no
	elif text=="RIGHT":
		rightgol=PhotoImage(file=rg)
		goalkeeper.configure(image=rightgol)
		goalkeeper.image=rightgol
		gg=PhotoImage(file=goal)
		rr.configure(image=gg)
		rr.image=gg
		
gk=PhotoImage(file="/storage/emulated/0/Download/20240220_190109.png")
ri=PhotoImage(file="/storage/emulated/0/Documents/pixelLab/20240220_190810.png")

goalkeeper=Label(image=gk)
rr=Label(image=ri)

goalkeeper.pack()
rr.pack()

for b in ["LEFT","CENTER","RIGHT"]:
	bb=Button(text=b,
	width=30,
	bg="black",
	fg="white",
	font="TkCaptionFont",
	command=lambda text=b: main(text)).pack()
	


root.mainloop()