from tkinter import *

oyna = Tk()
oyna["bg"]="#00BFFF"

username = Label(text="Username",bg="#00BFFF",font="TkFixedFont")
username.pack(pady=10)

user_entry = Entry()
user_entry.pack()

password = Label(text="Password",bg="#00BFFF",font="TkFixedFont")
password.pack(pady=10)

pass_entry = Entry()
pass_entry.pack()

login = Button(text="Login",bg="gold")
login.pack(pady=10)

oyna.mainloop()





