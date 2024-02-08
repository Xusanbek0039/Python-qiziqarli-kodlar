from tkinter import *
import requests

def get_html():
	url=entry.get()
	r=requests.get(url)
	h=r.text
	text.delete("1.0",END)
	text.insert(END,h)

root=Tk()
l=Label(text="Enter URL:").pack()
entry=Entry(width=50)
entry.pack()
b=Button(text="Get HTML Code", command=get_html).pack()
text=Text(height=20,width=100)
text.pack()
root.mainloop()



