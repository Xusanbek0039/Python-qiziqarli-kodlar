from tkinter import *
from tkinter import ttk
 
root = Tk()
root["bg"]="gold"

raqam=Label(text="Telefon raqamni kiriting:",bg="gold").pack()

raqamni_olish=Entry()
raqamni_olish.pack()

malumotlar=[]

ustunlar = ("number","company")
tree= ttk.Treeview(columns=ustunlar, show="headings")
tree.heading("number", text="Tel-raqam")
tree.heading("company", text="Kompaniya")
tree.pack(fill=BOTH, expand=1)

def saqlash():
 t=raqamni_olish.get()
 kod=t[:2]
 ikod=int(kod)
 malumotlar.clear()
 c=""
 if ikod in [91,90]:
 	c="Beeline"
 elif ikod==33:
 	c="Humans"
 elif ikod in [99,95]:
 	c="Uzmobile"
 elif ikod in [93,94,50]:
 	c="Ucell"
 elif ikod==97:
 	c="MobiUZ"
 else:
 	c="-"
 malumotlar.append((f"+998 ({kod}) {t[2:]}",c))
 for malumot in malumotlar:
 	tree.insert("", END, values=malumot)
 	
saqlash_tugmasi=Button(text="Saqlash",command=saqlash,bg="gold").pack()

root.mainloop()