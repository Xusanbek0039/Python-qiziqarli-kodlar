from tkinter import *
import random, time

oyna=Tk()
oyna["bg"]="black"

uyin_ismi=Label(text="TDM PUBG",bg="#1E90FF",width=100,fg="white").pack()

user=Label(text="Ismingizni kiriting:",bg="black",fg="white").pack()

ism_entry=Entry()
ism_entry.pack()

group1={}
group2={}

automatlar=["AKM","M16A4","SCAR-L","M416","GROZA","M762","KAR-98","AWM","M24","TOVA"]

stat1={}
stat2={}

info1=Label(text="",bg="black",fg="white",width=40)
info2=Label(text="",bg="black",fg="white",width=40)

s1=0
s2=0

info=Label(text="Malumotlar",width=20,height=5,bg="gold")

def start():
    global s1, s2
    m = random.choice([group1, group2])
    d = random.choice(list(m.keys()))
    if m is group1:
        r = random.choice(list(stat2.keys()))
        info1["text"] = f"{d}({group1.get(d)}) {r} ni uldirdi"
        s1 += 1
    else:
        r = random.choice(list(stat1.keys()))
        info2["text"] = f"{d}({group2.get(d)}) {r} ni uldirdi"
        s2 += 1
    info["text"] = f"Hisob:\n{s1}-{s2}"

	
		
def ism_tasdiq():
	ism=ism_entry.get()
	group1[ism]=random.choice(automatlar)
	stat1[ism]=0
	for i in range(4):
		a=random.choice(automatlar)
		b=random.randint(1,1000)
		group1[f"Player {b}"]=a
		stat1[f"Player {b}"]=0
	for i in range(5):
		a=random.choice(automatlar)
		b=random.randint(1,1000)
		group2[f"Player {b}"]=a
		stat2[f"Player {b}"]=0
	boshlash=Button(text="Otishma",command=start,bg="#3CB371",fg="white").pack()
	info1["text"]="\n".join(group1)
	info1["bg"]="#1E90FF"
	info2["text"]="\n".join(group2)
	info2["bg"]="crimson"
	
ism_btn=Button(text="Tasdiqlash",bg="#3CB371",fg="white",command=ism_tasdiq).pack(pady=10)

uyin_chegarasi=Label(text="",bg="#1E90FF",width=100,fg="white").pack()

info1.pack(pady=20)
info2.pack(pady=20)
info.pack()

oyna.mainloop()