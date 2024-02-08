from tkinter import *
from tkinter import messagebox

oyna=Tk()
oyna["bg"]="black"

name=Label(text="UZBEKCOIN",
width=100,
fg="white",
bg="steelblue",
font="TkCaptionFont").pack()

qul=1
coin=0

liga=Label(text="Liga: Bronza",
bg="gold",
width=100,
font="TkCaptionFont")

tap=Label(text="Energiya: 1",
bg="steelblue",
fg="white",
width=100,
font="TkCaptionFont")

coinlar=Label(text="0 UZBEKCOIN",
bg="crimson",
width=100,
fg="white",
font="TkCaptionFont")

def buy():
	global qul, coin
	qul+=1
	coin-=50
	messagebox.showinfo(title="Energiya",message=f"Yangi energiya sotib oldingiz!\nEnergiya: {qul}")
	tap["text"]=f"Energiya: {qul}"
	coinlar["text"]=f"{coin} UZBEKCOIN"

kumush,oltin,platina = False,False,False

def mining():
	global coin,kumush,oltin,platina
	if coin==100 and not kumush:
		messagebox.showinfo(title="Liga kutarildi",message=f"Yangi liga: Kumush")
		liga["text"]="Liga: Kumush"
		kumush=True
	elif coin==1000 and not oltin:
		messagebox.showinfo(title="Liga kutarildi",message=f"Yangi liga: Oltin")
		liga["text"]="Liga: Oltin"
		oltin=True
	elif coin==100000 and not platina:
		messagebox.showinfo(title="Liga kutarildi",message=f"Yangi liga: Platina")
		liga["text"]="Liga: Platina"
		platina=True
	coin+=qul
	coinlar["text"]=f"{coin} UZBEKCOIN"

liga.pack()
tap.pack()
coinlar.pack()

click=Button(text="MENGA BOSING",
bg="white",
fg="black",
font="TkCaptionFont",
activebackground="gold",
command=mining).pack(pady=50)

magazin=Label(text="Magazin",
bg="gold",
width=100,
font="TkCaptionFont").pack()

enegiya_buy=Button(text="Energiya (+1) - 50 UZBEKCOIN",
fg="white",
font="TkCaptionFont",
activebackground="gold",
bg="steelblue",
command=buy).pack(pady=50)

oyna.mainloop()