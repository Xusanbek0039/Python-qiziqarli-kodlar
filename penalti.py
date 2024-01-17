from tkinter import *
import random

penalti=Tk()
penalti["bg"]="black"

varatar=Label(text="VARATAR",bg="dodgerblue",width=100,fg="white").pack()
varatarist=Label(text="VARATARIST",bg="white",fg="dodgerblue",width=100).pack()
surov=Label(text="QAYERGA TEPMOQCHISIZ?",bg="dodgerblue",fg="white",width=100).pack()

elementlar="chapga","o'rtaga","o'nga"

malumot=Label(text="O'yin haqida malumot",bg="dodgerblue",fg="white",width=100)

gol_golmas=Label(text="Gollar haqida malumot",width=100,bg="white",fg="dodgerblue")

gol,golmas=0,0

def chapga():
	global gol, golmas
	bot_varatar=random.choice(elementlar)
	if bot_varatar!="chapga":
		malumot["text"]=f"Varatar {bot_varatar} sakradi, siz gol urdingiz"
		gol+=1
	else:
		malumot["text"]=f"Varatar ham {bot_varatar} ga sakradi, siz gol urolmadingiz"
		golmas+=1
	gol_golmas["text"]=f"Gollar soni {gol} ta | Urolmagan gollaringiz {golmas} ta"
	
		
def urtaga():
	global gol, golmas
	bot_varatar=random.choice(elementlar)
	if bot_varatar!="o'rtaga":
		malumot["text"]=f"Varatar {bot_varatar} sakradi, siz gol urdingiz"
		gol+=1
	else:
		malumot["text"]=f"Varatar ham {bot_varatar} ga sakradi, siz gol urolmadingiz"
		golmas+=1
	gol_golmas["text"]=f"Gollar soni {gol} ta | Urolmagan gollaringiz {golmas} ta"

def unga():
	global gol, golmas
	bot_varatar=random.choice(elementlar)
	if bot_varatar!="o'nga":
		malumot["text"]=f"Varatar {bot_varatar} sakradi, siz gol urdingiz"
		gol+=1
	else:
		malumot["text"]=f"Varatar ham {bot_varatar} ga sakradi, siz gol urolmadingiz"
		golmas+=1
	gol_golmas["text"]=f"Gollar soni {gol} ta | Urolmagan gollaringiz {golmas} ta"

tugma1=Button(text="CHAPGA",command=chapga,bg="white",width=100,fg="dodgerblue").pack()
tugma2=Button(text="O'RTAGA", command=urtaga,bg="white",fg="dodgerblue",width=100).pack()
tugma3=Button(text="O'NGA",command=unga,bg="white",fg="dodgerblue",width=100).pack()

malumot.pack()
gol_golmas.pack()

penalti.mainloop()