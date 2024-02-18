from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

oyna=Tk()
oyna["bg"]="white"

evos=Label(text="EVOS",
bg="BlueViolet",
fg="white",
font="TkCaptionFont",
width=100).pack()

total=0
main=[]

m1="Kombo Student"
m2="Kombo Detskoy"

def plus1():
	global total
	total+=18000
	savat["text"]=f"Savatga: ({total}) sum\nSotib olish"
	main.append(m1)

def plus2():
	global total
	total+=18000
	savat["text"]=f"Savatga: ({total}) sum\nSotib olish"
	main.append(m2)
	
def minus1():
	global total
	total-=18000
	savat["text"]=f"Savatga: ({total}) sum\nSotib olish"
	main.remove(m1)

def minus2():
	global total
	total-=18000
	savat["text"]=f"Savatga: ({total}) sum\nSotib olish"
	main.remove(m2)

def hisob():
	e1=main.count(m1)
	e2=main.count(m2)
	messagebox.showinfo(title="Hisob",message=f"{m1}: {e1} ta ({18000*e1}) sum\n{m2}: {e2} ta ({18000*e2}) sum")

i1 = PhotoImage(file="image.png")

l1=Label(image=i1).pack()

i1_narxi=Label(text="18000",
bg="white",
font=("Arial",10),
fg="BlueViolet").pack()

i1_plus=Button(text="+1",
bg="BlueViolet",
fg="white",command=plus1).pack()

i1_minus=Button(text="-1",
fg="BlueViolet",
bg="white",command=minus1).pack()

i2=PhotoImage(file="image.png")

l2=Label(image=i2).pack()

i2_narxi=Label(text="18000",
bg="white",
font=("Arial",10),
fg="BlueViolet").pack()

i2_plus=Button(text="+1",
bg="BlueViolet",
fg="white",command=plus2).pack()

i2_minus=Button(text="-1",
fg="BlueViolet",
bg="white",command=minus2).pack()

savat=Button(text=f"Savatga: ({total}) sum\nSotib olish",
width=100,
height=50,
bg="BlueViolet",
fg="white",
font="TkCaptionFont",
activebackground="white",
command=hisob)
savat.pack()

oyna.mainloop()