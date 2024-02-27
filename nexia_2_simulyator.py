from tkinter import *
import time, random

def boost(speed_label):
    rr=random.randint(1,61)
    pr["text"]=f"Pressure: {rr}/60 P"
    ss=random.randint(120,500)
    acc["text"]=f"Acceleration: {ss} A"
    x = 0
    for i in range(180):
        time.sleep(0.01)
        x += 1
        speed_label.config(text="Speed: " + str(x) + "/180 km/h")
        speed_label.update()
        
oyna = Tk()
oyna.configure(bg="white")

Label(text="NEXIA 2 SIMULYATOR", bg="black", fg="white", width=100, font="TkCaptionFont").pack()

rasm1 = PhotoImage(file="/storage/emulated/0/Pictures/nexia-2-blog.png")
Label(image=rasm1, bg="white").pack()

speed = Label(text="Speed: 0/180 km/h", fg="white", bg="black", font="TkCaptionFont", width=100)
speed.pack()

pr=Label(text="Pressure: 0/60 P", fg="black", bg="white", font="TkCaptionFont", width=100)
pr.pack()
acc=Label(text="Acceleration: 0 A", fg="white", bg="black", font="TkCaptionFont", width=100)
acc.pack()

Button(text="BOOST", width=50, height=30, font=("Arial", 32), bg="black", fg="white", activebackground="white", activeforeground="black", command=lambda: boost(speed)).pack()

oyna.mainloop()



