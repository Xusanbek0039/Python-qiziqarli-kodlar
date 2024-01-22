from tkinter import *
oyna=Tk()
oyna["bg"]="white"

jadval={"Dushanba": ["matematika","ona-tili","rus-tili","fizika","kimyo"],"Seshanba": ["tarih","geometriya","algebra","mehnat"],"Chorshanba": ["kimyo","fizika","jismon-tarbiya","rus-tili"],"Payshanba": ["uzbek-tili","fizika","rus-tili","ona-tili"],"Juma":["algebra","geometriya","mehnat"],"Shanba": ["jismon-tarbiya","uzbek-tili","tarih"]}

fan_info=Label(text="Malumotlar",width=20,height=10,bg="gold")

def fanlar(kun):
	fan=jadval.get(kun)
	fan_info["text"]="\n".join(fan)

for kun in jadval:
	kunlar=Button(text=kun,width=100, bg="slateblue",fg="white",command=lambda kun=kun: fanlar(kun)).pack()

fan_info.pack(pady=500)	
oyna.mainloop()